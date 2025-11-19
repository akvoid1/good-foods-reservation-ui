# 🚀 Quick Start Guide

## Get Running in 3 Minutes

### Step 1: Backend Setup (1 min)
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your Groq API key
python seed_data.py
python run.py
```
✅ Backend running on http://localhost:8000

### Step 2: Frontend Setup (1 min)
```bash
# In new terminal, from project root
npm install --legacy-peer-deps
npm run dev
```
✅ Frontend running on http://localhost:3000

### Step 3: Test It (1 min)
```bash
# In new terminal
python tests/test_llm_agent.py
```
✅ Tests passing

## Try It Out

1. Open http://localhost:3000
2. Type: **"Find me Italian restaurants in New York"**
3. See AI agent search and recommend venues
4. Click a venue to make a reservation

## Project Structure

```
📁 good-foods-reservation-ui/
├── 📄 README.md              # Full documentation
├── 📁 docs/                  # All documentation (6 files)
├── 📁 tests/                 # Test suite (2 files)
├── 📁 app/                   # Next.js frontend
├── 📁 components/            # React components
└── 📁 backend/               # Python FastAPI backend
    └── app/
        ├── agent/            # 🤖 LLM Agent (agentic system)
        ├── routers/          # API endpoints
        └── services/         # Business logic
```

## Key Documentation

- **📖 Full Setup**: `README.md`
- **💼 Business Case**: `docs/BUSINESS_STRATEGY.md` (40% of grade)
- **🤖 Agentic System**: `docs/AGENTIC_SYSTEM_EXPLAINED.md`
- **💬 Examples**: `docs/CONVERSATION_FLOWS.md`
- **✅ Requirements**: `docs/SUBMISSION_CHECKLIST.md`
- **🧪 Test Results**: `docs/LLM_AGENT_TEST_RESULTS.md`

## What Makes This Agentic?

1. **LLM Decision Making** - Agent decides which tools to use
2. **Tool Calling** - 4 tools: search, details, availability, booking
3. **Context Awareness** - Remembers conversation history
4. **Natural Language** - Understands user intent
5. **Multi-Turn Conversations** - Handles complex interactions

## Features

✅ Chat interface with LLM agent (llama-3.3-70b)
✅ 100 real venues across 10 cuisines and cities
✅ Full reservation system (create, view, cancel)
✅ Admin dashboard with analytics
✅ Email notifications (optional)
✅ Responsive design

## Tech Stack

- **Frontend**: Next.js 15, TypeScript, Tailwind CSS
- **Backend**: Python, FastAPI, SQLAlchemy
- **LLM**: Groq API (llama-3.3-70b-versatile)
- **Database**: SQLite (100 venues)

## Need Help?

- **Setup Issues**: See `README.md`
- **Backend Help**: See `backend/QUICKSTART.md`
- **Email Setup**: See `backend/EMAIL_SETUP.md`
- **Structure**: See `docs/PROJECT_STRUCTURE.md`

---

**Ready to go!** 🎉
