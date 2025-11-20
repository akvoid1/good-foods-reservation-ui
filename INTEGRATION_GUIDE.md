# Frontend-Backend Integration Guide

## Architecture

```
Next.js Frontend (Port 3000)
    ↓ API Routes (/app/api/*)
    ↓ Proxy Requests
Python Backend (Port 8000)
    ↓ LLM Agent + Tools
    ↓ Database (SQLite)
```

## What Was Changed

### 1. Next.js API Routes (Proxy Layer)
All API routes now forward requests to Python backend:

- ✅ `/app/api/agent/message/route.ts` → `http://localhost:8000/api/agent/message`
- ✅ `/app/api/agent/recommend/route.ts` → `http://localhost:8000/api/agent/recommend`
- ✅ `/app/api/reservations/route.ts` → `http://localhost:8000/api/reservations`
- ✅ `/app/api/reservations/create/route.ts` → `http://localhost:8000/api/reservations/create`
- ✅ `/app/api/reservations/[id]/cancel/route.ts` → `http://localhost:8000/api/reservations/{id}/cancel`

### 2. Environment Variables
Created `.env.local`:
```env
BACKEND_URL=http://localhost:8000
```

### 3. Data Flow

**Chat Flow:**
1. User types message in chat → `components/chat-pane.tsx`
2. Frontend calls → `POST /api/agent/message`
3. Next.js proxies → `POST http://localhost:8000/api/agent/message`
4. Python backend:
   - LLM processes message
   - Calls tools (search_venues, etc.)
   - Returns response with venues
5. Frontend displays response + venue cards

**Reservation Flow:**
1. User fills reservation form → `components/reservation-modal.tsx`
2. Frontend calls → `POST /api/reservations/create`
3. Next.js proxies → `POST http://localhost:8000/api/reservations/create`
4. Python backend:
   - Validates data
   - Saves to database
   - Returns booking confirmation
5. Frontend shows success message

## Running the Full Stack

### Terminal 1: Python Backend
```bash
cd backend
python run.py
```
Server runs on: http://localhost:8000

### Terminal 2: Next.js Frontend
```bash
npm run dev
# or
pnpm dev
```
Server runs on: http://localhost:3000

## Testing the Integration

### 1. Health Check
```bash
# Backend
curl http://localhost:8000/health

# Frontend (should proxy to backend)
curl http://localhost:3000/api/agent/recommend -X POST \
  -H "Content-Type: application/json" \
  -d '{"cuisine": "Italian"}'
```

### 2. Test Chat
1. Open http://localhost:3000
2. Type in chat: "Find me Italian restaurants"
3. Should see real venues from database
4. Check backend logs for LLM calls

### 3. Test Reservation
1. Click on a venue card
2. Fill out reservation form
3. Submit
4. Check backend database: `python backend/scripts/view_venues.py`

## Troubleshooting

### Backend not responding
```bash
# Check if backend is running
curl http://localhost:8000/health

# Restart backend
cd backend
python run.py
```

### Frontend can't reach backend
- Check `.env.local` has `BACKEND_URL=http://localhost:8000`
- Restart Next.js dev server: `npm run dev`
- Check CORS is enabled in backend (already configured)

### LLM errors
- Verify `backend/.env` has valid `LLM_API_KEY`
- Check Groq API quota: https://console.groq.com
- Try different model in `backend/.env`: `LLM_MODEL=llama-3.1-70b-versatile`

### Database empty
```bash
cd backend
python seed_data.py
```

## API Endpoints Reference

### Agent Endpoints
- `POST /api/agent/message` - Chat with AI agent
  ```json
  {
    "session_id": "user123",
    "message": "Find Italian restaurants"
  }
  ```

- `POST /api/agent/recommend` - Get recommendations
  ```json
  {
    "cuisine": "Italian",
    "city": "New York"
  }
  ```

### Reservation Endpoints
- `POST /api/reservations/create` - Create booking
  ```json
  {
    "venue_id": "v001",
    "datetime": "2024-12-25T19:00:00",
    "party_size": 4,
    "contact": {
      "name": "John Doe",
      "phone": "+1-555-0123",
      "email": "john@example.com"
    }
  }
  ```

- `GET /api/reservations?session_id=xxx` - List bookings
- `POST /api/reservations/{id}/cancel` - Cancel booking

## Next Steps

1. ✅ Backend running with LLM
2. ✅ Frontend proxying to backend
3. 🔄 Test full user flow
4. 📝 Write business strategy document
5. 🎥 Record demo video
6. 📚 Polish documentation

## Development Tips

- Backend auto-reloads on code changes (uvicorn --reload)
- Frontend auto-reloads on code changes (Next.js dev)
- Check backend logs for LLM tool calls
- Use browser DevTools Network tab to debug API calls
- Backend API docs: http://localhost:8000/docs (FastAPI auto-generated)
