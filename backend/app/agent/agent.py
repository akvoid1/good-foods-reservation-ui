from app.agent.llm import llm_client
from app.agent.tools import TOOLS
from app.services.venue_service import VenueService
from app.services.reservation_service import ReservationService
from typing import Dict, Any, List
import json


SYSTEM_PROMPT = """You are GoodFoods AI, a friendly and helpful restaurant reservation assistant. Your role is to help users:

1. **Discover restaurants** - Search and recommend venues based on preferences (cuisine, location, price, ambiance)
2. **Get information** - Provide details about specific restaurants (hours, menu, amenities)
3. **Make reservations** - Book tables after confirming availability and collecting contact info
4. **Manage bookings** - Help users view or modify their reservations

**Conversation Guidelines:**
- Be warm, conversational, and enthusiastic about food
- Ask clarifying questions when needed (party size, date/time, dietary preferences)
- Provide 2-3 recommendations at a time, not overwhelming lists
- When showing restaurant recommendations, ALWAYS include the venue name, city, rating, and key features
- When user asks about a specific restaurant by name, use get_venue_details with the venue_id from previous search results
- Always check availability before confirming reservations
- Collect contact info (name, phone, email) before finalizing bookings
- Confirm all details before creating a reservation
- Use natural language, avoid being robotic

**Tool Usage:**
- Use search_venues to find restaurants matching user criteria
- When user mentions a restaurant name from your recommendations, extract the venue_id from the search results and use get_venue_details
- Use check_availability before booking
- Use create_reservation only after confirming all details with user

**Important: Handling Restaurant Inquiries:**
- When presenting search results, format each restaurant naturally like:
  "🍽️ Restaurant Name in City
  ⭐ Rating • Price tier ($ to $$$$)
  Brief description highlighting key features"
- NEVER show venue IDs to users - keep them internal only
- NEVER use markdown formatting (**bold**, *italic*, etc.) - use plain text with emojis
- When you provide recommendations from search_venues, internally remember the venue IDs from the results
- If user asks about a restaurant you just recommended (e.g., "tell me about Tandoor Palace"), use the venue_id from your previous search results to call get_venue_details
- The search_venues tool returns a list with 'id', 'name', 'city', 'rating', 'description' fields - use the 'id' field for get_venue_details
- Present restaurant details including: full address, phone, operating hours, price tier, capacity, and special features
- Keep responses conversational and easy to read

**Response Style:**
- Keep responses concise but friendly
- Use emojis sparingly (🍽️ 🎉 ✨ ⭐ 💰) for visual appeal
- Format recommendations with clear line breaks for readability
- Use bullet points or numbered lists when showing multiple options
- Always end with a helpful question or next step
- Make responses feel natural and conversational, not robotic

**Example Good Response Format:**
"I found some great Italian spots for you! 🍝

🍽️ Trattoria Roma in New York
⭐ 4.8 • $$ • Cozy atmosphere
Authentic pasta and wood-fired pizzas

🍽️ Osteria Bella in New York  
⭐ 4.6 • $$$ • Romantic setting
Fresh seafood and homemade pasta

Which one sounds good to you?"

IMPORTANT: Do NOT use markdown formatting like **bold** or *italic* - just use plain text with emojis for emphasis.

Remember: You're helping people have great dining experiences!"""

class Agent:
    def __init__(self, db):
        self.db = db
        self.venue_service = VenueService(db)
        self.reservation_service = ReservationService(db)
    
    async def process_message(self, session_id: str, message: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Process user message with tool calling
        """
        # Build conversation history
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": message}
        ]
        
        # Call LLM with tools
        response = llm_client.chat_completion(messages=messages, tools=TOOLS)
        
        # Check if LLM wants to use tools
        tool_calls = llm_client.parse_tool_calls(response)
        
        if tool_calls:
            # Execute tools and get results
            tool_results = []
            venues_data = []
            
            for tool_call in tool_calls:
                result = await self._execute_tool(tool_call, session_id)
                tool_results.append(result)
                
                # Collect venue data for structured response
                if tool_call["name"] == "search_venues" and result.get("venues"):
                    venues_data = result["venues"]
            
            # Format response with tool results
            if venues_data:
                venue_names = [v["name"] for v in venues_data[:3]]
                response_text = f"I found some great options for you: {', '.join(venue_names)}. Would you like to know more about any of these?"
                
                return {
                    "type": "tool_result",
                    "text": response_text,
                    "suggested_replies": ["Tell me more", "Book one", "Different options"],
                    "structured": {
                        "intent": "recommendation",
                        "venues": venues_data
                    }
                }
            else:
                # Tool executed but no venues (e.g., reservation created)
                result_text = tool_results[0].get("message", "Done!")
                return {
                    "type": "tool_result",
                    "text": result_text,
                    "suggested_replies": ["View my bookings", "Find another restaurant"],
                    "structured": None
                }
        
        # No tool calls - just return LLM response
        text_response = llm_client.get_text_response(response)
        return {
            "type": "llm_response",
            "text": text_response,
            "suggested_replies": ["Show me options", "Tell me more", "Make a reservation"],
            "structured": None
        }
    
    async def _execute_tool(self, tool_call: Dict[str, Any], session_id: str) -> Dict[str, Any]:
        """
        Execute a tool call and return results
        """
        tool_name = tool_call["name"]
        arguments = tool_call["arguments"]
        
        if tool_name == "search_venues":
            # Handle optional parameters
            cuisine = arguments.get("cuisine") if arguments.get("cuisine") else None
            city = arguments.get("city") if arguments.get("city") else None
            
            venues = self.venue_service.search_venues(
                cuisine=cuisine,
                city=city,
                limit=10
            )
            return {"venues": [self._venue_to_dict(v) for v in venues]}
        
        elif tool_name == "get_venue_details":
            venue = self.venue_service.get_venue(arguments["venue_id"])
            if venue:
                return {"venue": self._venue_to_dict(venue)}
            return {"error": "Venue not found"}
        
        elif tool_name == "check_availability":
            available = self.venue_service.check_availability(
                arguments["venue_id"],
                arguments["datetime"],
                arguments["party_size"]
            )
            return {"available": available}
        
        elif tool_name == "create_reservation":
            reservation = self.reservation_service.create_reservation(
                session_id=session_id,
                venue_id=arguments["venue_id"],
                datetime_str=arguments["datetime"],
                party_size=arguments["party_size"],
                contact_name=arguments["contact_name"],
                contact_phone=arguments["contact_phone"],
                contact_email=arguments["contact_email"],
                notes=arguments.get("notes")
            )
            return {
                "message": f"Reservation confirmed! Your booking ID is {reservation.booking_id}",
                "reservation": self._reservation_to_dict(reservation)
            }
        
        return {"error": "Unknown tool"}
    
    def _venue_to_dict(self, venue) -> Dict[str, Any]:
        return {
            "id": venue.id,
            "name": venue.name,
            "cuisine": venue.cuisine,
            "rating": venue.rating,
            "capacity": venue.capacity,
            "price_tier": venue.price_tier,
            "city": venue.city,
            "image": venue.image,
            "tags": venue.tags or [],
            "distance_km": 2.5,  # Mock distance for now
            "score": 0.9
        }
    
    def _reservation_to_dict(self, reservation) -> Dict[str, Any]:
        return {
            "id": reservation.id,
            "booking_id": reservation.booking_id,
            "venue_id": reservation.venue_id,
            "venue_name": reservation.venue_name,
            "datetime": reservation.datetime.isoformat(),
            "party_size": reservation.party_size,
            "status": reservation.status
        }
