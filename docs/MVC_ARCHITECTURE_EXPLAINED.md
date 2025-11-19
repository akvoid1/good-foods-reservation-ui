# 🏗️ MVC Architecture Explained

## What is MVC?

**MVC (Model-View-Controller)** is a software design pattern that separates an application into three interconnected components:

### 1. Model (Data Layer)
- Manages data and business logic
- Interacts with the database
- Defines data structures
- Independent of user interface

### 2. View (Presentation Layer)
- Displays data to users
- Handles UI rendering
- Formats responses
- No business logic

### 3. Controller (Logic Layer)
- Handles user input
- Processes requests
- Coordinates Model and View
- Contains application logic

## MVC in This Project

### Frontend MVC (Next.js)

```
┌─────────────────────────────────────────┐
│           USER INTERACTION              │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│  VIEW (Components)                      │
│  - chat-pane.tsx                        │
│  - venue-card.tsx                       │
│  - reservation-modal.tsx                │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│  CONTROLLER (App Router)                │
│  - app/page.tsx                         │
│  - app/api/agent/route.ts               │
│  - app/admin/page.tsx                   │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│  MODEL (Services)                       │
│  - services/api-client.ts               │
│  - services/agent-service.ts            │
│  - services/venue-service.ts            │
└──────────────┬──────────────────────────┘
               │
               ▼
         BACKEND API
```

### Backend MVC (Python/FastAPI)

```
         HTTP REQUEST
               │
               ▼
┌─────────────────────────────────────────┐
│  CONTROLLER (controllers/)              │
│  - agent_controller.py                  │
│  - venue_controller.py                  │
│  - reservation_controller.py            │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│  SERVICE (services/)                    │
│  - venue_service.py                     │
│  - reservation_service.py               │
│  - email_service.py                     │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│  MODEL (models/)                        │
│  - venue.py (SQLAlchemy)                │
│  - reservation.py                       │
│  - database.py                          │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│  VIEW (views/)                          │
│  - venue_view.py                        │
│  - reservation_view.py                  │
│  - agent_view.py                        │
└──────────────┬──────────────────────────┘
               │
               ▼
         HTTP RESPONSE
```

## Example: Venue Search Flow

### Frontend Flow

**1. User Types in Chat**
```typescript
// VIEW: components/chat-pane.tsx
<input onChange={handleMessage} />
```

**2. Controller Handles Input**
```typescript
// CONTROLLER: app/api/agent/message/route.ts
export async function POST(request: Request) {
  const { message } = await request.json()
  
  // Call service
  const response = await agentService.sendMessage(message)
  
  return Response.json(response)
}
```

**3. Service Makes API Call**
```typescript
// MODEL: services/agent-service.ts
export const agentService = {
  async sendMessage(message: string) {
    const response = await fetch('/api/agent/message', {
      method: 'POST',
      body: JSON.stringify({ message })
    })
    return response.json()
  }
}
```

### Backend Flow

**1. Controller Receives Request**
```python
# CONTROLLER: controllers/agent_controller.py
@router.post("/message")
async def handle_message(request: MessageRequest):
    # Call service
    response = await agent_service.process_message(
        request.message,
        request.session_id
    )
    
    # Format with view
    return agent_view.format_response(response)
```

**2. Service Processes Logic**
```python
# SERVICE: services/agent_service.py
async def process_message(message: str, session_id: str):
    # Use LLM agent
    result = await agent.process(message, session_id)
    
    # If search needed, use venue service
    if result.tool == "search_venues":
        venues = venue_service.search(result.params)
        return {"venues": venues}
    
    return result
```

**3. Model Queries Database**
```python
# MODEL: models/venue.py
class Venue(Base):
    __tablename__ = "venues"
    
    id = Column(String, primary_key=True)
    name = Column(String)
    cuisine = Column(String)
    city = Column(String)
    
    @classmethod
    def search(cls, db, cuisine=None, city=None):
        query = db.query(cls)
        if cuisine:
            query = query.filter(cls.cuisine == cuisine)
        if city:
            query = query.filter(cls.city == city)
        return query.all()
```

**4. View Formats Response**
```python
# VIEW: views/venue_view.py
def format_venue_list(venues):
    return {
        "venues": [
            {
                "id": v.id,
                "name": v.name,
                "cuisine": v.cuisine,
                "city": v.city,
                "rating": v.rating,
                "price_tier": v.price_tier
            }
            for v in venues
        ],
        "count": len(venues)
    }
```

## Benefits of MVC

### 1. Separation of Concerns
```
❌ Without MVC:
- Everything in one file
- Hard to maintain
- Difficult to test

✅ With MVC:
- Clear responsibilities
- Easy to maintain
- Simple to test
```

### 2. Reusability
```python
# Service can be used by multiple controllers
venue_service.search()  # Used by agent controller
venue_service.search()  # Used by venue controller
venue_service.search()  # Used by admin controller
```

### 3. Testability
```python
# Test model independently
def test_venue_model():
    venue = Venue(name="Test", cuisine="Italian")
    assert venue.name == "Test"

# Test service independently
def test_venue_service():
    venues = venue_service.search(cuisine="Italian")
    assert len(venues) > 0

# Test controller independently
def test_venue_controller():
    response = client.get("/venues?cuisine=Italian")
    assert response.status_code == 200
```

### 4. Scalability
```
Easy to add new features:
- New model → Add new file in models/
- New endpoint → Add new controller
- New business logic → Add new service
- New response format → Add new view
```

## MVC vs Current Structure

### Before (Mixed)
```
backend/app/
├── main.py              # Everything mixed
├── database.py          # Models + DB connection
├── models.py            # Pydantic + SQLAlchemy mixed
├── routers/             # Controllers + Views mixed
│   ├── agent.py
│   └── reservations.py
└── services/            # Business logic
    ├── venue_service.py
    └── reservation_service.py
```

### After (MVC)
```
backend-api/
├── models/              # MODEL: Data layer
│   ├── database.py      # DB connection
│   ├── venue.py         # Venue model
│   └── reservation.py   # Reservation model
│
├── views/               # VIEW: Response formatting
│   ├── venue_view.py
│   ├── reservation_view.py
│   └── agent_view.py
│
├── controllers/         # CONTROLLER: Request handling
│   ├── venue_controller.py
│   ├── reservation_controller.py
│   └── agent_controller.py
│
├── services/            # Business logic (separate)
│   ├── venue_service.py
│   ├── reservation_service.py
│   └── email_service.py
│
└── main.py              # App entry point
```

## Key Principles

### 1. Single Responsibility
Each component has ONE job:
- Model: Data
- View: Presentation
- Controller: Logic

### 2. Loose Coupling
Components are independent:
- Change model without affecting view
- Change view without affecting controller
- Change controller without affecting model

### 3. High Cohesion
Related code stays together:
- All venue logic in venue files
- All reservation logic in reservation files
- All agent logic in agent files

## Common Patterns

### Pattern 1: CRUD Operations
```python
# MODEL: Define data structure
class Venue(Base):
    id = Column(String, primary_key=True)
    name = Column(String)

# SERVICE: Business logic
def create_venue(data):
    venue = Venue(**data)
    db.add(venue)
    db.commit()
    return venue

# CONTROLLER: Handle request
@router.post("/venues")
def create_venue_endpoint(data: VenueCreate):
    venue = venue_service.create_venue(data)
    return venue_view.format_venue(venue)

# VIEW: Format response
def format_venue(venue):
    return {
        "id": venue.id,
        "name": venue.name
    }
```

### Pattern 2: Search & Filter
```python
# MODEL: Query methods
class Venue(Base):
    @classmethod
    def search(cls, db, **filters):
        query = db.query(cls)
        for key, value in filters.items():
            query = query.filter(getattr(cls, key) == value)
        return query.all()

# SERVICE: Business logic
def search_venues(cuisine=None, city=None):
    filters = {}
    if cuisine:
        filters['cuisine'] = cuisine
    if city:
        filters['city'] = city
    return Venue.search(db, **filters)

# CONTROLLER: Handle request
@router.get("/venues")
def search_venues_endpoint(cuisine: str = None, city: str = None):
    venues = venue_service.search_venues(cuisine, city)
    return venue_view.format_venue_list(venues)

# VIEW: Format response
def format_venue_list(venues):
    return {
        "venues": [format_venue(v) for v in venues],
        "count": len(venues)
    }
```

## Summary

**MVC provides:**
- ✅ Clear structure
- ✅ Easy maintenance
- ✅ Better testing
- ✅ Team collaboration
- ✅ Scalability

**In this project:**
- Frontend: Next.js with MVC pattern
- Backend: Python/FastAPI with MVC pattern
- Clear separation of concerns
- Professional architecture

---

**MVC makes code better!** 🏗️
