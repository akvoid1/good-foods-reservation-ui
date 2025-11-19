from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import AgentMessageRequest, AgentResponse, RecommendRequest
from app.agent.agent import Agent

router = APIRouter()


@router.post("/message", response_model=AgentResponse)
async def agent_message(request: AgentMessageRequest, db: Session = Depends(get_db)):
    """
    Process user message with LLM agent
    """
    try:
        agent = Agent(db)
        response = await agent.process_message(
            session_id=request.session_id,
            message=request.message,
            context=request.context
        )
        return response
    except Exception as e:
        print(f"Agent error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/recommend")
async def recommend_venues(request: RecommendRequest, db: Session = Depends(get_db)):
    """
    Get venue recommendations based on criteria
    """
    try:
        from app.services.venue_service import VenueService
        venue_service = VenueService(db)
        
        venues = venue_service.search_venues(
            cuisine=request.cuisine,
            city=request.city,
            party_size=request.party_size,
            price_tier=request.prefs.get("price_tier") if request.prefs else None
        )
        
        venues_data = [
            {
                "id": v.id,
                "name": v.name,
                "cuisine": v.cuisine,
                "rating": v.rating,
                "capacity": v.capacity,
                "price_tier": v.price_tier,
                "city": v.city,
                "image": v.image,
                "tags": v.tags or [],
                "distance_km": 2.5,
                "score": 0.9
            }
            for v in venues
        ]
        
        return {"venues": venues_data}
    except Exception as e:
        print(f"Recommendation error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
