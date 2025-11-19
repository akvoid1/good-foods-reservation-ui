from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import CreateReservationRequest, ReservationResponse, ContactInfo
from app.services.reservation_service import ReservationService

router = APIRouter()


@router.post("/create", response_model=ReservationResponse)
async def create_reservation(
    request: CreateReservationRequest,
    session_id: str = Query(default="default_session"),
    db: Session = Depends(get_db)
):
    """
    Create a new reservation
    """
    try:
        # Get session ID from query parameter or use default
        if not session_id or session_id == "default_session":
            # Try to get from request body if available
            session_id = getattr(request, 'session_id', 'default_session')
        
        service = ReservationService(db)
        reservation = service.create_reservation(
            session_id=session_id,
            venue_id=request.venue_id,
            datetime_str=request.datetime,
            party_size=request.party_size,
            contact_name=request.contact.name,
            contact_phone=request.contact.phone,
            contact_email=request.contact.email,
            notes=request.notes
        )
        
        return ReservationResponse(
            id=reservation.id,
            venue_id=reservation.venue_id,
            venue_name=reservation.venue_name,
            datetime=reservation.datetime.isoformat(),
            party_size=reservation.party_size,
            status=reservation.status,
            contact=ContactInfo(
                name=reservation.contact_name,
                phone=reservation.contact_phone,
                email=reservation.contact_email
            ),
            notes=reservation.notes,
            booking_id=reservation.booking_id
        )
    except Exception as e:
        print(f"Reservation creation error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/", response_model=list[ReservationResponse])
async def get_reservations(
    session_id: str = Query(default="default_session"),
    db: Session = Depends(get_db)
):
    """
    Get all reservations for a session
    """
    try:
        service = ReservationService(db)
        reservations = service.get_reservations(session_id)
        
        return [
            ReservationResponse(
                id=r.id,
                venue_id=r.venue_id,
                venue_name=r.venue_name,
                datetime=r.datetime.isoformat(),
                party_size=r.party_size,
                status=r.status,
                contact=ContactInfo(
                    name=r.contact_name,
                    phone=r.contact_phone,
                    email=r.contact_email
                ),
                notes=r.notes,
                booking_id=r.booking_id
            )
            for r in reservations
        ]
    except Exception as e:
        print(f"Get reservations error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/{reservation_id}/cancel")
async def cancel_reservation(reservation_id: str, db: Session = Depends(get_db)):
    """
    Cancel a reservation
    """
    try:
        service = ReservationService(db)
        success = service.cancel_reservation(reservation_id)
        
        if not success:
            raise HTTPException(status_code=404, detail="Reservation not found")
        
        return {"success": True, "cancelled_id": reservation_id}
    except HTTPException:
        raise
    except Exception as e:
        print(f"Cancellation error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/admin")
async def get_all_reservations_admin(
    limit: int = Query(default=100),
    db: Session = Depends(get_db)
):
    """
    Get all reservations (admin view)
    Returns recent reservations across all sessions
    """
    try:
        service = ReservationService(db)
        reservations = service.get_all_reservations(limit=limit)
        
        result = []
        for r in reservations:
            try:
                # Validate email before adding
                email = r.contact_email if '@' in r.contact_email else 'invalid@example.com'
                
                result.append({
                    "id": r.id,
                    "venue_id": r.venue_id,
                    "venue_name": r.venue_name,
                    "datetime": r.datetime.isoformat(),
                    "party_size": r.party_size,
                    "status": r.status,
                    "contact": {
                        "name": r.contact_name,
                        "phone": r.contact_phone,
                        "email": email
                    },
                    "notes": r.notes,
                    "booking_id": r.booking_id
                })
            except Exception as e:
                print(f"Skipping invalid reservation {r.id}: {e}")
                continue
        
        return result
    except Exception as e:
        print(f"Admin reservations error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
