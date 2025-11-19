# 🤖 The Agentic Part of Your Website

## What is "Agentic"?

An **agentic system** is one where an AI agent:
1. **Understands** user intent from natural language
2. **Decides** which actions to take (not hardcoded)
3. **Uses tools** to accomplish tasks
4. **Responds** intelligently based on results

---

## Your Agentic Components

### 1. The Chat Interface (Frontend)
**Location**: Home page at http://localhost:3000

**What it does:**
- User types natural language queries
- Sends to AI agent
- Displays intelligent responses
- Shows venue recommendations

**Example:**
```
User: "Find me Italian restaurants in New York"
↓
Agent processes and responds with venues
```

---

### 2. The AI Agent (Backend Core)
**Location**: `backend/app/agent/agent.py`

**This is the BRAIN of your agentic system!**

**What it does:**
```python
class Agent:
    async def process_message(self, session_id, message, context):
        # 1. Sends message to LLM
        # 2. LLM decides which tools to use
        # 3. Executes tools
        # 4. Returns intelligent response
```

**Key Features:**
- ✅ **Not hardcoded** - LLM makes decisions
- ✅ **Tool calling** - Uses tools dynamically
- ✅ **Context aware** - Remembers conversation
- ✅ **Intelligent** - Understands intent

---

### 3. The LLM (Language Model)
**Location**: `backend/app/agent/llm.py`

**What it does:**
- Powered by **llama-3.3-70b** via Groq API
- Understands natural language
- Decides which tools to call
- Generates human-like responses

**Example Decision Making:**
```
User: "Find me Italian restaurants"
↓
LLM thinks: "User wants to search for restaurants"
↓
LLM decides: "I should call search_venues tool"
↓
LLM calls: search_venues(cuisine="Italian")
```

---

### 4. The Tools (Agent's Capabilities)
**Location**: `backend/app/agent/tools.py`

**These are the ACTIONS your agent can take:**

#### Tool 1: search_venues
```python
{
  "name": "search_venues",
  "description": "Search for restaurants by cuisine, location, etc.",
  "parameters": {
    "cuisine": "Type of cuisine (Italian, Indian, etc.)",
    "city": "City or location"
  }
}
```

**What it does:**
- Searches database for matching restaurants
- Filters by cuisine, city, tags
- Returns list of venues

#### Tool 2: get_venue_details
```python
{
  "name": "get_venue_details",
  "description": "Get detailed information about a specific restaurant"
}
```

**What it does:**
- Gets full details of a specific venue
- Returns capacity, hours, contact info

#### Tool 3: check_availability
```python
{
  "name": "check_availability",
  "description": "Check if restaurant has availability"
}
```

**What it does:**
- Checks if venue can accommodate party size
- Verifies capacity

#### Tool 4: create_reservation
```python
{
  "name": "create_reservation",
  "description": "Create a reservation at a restaurant"
}
```

**What it does:**
- Books a table
- Saves to database
- Sends confirmation email

---

## How the Agentic System Works

### Example Flow:

```
┌─────────────────────────────────────────────────────────────┐
│ USER: "Find me a romantic Italian restaurant for 2 people" │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ CHAT INTERFACE (Frontend)                                   │
│ - Captures user message                                     │
│ - Sends to backend API                                      │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ AGENT (Backend)                                             │
│ - Receives message                                          │
│ - Sends to LLM with tool definitions                        │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ LLM (llama-3.3-70b)                                         │
│ - Understands: User wants Italian, romantic, for 2         │
│ - Decides: Should call search_venues tool                  │
│ - Returns: Tool call with parameters                        │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ TOOL EXECUTION (Agent)                                      │
│ - Calls: search_venues(cuisine="Italian", tags=["romantic"])│
│ - Searches database                                         │
│ - Returns: List of matching venues                          │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ RESPONSE FORMATTING (Agent)                                 │
│ - Formats venues into response                              │
│ - Adds suggested replies                                    │
│ - Returns to frontend                                       │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ DISPLAY (Frontend)                                          │
│ - Shows agent response                                      │
│ - Displays venue cards                                      │
│ - User can click to book                                    │
└─────────────────────────────────────────────────────────────┘
```

---

## Why This is "Agentic"

### ❌ NOT Agentic (Traditional):
```javascript
if (message.includes("Italian")) {
  return searchItalianRestaurants();
}
if (message.includes("French")) {
  return searchFrenchRestaurants();
}
// Hardcoded rules for every case
```

### ✅ Agentic (Your System):
```python
# LLM reads message
# LLM understands intent
# LLM decides which tool to use
# LLM calls tool with appropriate parameters
# LLM formats response naturally

# NO HARDCODED RULES!
# Agent adapts to ANY query
```

---

## Key Agentic Features in Your System

### 1. Intent Recognition ✅
**Not hardcoded** - LLM understands what user wants

**Examples:**
- "Find me Italian restaurants" → search_venues
- "Show me romantic places" → search_venues with tags
- "I need a table for 8" → search_venues with party_size

### 2. Tool Selection ✅
**LLM decides** which tool to use based on context

**Examples:**
- Search query → search_venues
- Specific venue question → get_venue_details
- Booking request → create_reservation

### 3. Parameter Extraction ✅
**LLM extracts** relevant information from natural language

**Examples:**
- "Italian in New York" → cuisine="Italian", city="New York"
- "Romantic place for 2" → tags=["romantic"], party_size=2
- "Tonight at 8pm" → datetime="2024-11-18T20:00:00"

### 4. Natural Responses ✅
**LLM generates** human-like responses

**Examples:**
- "I found some great Italian options for you..."
- "Would you like to know more about any of these?"
- "Let me search for romantic restaurants..."

---

## Where to See the Agentic System

### 1. Chat Interface
**Location**: http://localhost:3000 (home page)

**Try these queries:**
- "Find me Italian restaurants"
- "Show me romantic places"
- "I need a table for 8 people"
- "What are some good Indian restaurants?"

### 2. Backend Logs
**Location**: Backend terminal

**Watch for:**
```
INFO: POST /api/agent/message HTTP/1.1 200 OK
```

You'll see:
- LLM API calls
- Tool execution
- Search results

### 3. Code Files

**Agent Brain:**
- `backend/app/agent/agent.py` - Main agent logic

**LLM Client:**
- `backend/app/agent/llm.py` - LLM integration

**Tool Definitions:**
- `backend/app/agent/tools.py` - 4 tools

**Tool Implementations:**
- `backend/app/services/venue_service.py` - Search logic
- `backend/app/services/reservation_service.py` - Booking logic

---

## What Makes Your Agent Special

### 1. True AI Decision Making
- ✅ LLM decides actions (not hardcoded)
- ✅ Adapts to any query
- ✅ Understands context

### 2. Tool Calling Architecture
- ✅ 4 tools available
- ✅ LLM chooses which to use
- ✅ Dynamic parameter extraction

### 3. Real Database Integration
- ✅ 100 venues
- ✅ Live search
- ✅ Actual bookings

### 4. Production Quality
- ✅ Error handling
- ✅ Async operations
- ✅ Clean architecture

---

## Demo Script for Agentic Features

### Show 1: Natural Language Understanding
```
Type: "Find me Italian restaurants"
Show: Agent understands and searches
```

### Show 2: Tool Calling
```
Type: "Show me romantic places"
Show: Backend logs - tool being called
```

### Show 3: Complex Query
```
Type: "I need a quiet place for business lunch for 6 people"
Show: Agent extracts multiple parameters
```

### Show 4: Multi-turn Conversation
```
Turn 1: "Find me a restaurant"
Turn 2: "Make it Italian"
Show: Agent remembers context
```

---

## Summary

### Your Agentic System Consists Of:

1. **Chat Interface** (Frontend)
   - Where users interact
   - Natural language input

2. **AI Agent** (Backend)
   - Brain of the system
   - Processes messages
   - Executes tools

3. **LLM** (llama-3.3-70b)
   - Understands intent
   - Decides actions
   - Generates responses

4. **Tools** (4 capabilities)
   - search_venues
   - get_venue_details
   - check_availability
   - create_reservation

5. **Services** (Tool implementations)
   - Database search
   - Booking logic
   - Email sending

### What Makes It Agentic:

✅ **Autonomous** - Makes own decisions
✅ **Intelligent** - Understands natural language
✅ **Tool-using** - Can perform actions
✅ **Adaptive** - Handles any query
✅ **Not hardcoded** - LLM decides everything

**Your entire chat-based reservation system is the agentic part!** 🤖
