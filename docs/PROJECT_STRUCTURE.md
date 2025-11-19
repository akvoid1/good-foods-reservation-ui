# 📁 Project Structure

## Clean & Organized File Layout

```
good-foods-reservation-ui/
├── 📄 README.md                    # Main documentation & setup guide
├── 📄 .env.example                 # Environment template
├── 📄 .env.local                   # Frontend configuration
├── 📄 package.json                 # Node.js dependencies
├── 📄 next.config.mjs              # Next.js configuration
├── 📄 tailwind.config.ts           # Tailwind CSS config
├── 📄 tsconfig.json                # TypeScript config
├── 📄 components.json              # shadcn/ui config
│
├── 📁 docs/                        # 📚 Documentation
│   ├── BUSINESS_STRATEGY.md        # Business case (40% of grade)
│   ├── CONVERSATION_FLOWS.md       # Example conversation patterns
│   ├── AGENTIC_SYSTEM_EXPLAINED.md # What makes it agentic
│   ├── SUBMISSION_CHECKLIST.md     # Requirements verification
│   ├── LLM_AGENT_TEST_RESULTS.md   # Test results & proof
│   └── PROJECT_STRUCTURE.md        # This file
│
├── 📁 tests/                       # 🧪 Test Suite
│   ├── test_llm_agent.py          # Comprehensive LLM test
│   └── test_integration.py        # Full stack integration test
│
├── 📁 app/                         # 🎨 Next.js Frontend
│   ├── layout.tsx                 # Root layout
│   ├── page.tsx                   # Home page with chat
│   ├── globals.css                # Global styles
│   ├── admin/
│   │   └── page.tsx              # Admin dashboard
│   ├── discover/
│   │   └── page.tsx              # Venue discovery
│   ├── reservations/
│   │   └── page.tsx              # User reservations
│   └── api/                      # API routes (proxy to backend)
│       ├── agent/
│       │   ├── message/route.ts
│       │   └── recommend/route.ts
│       └── reservations/
│           ├── route.ts
│           ├── create/route.ts
│           ├── admin/route.ts
│           └── [id]/cancel/route.ts
│
├── 📁 components/                  # ⚛️ React Components
│   ├── ui/                        # shadcn/ui components
│   ├── chat-pane.tsx             # Chat interface
│   ├── venue-card.tsx            # Venue display
│   ├── reservation-modal.tsx     # Booking form
│   ├── reservation-list-item.tsx
│   ├── recommendation-drawer.tsx
│   ├── admin-stats-card.tsx
│   ├── filter-bar.tsx
│   ├── map-view.tsx
│   └── theme-provider.tsx
│
├── 📁 lib/                         # 🔧 Utilities
│   ├── api.ts                     # API client functions
│   ├── session.ts                 # Session management
│   └── utils.ts                   # Utility functions
│
├── 📁 hooks/                       # 🪝 React Hooks
│   ├── use-mobile.ts
│   └── use-toast.ts
│
├── 📁 public/                      # 🖼️ Static Assets
│   ├── icon.svg
│   ├── placeholder.svg
│   └── [restaurant images]
│
└── 📁 backend/                     # 🐍 Python Backend
    ├── 📄 README.md               # Backend overview
    ├── 📄 QUICKSTART.md           # Quick setup guide
    ├── 📄 EMAIL_SETUP.md          # Email configuration
    ├── 📄 requirements.txt        # Python dependencies
    ├── 📄 .env                    # Backend configuration
    ├── 📄 .env.example            # Environment template
    ├── 📄 run.py                  # Server startup script
    ├── 📄 seed_data.py            # Database seeding (100 venues)
    ├── 📄 goodfoods.db            # SQLite database
    │
    └── 📁 app/                    # FastAPI Application
        ├── main.py                # FastAPI entry point
        ├── config.py              # Configuration settings
        ├── database.py            # SQLAlchemy models
        ├── models.py              # Pydantic models
        │
        ├── 📁 agent/              # 🤖 LLM Agent (Agentic System)
        │   ├── __init__.py
        │   ├── agent.py           # Main agent logic
        │   ├── llm.py             # LLM client (Groq)
        │   └── tools.py           # Tool definitions (4 tools)
        │
        ├── 📁 routers/            # 🛣️ API Endpoints
        │   ├── __init__.py
        │   ├── agent.py           # Agent endpoints
        │   └── reservations.py    # Reservation endpoints
        │
        └── 📁 services/           # 💼 Business Logic
            ├── __init__.py
            ├── venue_service.py   # Venue search
            ├── reservation_service.py # Booking logic
            └── email_service.py   # Email notifications
```

## Key Files Explained

### 🎯 Core Application Files

**Frontend Entry Points:**
- `app/page.tsx` - Home page with chat interface (main agentic interaction)
- `app/admin/page.tsx` - Admin dashboard with analytics
- `app/reservations/page.tsx` - User reservation management
- `app/discover/page.tsx` - Venue discovery and browsing

**Backend Entry Points:**
- `backend/run.py` - Start the FastAPI server
- `backend/app/main.py` - FastAPI application setup
- `backend/seed_data.py` - Populate database with 100 venues

### 🤖 Agentic System (The Brain)

**Core Agent Files:**
- `backend/app/agent/agent.py` - Main agent logic, conversation management
- `backend/app/agent/llm.py` - LLM client (Groq API integration)
- `backend/app/agent/tools.py` - 4 tools the agent can use:
  - `search_venues` - Find restaurants by criteria
  - `get_venue_details` - Get specific venue info
  - `check_availability` - Check booking availability
  - `create_reservation` - Make a booking

### 📚 Documentation Files

**Essential Docs (in `docs/` folder):**
- `BUSINESS_STRATEGY.md` - Complete business case (40% of grade)
- `CONVERSATION_FLOWS.md` - 10 example conversation patterns
- `AGENTIC_SYSTEM_EXPLAINED.md` - Explains what makes it agentic
- `SUBMISSION_CHECKLIST.md` - Verifies all requirements met
- `LLM_AGENT_TEST_RESULTS.md` - Proof that agentic system works

**Backend Docs:**
- `backend/README.md` - Backend overview
- `backend/QUICKSTART.md` - Quick setup guide
- `backend/EMAIL_SETUP.md` - Email configuration

### 🧪 Test Files (in `tests/` folder)

- `test_llm_agent.py` - Comprehensive test of LLM and tool calling
- `test_integration.py` - Full stack integration test

### ⚙️ Configuration Files

**Frontend:**
- `.env.local` - Frontend config (BACKEND_URL)
- `next.config.mjs` - Next.js configuration
- `tailwind.config.ts` - Tailwind CSS config
- `tsconfig.json` - TypeScript config

**Backend:**
- `backend/.env` - Backend config (LLM_API_KEY, SMTP settings)
- `backend/requirements.txt` - Python dependencies

## Architecture Layers

### Frontend Architecture
```
UI Components (React/Next.js)
    ↓
API Client (lib/api.ts)
    ↓
Next.js API Routes (app/api/)
    ↓
Backend API (FastAPI)
```

### Backend Architecture
```
API Routes (routers/)
    ↓
Services (services/)
    ↓
Database (SQLAlchemy)

API Routes (routers/)
    ↓
Agent (agent/)
    ↓
LLM (Groq API)
    ↓
Tools (tools.py)
```

### Agentic Flow
```
User Message
    ↓
Chat Component (components/chat-pane.tsx)
    ↓
Agent API (app/api/agent/message/route.ts)
    ↓
Backend Agent (backend/app/agent/agent.py)
    ↓
LLM (backend/app/agent/llm.py)
    ↓
Tool Selection & Execution (backend/app/agent/tools.py)
    ↓
Response to User
```

## File Count Summary

- **Total Files**: ~50 (clean and organized)
- **Documentation**: 6 essential files (in `docs/`)
- **Tests**: 2 comprehensive tests (in `tests/`)
- **Frontend**: ~25 files (app/, components/, lib/)
- **Backend**: ~15 files (backend/app/)
- **Config**: ~8 files (root level)

## Benefits of This Structure

### 📁 Organized
- Documentation in `docs/` folder
- Tests in `tests/` folder
- Clear separation of concerns

### 🔍 Easy to Navigate
- Logical folder structure
- Descriptive file names
- Clear hierarchy

### 🚀 Production Ready
- Clean codebase
- No duplicate files
- Well documented

### ✅ Evaluation Friendly
- All requirements easily accessible
- Clear documentation structure
- Test results readily available

## Quick Navigation

### To Start Development:
1. `backend/run.py` - Start backend
2. `npm run dev` - Start frontend
3. Open http://localhost:3000

### To Run Tests:
1. `python tests/test_llm_agent.py` - Test LLM agent
2. `python tests/test_integration.py` - Test integration

### To Review Documentation:
1. `README.md` - Main setup guide
2. `docs/BUSINESS_STRATEGY.md` - Business case
3. `docs/SUBMISSION_CHECKLIST.md` - Requirements check

### To Configure:
1. `backend/.env` - Backend settings
2. `.env.local` - Frontend settings
3. `backend/EMAIL_SETUP.md` - Email setup

---

**Clean, organized, and ready for evaluation!** ✨
