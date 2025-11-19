# Quick Start Guide

Get the GoodFoods backend running in 5 minutes!

## Step 1: Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

## Step 2: Configure Environment

```bash
cp .env.example .env
```

Edit `.env` and add your LLM API key:

```env
LLM_API_KEY=your_groq_or_openai_key_here
LLM_BASE_URL=https://api.groq.com/openai/v1
LLM_MODEL=llama-3.3-70b-versatile
```

**LLM Provider Options:**

- **Groq** (Recommended - Fast & Free): 
  - Get key: https://console.groq.com/keys
  - Base URL: `https://api.groq.com/openai/v1`
  - Model: `llama-3.3-70b-versatile`

- **OpenAI**:
  - Get key: https://platform.openai.com/api-keys
  - Base URL: `https://api.openai.com/v1`
  - Model: `gpt-4o-mini` or `gpt-3.5-turbo`

- **Together AI**:
  - Get key: https://api.together.xyz/settings/api-keys
  - Base URL: `https://api.together.xyz/v1`
  - Model: `meta-llama/Llama-3.3-70B-Instruct-Turbo`

## Step 3: Seed Database

```bash
python seed_data.py
```

Expected output:
```
✅ Successfully seeded 100 venues!
📊 Venue Distribution:
  Italian: 12
  Indian: 11
  Chinese: 10
  ...
```

## Step 4: Test Setup

```bash
python test_setup.py
```

This verifies:
- ✅ Database connection
- ✅ Venue search works
- ✅ Services are functional

## Step 5: Run Server

```bash
python run.py
```

Server will start at: `http://localhost:8000`

## Step 6: Test API

Open browser to:
- Health check: http://localhost:8000/health
- API docs: http://localhost:8000/docs

Or test with curl:

```bash
# Health check
curl http://localhost:8000/health

# Get recommendations
curl -X POST http://localhost:8000/api/agent/recommend \
  -H "Content-Type: application/json" \
  -d '{"cuisine": "Italian", "city": "New York"}'

# Chat with agent
curl -X POST http://localhost:8000/api/agent/message \
  -H "Content-Type: application/json" \
  -d '{"session_id": "test123", "message": "Find me a romantic Italian restaurant"}'
```

## Troubleshooting

**No venues found?**
```bash
python seed_data.py
```

**Database locked?**
```bash
rm goodfoods.db
python seed_data.py
```

**LLM errors?**
- Check your API key in `.env`
- Verify the base URL matches your provider
- Check API quota/credits

**Port 8000 in use?**
```bash
# Change port in run.py or:
uvicorn app.main:app --port 8001
```

## Next Steps

1. ✅ Backend running
2. Connect Next.js frontend (update API URLs)
3. Test conversation flows
4. Deploy to production

## Useful Commands

```bash
# View venues in database
python scripts/view_venues.py 20

# Add premium venues
python scripts/add_more_venues.py

# Run with auto-reload
python run.py

# Run tests
python test_setup.py
```

## Need Help?

Check the main README.md for detailed documentation.
