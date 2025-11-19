# 🍽️ GoodFoods - AI Restaurant Reservation System

> Full-stack restaurant reservation platform powered by conversational AI agent with LLM tool calling

[![Next.js](https://img.shields.io/badge/Next.js-15-black)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-009688)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue)](https://www.typescriptlang.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## 🌟 Features

- 🤖 **Conversational AI Agent** - Natural language booking with llama-3.3-70b
- 🛠️ **Tool Calling Architecture** - LLM decides which tools to use (search, book, cancel)
- 🍕 **100 Real Venues** - Pre-populated database across 10 cuisines and 10 cities
- 📅 **Full Reservation System** - Create, view, and cancel bookings
- 💡 **Intelligent Recommendations** - Context-aware venue suggestions
- 📊 **Admin Dashboard** - Analytics and reservation management
- 📧 **Email Notifications** - Automated booking confirmations
- 🎨 **Modern UI** - Responsive design with Tailwind CSS and shadcn/ui

## 🏗️ Architecture

```
┌─────────────────────────────────────────────┐
│         Next.js Frontend (Port 3000)        │
│  ┌─────────────────────────────────────┐   │
│  │  MVC Pattern                        │   │
│  │  • Views: Components                │   │
│  │  • Controllers: App Router          │   │
│  │  • Models: API Services             │   │
│  └─────────────────────────────────────┘   │
└──────────────────┬──────────────────────────┘
                   │ REST API
┌──────────────────▼──────────────────────────┐
│      Python Backend (Port 8000)             │
│  ┌─────────────────────────────────────┐   │
│  │  MVC Pattern                        │   │
│  │  • Models: SQLAlchemy               │   │
│  │  • Views: Response Formatters       │   │
│  │  • Controllers: FastAPI Routes      │   │
│  │  • Services: Business Logic         │   │
│  └─────────────────────────────────────┘   │
│  ┌─────────────────────────────────────┐   │
│  │  AI Agent (Agentic System)         │   │
│  │  • LLM: llama-3.3-70b (Groq)       │   │
│  │  • Tools: 4 function tools          │   │
│  │  • Context: Conversation memory     │   │
│  └─────────────────────────────────────┘   │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│         SQLite Database                     │
│  • 100 venues (10 cuisines × 10 cities)    │
│  • Reservations with full details          │
└─────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Node.js 18+
- Python 3.8+
- Groq API key (free at [console.groq.com](https://console.groq.com))

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/akvoid1/good-foods-reservation-ui.git
cd good-foods-reservation-ui
```

**2. Backend Setup**
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your Groq API key
python seed_data.py  # Populate database with 100 venues
python run.py        # Start backend on http://localhost:8000
```

**3. Frontend Setup** (new terminal)
```bash
npm install --legacy-peer-deps
npm run dev  # Start frontend on http://localhost:3000
```

**4. Test It**
```bash
python tests/test_llm_agent.py
```

### Try It Out

1. Open http://localhost:3000
2. Type: **"Find me Italian restaurants in New York"**
3. See the AI agent search and recommend venues
4. Click a venue to make a reservation

## 🛠️ Tech Stack

### Frontend
- **Framework:** Next.js 15 (App Router)
- **Language:** TypeScript
- **Styling:** Tailwind CSS v4
- **UI Components:** shadcn/ui
- **State Management:** React hooks
- **API Client:** Fetch API

### Backend
- **Framework:** FastAPI (Python)
- **Database:** SQLAlchemy + SQLite
- **LLM:** Groq API (llama-3.3-70b-versatile)
- **Email:** SMTP (Gmail)
- **Validation:** Pydantic

### AI/ML
- **Model:** llama-3.3-70b-versatile
- **Provider:** Groq (fast inference)
- **Architecture:** Tool calling with 4 tools
- **Tools:**
  - `search_venues` - Find restaurants by criteria
  - `get_venue_details` - Get specific venue info
  - `check_availability` - Check booking availability
  - `create_reservation` - Make a booking

## 📖 Documentation

- **[START_HERE.md](START_HERE.md)** - Complete getting started guide
- **[QUICK_START.md](QUICK_START.md)** - 3-minute setup
- **[docs/BUSINESS_STRATEGY.md](docs/BUSINESS_STRATEGY.md)** - Business case & ROI analysis
- **[docs/AGENTIC_SYSTEM_EXPLAINED.md](docs/AGENTIC_SYSTEM_EXPLAINED.md)** - What makes it agentic
- **[docs/CONVERSATION_FLOWS.md](docs/CONVERSATION_FLOWS.md)** - Example conversations
- **[docs/MVC_ARCHITECTURE_EXPLAINED.md](docs/MVC_ARCHITECTURE_EXPLAINED.md)** - MVC pattern explained
- **[MVC_STRUCTURE.md](MVC_STRUCTURE.md)** - Project structure overview

## 🎯 Key Features Explained

### Agentic System

The AI agent is truly agentic because:
1. **Autonomous Decision Making** - LLM decides which tools to use
2. **Tool Calling** - Dynamically selects and executes functions
3. **Context Awareness** - Maintains conversation history
4. **Natural Language** - Understands user intent without rigid commands
5. **Multi-Turn Conversations** - Handles complex booking flows

### Example Conversation

```
User: "Find me Italian restaurants in New York"
Agent: [Calls search_venues tool]
      "I found 10 great Italian restaurants in New York..."

User: "Tell me more about the first one"
Agent: [Calls get_venue_details tool]
      "Bella Italia is a 4.5-star restaurant..."

User: "Book a table for 2 tonight at 8pm"
Agent: [Calls check_availability, then create_reservation]
      "Great! I've reserved a table for 2..."
```

## 📊 Database

Pre-populated with 100 realistic venues:
- **10 Cuisines:** Italian, Indian, Chinese, French, Japanese, Mexican, Mediterranean, Thai, American, Korean
- **10 Cities:** New York, LA, Chicago, San Francisco, Boston, Seattle, Austin, Miami, Denver, Portland
- **Realistic Data:** Ratings (3.8-5.0), capacities (40-200), price tiers (1-4), tags, hours

## 🧪 Testing

```bash
# Comprehensive LLM agent test
python tests/test_llm_agent.py

# Full stack integration test
python tests/test_integration.py
```

## 📁 Project Structure

```
good-foods-reservation-ui/
├── app/                    # Next.js frontend
│   ├── page.tsx           # Home with chat
│   ├── admin/             # Admin dashboard
│   ├── discover/          # Venue discovery
│   ├── reservations/      # User bookings
│   └── api/               # API routes
├── components/            # React components
├── backend/               # Python backend
│   ├── app/
│   │   ├── agent/        # AI agent system
│   │   ├── routers/      # API endpoints
│   │   └── services/     # Business logic
│   ├── run.py
│   └── seed_data.py
├── docs/                  # Documentation
└── tests/                 # Test suite
```

## 🚀 Deployment

### Backend
- Deploy to: Railway, Render, or AWS
- Upgrade to PostgreSQL for production
- Set environment variables

### Frontend
- Deploy to: Vercel (recommended)
- Set BACKEND_URL to production backend
- Automatic deployments on push

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

MIT License - see [LICENSE](LICENSE) file

## 🙏 Acknowledgments

- Built with Next.js, FastAPI, and Groq
- UI components from shadcn/ui
- LLM: llama-3.3-70b-versatile via Groq API

## 📧 Contact

- GitHub: [@akvoid1](https://github.com/akvoid1)
- Repository: [good-foods-reservation-ui](https://github.com/akvoid1/good-foods-reservation-ui)

---

**Built with ❤️ using AI and modern web technologies**

⭐ Star this repo if you find it helpful!
