# GoodFoods Backend API

FastAPI backend for AI-powered restaurant reservation system with LLM tool calling.

## Features

- **LLM Agent**: Conversational AI with function calling (llama-3.3 or compatible)
- **Tool Calling**: Search venues, check availability, create reservations
- **Database**: SQLite (easily switchable to PostgreSQL)
- **RESTful API**: Clean endpoints for frontend integration

## Setup

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
cp .env.example .env
```

Edit `.env` and add your LLM API key:
```
LLM_API_KEY=your_api_key_here
LLM_BASE_URL=https://api.openai.com/v1
LLM_MODEL=llama-3.3-70b-versatile
```

### 3. Seed the Database

```bash
python seed_data.py
```

This will populate the database with 100 realistic restaurant venues across 10 cities.

### 4. Run the Server

```bash
python run.py
# or
uvicorn app.main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`

### 5. View Venues (Optional)

```bash
python scripts/view_venues.py 20
```

## API Endpoints

### Agent
- `POST /api/agent/message` - Send message to AI agent
- `POST /api/agent/recommend` - Get venue recommendations

### Reservations
- `POST /api/reservations/create` - Create reservation
- `GET /api/reservations?session_id=xxx` - Get user reservations
- `POST /api/reservations/{id}/cancel` - Cancel reservation

### Health
- `GET /` - API info
- `GET /health` - Health check

## Project Structure

```
backend/
├── app/
│   ├── agent/          # LLM agent with tool calling
│   ├── routers/        # API endpoints
│   ├── services/       # Business logic
│   ├── config.py       # Configuration
│   ├── database.py     # Database models
│   ├── models.py       # Pydantic models
│   └── main.py         # FastAPI app
├── requirements.txt
└── .env
```

## Database

The seed script generates 100 venues with:
- 10 different cuisines (Italian, Indian, Chinese, French, Japanese, etc.)
- 10 cities across the US
- Realistic names, ratings (3.8-5.0), capacities (40-200)
- Price tiers (1-4), tags, operating hours
- Contact info and descriptions

## Utilities

- `seed_data.py` - Populate database with 100 venues
- `scripts/view_venues.py` - View venues in database
- `scripts/add_more_venues.py` - Add premium/special venues

## Next Steps

1. ✅ Database populated with 100 venues
2. Add your LLM API key to `.env`
3. Test the agent with different queries
4. Connect Next.js frontend to this backend
