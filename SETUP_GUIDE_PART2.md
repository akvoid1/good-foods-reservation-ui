# GoodFoods - Complete Setup Guide (Part 2)

## 🚧 Challenges Faced During Development

### Challenge 1: SQLAlchemy DateTime Default Issue
**Problem**: Using `datetime.utcnow` as default for DateTime columns caused AttributeError

**Solution**: Changed to use SQLAlchemy's `func.now()`

**Impact**: Fixed in `backend/app/database.py`

### Challenge 2: Groq Tool Calling Format
**Problem**: Groq's llama model was strict about tool parameter formats. Empty strings caused errors

**Solution**: 
- Simplified tool parameters
- Improved system prompt to guide LLM
- Added parameter validation in agent

**Impact**: 
- Modified `backend/app/agent/tools.py`
- Updated `backend/app/agent/agent.py`

### Challenge 3: Next.js Dependency Conflicts
**Problem**: React 19 incompatibility with some UI libraries

**Solution**: Used `--legacy-peer-deps` flag

**Impact**: All dependencies installed successfully

### Challenge 4: CORS Configuration
**Problem**: Frontend couldn't reach backend due to CORS restrictions

**Solution**: Added CORS middleware in FastAPI

**Impact**: Frontend can now communicate with backend

### Challenge 5: API Route Proxying
**Problem**: Next.js API routes had mock data, needed to proxy to Python backend

**Solution**: Updated all 5 API routes to forward requests

**Impact**: All routes now proxy to backend:
- `app/api/agent/message/route.ts`
- `app/api/agent/recommend/route.ts`
- `app/api/reservations/route.ts`
- `app/api/reservations/create/route.ts`
- `app/api/reservations/[id]/cancel/route.ts`

### Challenge 6: Database Seeding
**Problem**: Needed realistic restaurant data for 100 venues

**Solution**: Created intelligent seed script with cuisine-specific name generation

**Impact**: `backend/seed_data.py` generates diverse, realistic data

### Challenge 7: Tool Calling Validation
**Problem**: LLM sometimes called tools with invalid parameters

**Solution**: 
- Added parameter validation in agent
- Improved tool descriptions
- Better system prompt guidance
- Graceful error handling

**Impact**: More reliable tool calling, fewer errors
