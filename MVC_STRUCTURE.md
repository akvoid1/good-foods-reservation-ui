# 🏗️ MVC Architecture - Complete Reorganization

## New Project Structure

```
good-foods-reservation-ui/
│
├── 📁 frontend/                    # FRONTEND (Next.js MVC)
│   ├── 📁 src/
│   │   ├── 📁 app/                # Next.js App Router (Controllers)
│   │   │   ├── layout.tsx
│   │   │   ├── page.tsx
│   │   │   ├── admin/
│   │   │   ├── discover/
│   │   │   ├── reservations/
│   │   │   └── api/              # API Routes (Controllers)
│   │   │
│   │   ├── 📁 components/         # VIEW Components (Reusable UI)
│   │   │   ├── ui/               # Base UI components
│   │   │   ├── chat-pane.tsx
│   │   │   ├── venue-card.tsx
│   │   │   ├── reservation-modal.tsx
│   │   │   └── ...
│   │   │
│   │   ├── 📁 views/              # VIEW Pages (Page-specific components)
│   │   │   ├── home/
│   │   │   ├── admin/
│   │   │   ├── discover/
│   │   │   └── reservations/
│   │   │
│   │   ├── 📁 services/           # API Services (Data Layer)
│   │   │   ├── api-client.ts     # Base API client
│   │   │   ├── agent-service.ts  # Agent API calls
│   │   │   ├── venue-service.ts  # Venue API calls
│   │   │   └── reservation-service.ts
│   │   │
│   │   ├── 📁 hooks/              # Custom React Hooks
│   │   │   ├── use-mobile.ts
│   │   │   ├── use-toast.ts
│   │   │   └── use-session.ts
│   │   │
│   │   ├── 📁 utils/              # Utility Functions
│   │   │   ├── cn.ts             # Class name utility
│   │   │   ├── date.ts           # Date formatting
│   │   │   └── session.ts        # Session management
│   │   │
│   │   └── 📁 styles/             # Global Styles
│   │       └── globals.css
│   │
│   ├── 📁 public/                 # Static Assets
│   │   ├── images/
│   │   └── icons/
│   │
│   ├── package.json
│   ├── next.config.mjs
│   ├── tailwind.config.ts
│   ├── tsconfig.json
│   └── .env.local
│
├── 📁 backend-api/                # BACKEND (Python MVC)
│   │
│   ├── 📁 models/                 # MODEL Layer (Data Models)
│   │   ├── __init__.py
│   │   ├── venue.py              # Venue model
│   │   ├── reservation.py        # Reservation model
│   │   └── database.py           # Database connection
│   │
│   ├── 📁 views/                  # VIEW Layer (Response Formatters)
│   │   ├── __init__.py
│   │   ├── venue_view.py         # Venue response formatting
│   │   ├── reservation_view.py   # Reservation response formatting
│   │   └── agent_view.py         # Agent response formatting
│   │
│   ├── 📁 controllers/            # CONTROLLER Layer (Request Handlers)
│   │   ├── __init__.py
│   │   ├── venue_controller.py   # Venue endpoints
│   │   ├── reservation_controller.py
│   │   └── agent_controller.py   # Agent endpoints
│   │
│   ├── 📁 services/               # Business Logic Layer
│   │   ├── __init__.py
│   │   ├── venue_service.py      # Venue business logic
│   │   ├── reservation_service.py
│   │   ├── email_service.py
│   │   └── notification_service.py
│   │
│   ├── 📁 agent/                  # AI Agent System
│   │   ├── __init__.py
│   │   ├── agent.py              # Main agent logic
│   │   ├── llm.py                # LLM client
│   │   └── tools.py              # Tool definitions
│   │
│   ├── 📁 config/                 # Configuration
│   │   ├── __init__.py
│   │   ├── settings.py           # App settings
│   │   └── database.py           # DB configuration
│   │
│   ├── 📁 utils/                  # Utility Functions
│   │   ├── __init__.py
│   │   ├── validators.py         # Input validation
│   │   └── helpers.py            # Helper functions
│   │
│   ├── main.py                    # FastAPI app entry
│   ├── run.py                     # Server startup
│   ├── seed_data.py               # Database seeding
│   ├── requirements.txt
│   └── .env
│
├── 📁 docs/                       # Documentation
│   ├── BUSINESS_STRATEGY.md
│   ├── CONVERSATION_FLOWS.md
│   ├── AGENTIC_SYSTEM_EXPLAINED.md
│   ├── SUBMISSION_CHECKLIST.md
│   ├── LLM_AGENT_TEST_RESULTS.md
│   └── MVC_ARCHITECTURE.md
│
├── 📁 tests/                      # Test Suite
│   ├── test_llm_agent.py
│   └── test_integration.py
│
├── README.md
└── QUICK_START.md
```

## MVC Pattern Explanation

### FRONTEND (Next.js MVC)

#### Model (Data Layer)
- **Location**: `frontend/src/services/`
- **Purpose**: API communication, data fetching
- **Files**:
  - `api-client.ts` - Base HTTP client
  - `agent-service.ts` - Agent API calls
  - `venue-service.ts` - Venue data operations
  - `reservation-service.ts` - Reservation operations

#### View (Presentation Layer)
- **Location**: `frontend/src/components/` + `frontend/src/views/`
- **Purpose**: UI components, visual presentation
- **Components**:
  - Reusable UI components (buttons, cards, modals)
  - Page-specific view components
  - Layout components

#### Controller (Logic Layer)
- **Location**: `frontend/src/app/`
- **Purpose**: Route handling, business logic, state management
- **Files**:
  - Page components (page.tsx)
  - API routes (app/api/)
  - Layout components (layout.tsx)

### BACKEND (Python MVC)

#### Model (Data Layer)
- **Location**: `backend-api/models/`
- **Purpose**: Database models, data structures
- **Files**:
  - `venue.py` - Venue SQLAlchemy model
  - `reservation.py` - Reservation model
  - `database.py` - Database connection & session

#### View (Response Layer)
- **Location**: `backend-api/views/`
- **Purpose**: Format responses, serialize data
- **Files**:
  - `venue_view.py` - Format venue responses
  - `reservation_view.py` - Format reservation responses
  - `agent_view.py` - Format agent responses

#### Controller (Request Layer)
- **Location**: `backend-api/controllers/`
- **Purpose**: Handle HTTP requests, route logic
- **Files**:
  - `venue_controller.py` - Venue endpoints
  - `reservation_controller.py` - Reservation endpoints
  - `agent_controller.py` - Agent endpoints

#### Services (Business Logic)
- **Location**: `backend-api/services/`
- **Purpose**: Core business logic, separate from HTTP
- **Files**:
  - `venue_service.py` - Venue search logic
  - `reservation_service.py` - Booking logic
  - `email_service.py` - Email notifications

## Data Flow

### Frontend Request Flow
```
User Interaction
    ↓
View Component (components/)
    ↓
Controller (app/page.tsx or app/api/)
    ↓
Service (services/api-client.ts)
    ↓
Backend API
```

### Backend Request Flow
```
HTTP Request
    ↓
Controller (controllers/venue_controller.py)
    ↓
Service (services/venue_service.py)
    ↓
Model (models/venue.py)
    ↓
Database
    ↓
View (views/venue_view.py)
    ↓
HTTP Response
```

### Agent Flow
```
User Message
    ↓
Frontend Controller (app/api/agent/message/route.ts)
    ↓
Backend Controller (controllers/agent_controller.py)
    ↓
Agent Service (agent/agent.py)
    ↓
LLM (agent/llm.py)
    ↓
Tools (agent/tools.py)
    ↓
Business Services (services/)
    ↓
Models (models/)
    ↓
View Formatter (views/agent_view.py)
    ↓
Response
```

## File Mapping (Old → New)

### Frontend Files

**Old Structure → New Structure**

```
app/                          → frontend/src/app/
components/                   → frontend/src/components/
lib/api.ts                   → frontend/src/services/api-client.ts
lib/session.ts               → frontend/src/utils/session.ts
lib/utils.ts                 → frontend/src/utils/cn.ts
hooks/                       → frontend/src/hooks/
public/                      → frontend/public/
styles/globals.css           → frontend/src/styles/globals.css
package.json                 → frontend/package.json
next.config.mjs              → frontend/next.config.mjs
tailwind.config.ts           → frontend/tailwind.config.ts
tsconfig.json                → frontend/tsconfig.json
.env.local                   → frontend/.env.local
```

### Backend Files

**Old Structure → New Structure**

```
backend/app/database.py      → backend-api/models/database.py
backend/app/models.py        → backend-api/models/ (split into files)
backend/app/routers/         → backend-api/controllers/
backend/app/services/        → backend-api/services/
backend/app/agent/           → backend-api/agent/
backend/app/config.py        → backend-api/config/settings.py
backend/app/main.py          → backend-api/main.py
backend/run.py               → backend-api/run.py
backend/seed_data.py         → backend-api/seed_data.py
backend/requirements.txt     → backend-api/requirements.txt
backend/.env                 → backend-api/.env
```

## Benefits of MVC Structure

### 1. Separation of Concerns
- **Models**: Handle data and database
- **Views**: Handle presentation and formatting
- **Controllers**: Handle request/response logic

### 2. Maintainability
- Easy to find and modify code
- Clear responsibility for each file
- Reduced code duplication

### 3. Scalability
- Add new features without affecting existing code
- Easy to add new models, views, or controllers
- Clear structure for team collaboration

### 4. Testability
- Test models independently
- Test controllers without views
- Mock services for unit tests

### 5. Reusability
- Services can be used by multiple controllers
- Views can format data for different endpoints
- Models are shared across the application

## Implementation Steps

### Phase 1: Backend Reorganization
1. ✅ Create new directory structure
2. ⏳ Split models into separate files
3. ⏳ Create view formatters
4. ⏳ Rename routers to controllers
5. ⏳ Update imports and references
6. ⏳ Test backend functionality

### Phase 2: Frontend Reorganization
1. ✅ Create new directory structure
2. ⏳ Move components to src/components
3. ⏳ Create service layer (API clients)
4. ⏳ Move utilities to src/utils
5. ⏳ Update imports and references
6. ⏳ Test frontend functionality

### Phase 3: Integration & Testing
1. ⏳ Update API endpoints
2. ⏳ Test full stack integration
3. ⏳ Update documentation
4. ⏳ Verify all features work

## Next Steps

Run the reorganization script:
```bash
python reorganize_mvc.py
```

This will:
1. Create all necessary directories
2. Move files to new locations
3. Update all imports
4. Preserve all functionality
5. Generate migration report

---

**Ready to implement MVC architecture!** 🏗️
