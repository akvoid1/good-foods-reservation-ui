# GoodFoods - Conversation Flow Examples

This document demonstrates various user interaction patterns with the GoodFoods AI agent, showcasing its ability to handle diverse scenarios and intents.

---

## Flow 1: Simple Venue Search

**User Intent**: Find restaurants by cuisine

```
User: "Show me Italian restaurants"

Agent: [Calls search_venues(cuisine="Italian")]
       "I found some great Italian options for you: Pizzeria Bar, 
       The Pizzeria Garden. Would you like to know more about any of these?"

Structured Response:
- Type: tool_result
- Venues: 2 Italian restaurants
- Suggested replies: ["Tell me more", "Book one", "Different options"]

User: "Tell me more about Pizzeria Bar"

Agent: [Calls get_venue_details(venue_id="v001")]
       "Pizzeria Bar is a highly-rated Italian restaurant (4.9⭐) in New York. 
       They have a capacity of 120 people and are known for their wood-fired pizzas. 
       Price range: $$. Would you like to make a reservation?"

User: "Yes, book a table for 2 tonight at 7pm"

Agent: [Calls check_availability(venue_id="v001", datetime="2024-11-19T19:00:00", party_size=2)]
       "Great! Pizzeria Bar has availability for 2 people tonight at 7pm. 
       To complete your reservation, I'll need your name, phone number, and email."

User: "John Doe, +1-555-0123, john@example.com"

Agent: [Calls create_reservation(...)]
       "Perfect! Your reservation is confirmed at Pizzeria Bar for 2 people 
       tonight at 7:00 PM. Your booking ID is GF-ABC123. You'll receive a 
       confirmation email shortly."
```

**Key Features Demonstrated:**
- Natural language understanding
- Tool calling sequence
- Information gathering
- Booking confirmation

---

## Flow 2: Complex Multi-Criteria Search

**User Intent**: Find restaurant with specific requirements

```
User: "I need a romantic place for dinner, outdoor seating preferred, 
      not too expensive, somewhere in New York"

Agent: [Calls search_venues(city="New York", tags=["romantic", "outdoor seating"])]
       "I found some perfect romantic spots with outdoor seating in New York: 
       The Oak (Mediterranean, $$), Bella Italia (Italian, $$), 
       Mediterranean Grill (Greek, $$). All have great ambiance and outdoor areas."

Structured Response:
- Type: tool_result
- Venues: 3 restaurants matching criteria
- Filters applied: city, tags, price_tier

User: "What's the vibe like at The Oak?"

Agent: "The Oak is a Mediterranean restaurant with a quiet, intimate atmosphere. 
       It's known for its excellent wine selection and is perfect for romantic dinners. 
       Rated 4.6⭐ with capacity for 80 guests. Would you like to book here?"

User: "Yes, for 2 people this Saturday at 8pm"

Agent: [Checks availability]
       "The Oak is available Saturday at 8pm for 2 people. May I have your 
       contact information to complete the booking?"

User: "Sarah Johnson, +1-555-9876, sarah.j@email.com"

Agent: [Creates reservation]
       "Wonderful! Your romantic dinner at The Oak is confirmed for Saturday 
       at 8:00 PM for 2 people. Booking ID: GF-XYZ789. Enjoy your evening!"
```

**Key Features Demonstrated:**
- Multi-criteria filtering
- Tag-based search
- Contextual follow-up questions
- Personalized recommendations

---

## Flow 3: Group Booking with Constraints

**User Intent**: Large party with specific needs

```
User: "I need to book a table for 12 people for a business lunch next Tuesday"

Agent: [Calls search_venues(party_size=12, tags=["business casual", "group friendly"])]
       "For a group of 12, I recommend these venues with private rooms or 
       large table capacity: Dragon Palace (Chinese, 150 capacity, private rooms), 
       Mediterranean Grill (Greek, 110 capacity, group friendly). 
       What type of cuisine would you prefer?"

User: "Chinese sounds good. Do they have a private room?"

Agent: [Calls get_venue_details(venue_id="v003")]
       "Yes! Dragon Palace has private rooms perfect for business meetings. 
       They can accommodate up to 20 people in their private dining area. 
       What time works for your lunch?"

User: "1pm would be ideal"

Agent: [Checks availability]
       "Dragon Palace has their private room available Tuesday at 1pm for 12 people. 
       This is perfect for a business lunch. Shall I proceed with the booking?"

User: "Yes please. Michael Chen, +1-555-4567, mchen@company.com. 
      Can we get a set menu for the group?"

Agent: [Creates reservation with notes]
       "Excellent! Your business lunch at Dragon Palace is confirmed for Tuesday 
       at 1:00 PM for 12 people in their private room. Booking ID: GF-BUS456. 
       I've added a note about the set menu request - the restaurant will contact 
       you to discuss options. Confirmation sent to mchen@company.com."
```

**Key Features Demonstrated:**
- Large party handling
- Private room recommendations
- Special requests (notes field)
- Business context understanding

---

## Flow 4: Cuisine Exploration & Discovery

**User Intent**: Discover new restaurants

```
User: "What are some good Indian places?"

Agent: [Calls search_venues(cuisine="Indian")]
       "I found several excellent Indian restaurants: Saffron House (4.8⭐, 
       South Indian specialties), Curry Corner (4.4⭐, budget-friendly), 
       The Curry Place (4.2⭐, upscale). What's your preference - 
       casual or fine dining?"

User: "Something upscale"

Agent: "The Curry Place would be perfect! It's an upscale Indian restaurant 
       with a rating of 4.2⭐, known for its aromatic spices and tandoor specialties. 
       Price range: $$$. They have vegetarian and vegan options. 
       Would you like to make a reservation?"

User: "Not right now, but can you show me some French restaurants too?"

Agent: [Calls search_venues(cuisine="French")]
       "Of course! Here are some excellent French options: Le Blanc (4.9⭐, 
       fine dining, romantic), Bistro Palace (3.9⭐, casual French, Los Angeles). 
       Le Blanc is particularly special - it's a premium restaurant perfect 
       for special occasions. Would you like more details about either?"

User: "Tell me about Le Blanc"

Agent: [Gets venue details]
       "Le Blanc is our highest-rated French restaurant at 4.9⭐. It's a 
       fine dining establishment with an intimate setting (60 capacity), 
       perfect for romantic dinners or special celebrations. Price range: $$$$. 
       They're known for their seasonal tasting menus and extensive wine list. 
       Located 3.5km away. Would you like to book a table?"
```

**Key Features Demonstrated:**
- Exploratory conversation
- Comparative recommendations
- Cuisine switching
- Detailed venue information

---

## Flow 5: Modification & Cancellation

**User Intent**: Manage existing reservation

```
User: "I need to check my reservations"

Agent: [Calls get_reservations(session_id="user123")]
       "You have 2 upcoming reservations:
       1. Saffron House - Dec 25 at 7:00 PM for 4 people (GF-ABC123)
       2. The Oak - Dec 28 at 8:00 PM for 2 people (GF-XYZ789)
       
       Would you like to modify or cancel any of these?"

User: "I need to cancel the one at The Oak"

Agent: "I can help you cancel your reservation at The Oak on December 28. 
       Just to confirm - that's the booking for 2 people at 8:00 PM 
       (Booking ID: GF-XYZ789). Should I proceed with the cancellation?"

User: "Yes, cancel it"

Agent: [Calls cancel_reservation(reservation_id="res_xyz789")]
       "Your reservation at The Oak for December 28 has been cancelled. 
       Booking ID GF-XYZ789 is now cancelled. You'll receive a confirmation 
       email shortly. Is there anything else I can help you with?"

User: "Can I book a different restaurant for that same night?"

Agent: "Of course! What type of restaurant would you like for December 28 at 8pm?"
```

**Key Features Demonstrated:**
- Reservation management
- Cancellation handling
- Confirmation before action
- Seamless rebooking

---

## Flow 6: No Results / Alternative Suggestions

**User Intent**: Search with no matches

```
User: "Find me a Brazilian steakhouse in Seattle"

Agent: [Calls search_venues(cuisine="Brazilian", city="Seattle")]
       "I don't have any Brazilian restaurants in Seattle in our current listings. 
       However, I can suggest some alternatives:
       
       1. Similar cuisine: Would you like to try other South American options?
       2. Same city: Seattle has excellent steakhouses and grills
       3. Different city: We have Brazilian restaurants in other nearby cities
       
       What would you prefer?"

User: "Show me steakhouses in Seattle"

Agent: [Calls search_venues(tags=["steakhouse"], city="Seattle")]
       "Great choice! Here are some excellent steakhouses in Seattle: 
       American Grill (4.5⭐, classic steakhouse), The Tavern (4.3⭐, 
       casual dining). Both offer premium cuts and great ambiance. 
       Would you like to know more about either?"
```

**Key Features Demonstrated:**
- Graceful handling of no results
- Alternative suggestions
- Flexible search pivoting
- Helpful guidance

---

## Flow 7: Time-Sensitive Booking

**User Intent**: Urgent same-day reservation

```
User: "I need a table for 2 tonight at 8pm, ASAP"

Agent: [Calls search_venues with urgency context]
       "Let me find available restaurants for 2 people tonight at 8pm. 
       
       Available now:
       - Pizzeria Bar (Italian, 4.9⭐, 1.2km away)
       - Dragon Palace (Chinese, 4.5⭐, 0.8km away)
       - Curry Corner (Indian, 4.4⭐, 1.5km away)
       
       Dragon Palace is closest and has immediate availability. 
       Would you like to book there?"

User: "Yes, book Dragon Palace"

Agent: "Perfect! To secure your table at Dragon Palace for tonight at 8pm, 
       I need your contact information quickly."

User: "Emma Wilson, +1-555-7890, emma.w@email.com"

Agent: [Creates reservation immediately]
       "Done! Your table at Dragon Palace is confirmed for TONIGHT at 8:00 PM 
       for 2 people. Booking ID: GF-URG123. The restaurant is 0.8km away. 
       Confirmation sent to your email. See you tonight!"
```

**Key Features Demonstrated:**
- Urgency recognition
- Proximity-based recommendations
- Fast booking flow
- Immediate confirmation

---

## Flow 8: Special Occasions

**User Intent**: Celebration booking

```
User: "I want to book a restaurant for my anniversary, something really special"

Agent: "Congratulations on your anniversary! I'll find the perfect place for 
       your celebration. A few questions:
       - What's your preferred cuisine?
       - What's your budget range?
       - Any specific date and time in mind?"

User: "French food, willing to splurge, next Saturday at 7:30pm"

Agent: [Calls search_venues(cuisine="French", price_tier=4, tags=["romantic"])]
       "For your special anniversary, I highly recommend Le Blanc - our 
       highest-rated French restaurant (4.9⭐). It's a fine dining establishment 
       with an intimate, romantic atmosphere. Perfect for celebrations. 
       They offer a tasting menu with wine pairing. Price range: $$$$. 
       Shall I check availability for Saturday at 7:30pm?"

User: "Yes please, for 2 people"

Agent: [Checks availability]
       "Wonderful news! Le Blanc has availability for 2 people next Saturday 
       at 7:30 PM. To make this extra special, would you like me to add a 
       note about your anniversary? They often provide complimentary dessert 
       for celebrations."

User: "Yes, that would be great! David and Lisa Martinez, +1-555-3456, 
      david.martinez@email.com"

Agent: [Creates reservation with anniversary note]
       "Perfect! Your anniversary dinner at Le Blanc is confirmed for Saturday 
       at 7:30 PM for 2 people. Booking ID: GF-ANV789. I've noted it's your 
       anniversary celebration - the restaurant will make it special! 
       Confirmation sent. Happy anniversary!"
```

**Key Features Demonstrated:**
- Occasion recognition
- Personalized recommendations
- Special notes handling
- Celebratory tone

---

## Flow 9: Dietary Restrictions

**User Intent**: Find restaurants with specific dietary options

```
User: "I'm vegetarian and looking for a place with good vegetarian options"

Agent: [Calls search_venues(tags=["vegetarian friendly", "vegan options"])]
       "I have several great options with excellent vegetarian menus:
       
       - Saffron House (Indian, 4.8⭐) - Extensive vegetarian menu
       - Mediterranean Grill (Greek, 4.5⭐) - Many vegetarian dishes
       - The Oak (Mediterranean, 4.6⭐) - Vegetarian-friendly
       
       Indian cuisine typically has the most vegetarian options. 
       Would you like to try Saffron House?"

User: "Yes, but I'm also gluten-free. Can they accommodate that?"

Agent: [Gets venue details with dietary info]
       "Great question! Saffron House is vegetarian-friendly and can accommodate 
       gluten-free requests. I recommend mentioning your dietary restrictions 
       when you arrive, and they'll guide you through the menu. Many Indian 
       dishes are naturally gluten-free. Would you like to make a reservation?"

User: "Yes, for 3 people tomorrow at 6pm"

Agent: [Checks availability]
       "Saffron House is available tomorrow at 6pm for 3 people. 
       May I have your contact information? I'll also add a note about 
       your vegetarian and gluten-free requirements."

User: "Rachel Green, +1-555-6789, rachel.g@email.com"

Agent: [Creates reservation with dietary notes]
       "All set! Your reservation at Saffron House is confirmed for tomorrow 
       at 6:00 PM for 3 people. Booking ID: GF-VEG456. I've noted your 
       vegetarian and gluten-free requirements. The restaurant will be prepared. 
       Confirmation sent!"
```

**Key Features Demonstrated:**
- Dietary restriction handling
- Tag-based filtering
- Special notes for kitchen
- Proactive accommodation

---

## Flow 10: Multi-Turn Refinement

**User Intent**: Iterative search refinement

```
User: "Show me restaurants"

Agent: "I'd be happy to help you find a restaurant! To give you the best 
       recommendations, could you tell me:
       - What type of cuisine do you prefer?
       - How many people?
       - Any specific date/time in mind?"

User: "Asian food, 4 people"

Agent: [Calls search_venues(cuisine="Asian", party_size=4)]
       "Great! I found several Asian restaurants that can accommodate 4 people:
       - Dragon Palace (Chinese, 4.5⭐, 150 capacity)
       - Tokyo Kitchen (Japanese, 4.6⭐, 70 capacity)
       - Bangkok Orchid (Thai, 4.4⭐, 90 capacity)
       
       Do you have a preference for Chinese, Japanese, or Thai?"

User: "Japanese, but something not too expensive"

Agent: [Refines search with price filter]
       "Tokyo Kitchen is a great mid-range Japanese restaurant ($$). 
       They're known for fresh sushi and traditional dishes. Rated 4.6⭐. 
       Would this work for you?"

User: "Perfect! Do they have a quiet area? It's for a family dinner"

Agent: "Tokyo Kitchen has a modern but comfortable atmosphere. While I don't 
       have specific information about quiet areas, I can add a note to your 
       reservation requesting a quieter table. When would you like to dine?"

User: "This Friday at 7pm"

Agent: [Checks availability]
       "Tokyo Kitchen is available Friday at 7pm for 4 people. I'll request 
       a quieter table for your family dinner. May I have your contact details?"

User: "Tom Anderson, +1-555-2468, tom.a@email.com"

Agent: [Creates reservation with special request]
       "Excellent! Your family dinner at Tokyo Kitchen is confirmed for Friday 
       at 7:00 PM for 4 people. Booking ID: GF-FAM234. I've requested a quieter 
       table area. Confirmation sent to tom.a@email.com. Enjoy your meal!"
```

**Key Features Demonstrated:**
- Progressive information gathering
- Search refinement
- Special requests handling
- Family-friendly recommendations

---

## Summary of Agent Capabilities

### Natural Language Understanding
- ✅ Handles vague queries ("show me restaurants")
- ✅ Understands complex requirements ("romantic, outdoor, not expensive")
- ✅ Recognizes urgency ("ASAP", "tonight")
- ✅ Detects special occasions ("anniversary", "business lunch")

### Tool Calling Intelligence
- ✅ Decides which tools to use based on context
- ✅ Chains multiple tool calls (search → details → book)
- ✅ Validates data before calling tools
- ✅ Handles tool failures gracefully

### Conversation Management
- ✅ Maintains context across turns
- ✅ Asks clarifying questions
- ✅ Provides helpful suggestions
- ✅ Confirms before taking actions

### Personalization
- ✅ Remembers user preferences within session
- ✅ Tailors recommendations to stated needs
- ✅ Adjusts tone for occasion (casual vs. formal)
- ✅ Provides relevant follow-up suggestions

### Error Handling
- ✅ Gracefully handles no results
- ✅ Suggests alternatives
- ✅ Validates user input
- ✅ Confirms critical actions (cancellations)

---

## Testing Recommendations

### Test Scenarios to Validate:
1. ✅ Simple cuisine search
2. ✅ Multi-criteria filtering
3. ✅ Large party bookings
4. ✅ Same-day urgent reservations
5. ✅ Special occasions with notes
6. ✅ Dietary restrictions
7. ✅ Reservation modifications
8. ✅ No results handling
9. ✅ Multi-turn refinement
10. ✅ Edge cases (invalid dates, full venues)

### Metrics to Track:
- Conversation completion rate
- Average turns to booking
- Tool calling accuracy
- Customer satisfaction scores
- Booking conversion rate

---

**Document Version**: 1.0  
**Last Updated**: November 19, 2025  
**Purpose**: Demonstrate AI agent capabilities and conversation patterns
