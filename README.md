# GoodFoods - AI-Powered Restaurant Reservation System

A complete full-stack application featuring an LLM-powered conversational AI agent for restaurant reservations. Built with Next.js, FastAPI, and llama-3.3-70b with tool calling capabilities.

## 🎥 Demo Video

[Link to demo video - to be recorded]

## 🌟 Key Features

- **Conversational AI Agent**: Natural language booking with llama-3.3-70b
- **Tool Calling Architecture**: LLM decides which tools to use (search, book, cancel)
- **100 Real Venues**: Populated database across 10 cuisines and 10 cities
- **Full Reservation System**: Create, view, and cancel bookings
- **Intelligent Recommendations**: Context-aware venue suggestions
- **Responsive UI**: Modern design with Tailwind CSS and shadcn/ui
- **Admin Dashboard**: Analytics and reservation management

## Features

- **Chat Interface**: Conversational AI agent for personalized recommendations and reservations
- **Venue Discovery**: Browse and filter restaurants with map and list views
- **Smart Reservations**: Multi-step booking flow with date, time, party size, and contact info
- **User Bookings**: View and manage your reservations with cancellation support
- **Admin Dashboard**: Manager view with key metrics and upcoming reservations
- **Mobile-First Design**: Fully responsive with accessible components
- **Design System**: Warm, modern aesthetic with teal and amber accent colors

## 🏗️ Architecture

```
Next.js Frontend (Port 3000)
    ↓ API Routes
Python Backend (Port 8000)
    ↓ LLM Agent + Tools
Groq API (llama-3.3-70b)
    ↓ Database
SQLite (100 venues)
```

## 🛠️ Tech Stack

### Frontend
- **Framework**: Next.js 15+ (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS v4
- **UI Components**: shadcn/ui
- **Icons**: lucide-react

### Backend
- **Framework**: FastAPI (Python)
- **Database**: SQLAlchemy + SQLite
- **LLM**: Groq API (llama-3.3-70b-versatile)
- **API Client**: OpenAI-compatible

### AI/ML
- **Model**: llama-3.3-70b-versatile
- **Provider**: Groq (fast inference)
- **Architecture**: Tool calling with 4 tools
- **Tools**: search_venues, get_venue_details, check_availability, create_reservation

## Project Structure

\`\`\`
/app
  /api              # API route handlers
    /agent          # LLM agent endpoints
    /reservations   # Booking endpoints
  /(public)
  /admin            # Manager dashboard
  /discover         # Venue discovery
  /reservations     # User bookings
  /layout.tsx       # Root layout
  /page.tsx         # Home page
  /globals.css      # Global styles & design tokens

/components
  /ui               # shadcn/ui components
  /chat-pane.tsx    # Chat widget
  /venue-card.tsx   # Venue display card
  /filter-bar.tsx   # Discovery filters
  /map-view.tsx     # Map placeholder
  /recommendation-drawer.tsx  # AI recommendations
  /reservation-modal.tsx      # Booking flow

/lib
  /api.ts           # API client functions
  /session.ts       # Session management
  /utils.ts         # Utility functions

/public             # Static assets & venue images
\`\`\`

## 🚀 Quick Start

### Prerequisites

- Python 3.8+ (for backend)
- Node.js 18+ (for frontend)
- Groq API key (free at https://console.groq.com)

### Installation

#### 1. Backend Setup

\`\`\`bash
# Navigate to backend
cd backend

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your Groq API key:
# LLM_API_KEY=your_groq_key_here

# Seed database with 100 venues
python seed_data.py

# Start backend server
python run.py
\`\`\`

Backend will run on: http://localhost:8000

#### 2. Frontend Setup

\`\`\`bash
# In project root
npm install --legacy-peer-deps

# Configure environment
cp .env.example .env.local
# BACKEND_URL is already set to http://localhost:8000

# Start frontend server
npm run dev
\`\`\`

Frontend will run on: http://localhost:3000

#### 3. Test Integration

\`\`\`bash
# Run comprehensive tests
python tests/test_llm_agent.py
python tests/test_integration.py
\`\`\`

### 🎯 Quick Test

1. Open http://localhost:3000
2. Type in chat: "Find me Italian restaurants in New York"
3. Agent will search database and return real venues
4. Click on a venue to make a reservation

## 📖 Usage

### Chat Interface

The AI agent understands natural language queries:

\`\`\`
"Find me Italian restaurants in New York"
"Table for 4 tonight at 8pm"
"Show me romantic places with outdoor seating"
"I need a quiet spot for a business lunch"
\`\`\`

The agent will:
1. Understand your intent
2. Call appropriate tools (search_venues, check_availability, etc.)
3. Return personalized recommendations
4. Guide you through booking

### Pages

- **Home** (`/`): Chat interface + featured venues
- **Discover** (`/discover`): Browse all 100 venues with filters
- **Reservations** (`/reservations`): View and manage bookings
- **Admin** (`/admin`): Analytics dashboard

### Making a Reservation

**Via Chat:**
1. Describe what you want: "Italian restaurant for 2 tonight"
2. Agent shows options
3. Say "Book [restaurant name]"
4. Provide contact info
5. Get confirmation with booking ID

**Via UI:**
1. Browse venues or use filters
2. Click on a venue card
3. Fill out reservation form
4. Submit and receive confirmation

## 🔌 API Endpoints

All Next.js routes proxy to Python backend.

### Agent Endpoints

**POST** `/api/agent/message`
\`\`\`json
{
  "session_id": "user123",
  "message": "Find Italian restaurants"
}
\`\`\`

Response:
\`\`\`json
{
  "type": "tool_result",
  "text": "I found some great options...",
  "structured": {
    "venues": [...]
  },
  "suggested_replies": ["Tell me more", "Book one"]
}
\`\`\`

**POST** `/api/agent/recommend`
\`\`\`json
{
  "cuisine": "Italian",
  "city": "New York"
}
\`\`\`

### Reservation Endpoints

**POST** `/api/reservations/create`
\`\`\`json
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
\`\`\`

**GET** `/api/reservations?session_id=xxx`

**POST** `/api/reservations/{id}/cancel`

### Backend API Docs

FastAPI auto-generates docs: http://localhost:8000/docs

## ⚙️ Configuration

### Backend (.env)
\`\`\`env
# LLM Configuration
LLM_API_KEY=your_groq_key_here
LLM_BASE_URL=https://api.groq.com/openai/v1
LLM_MODEL=llama-3.3-70b-versatile

# Database
DATABASE_URL=sqlite:///./goodfoods.db

# API
API_HOST=0.0.0.0
API_PORT=8000
CORS_ORIGINS=http://localhost:3000
\`\`\`

### Frontend (.env.local)
\`\`\`env
BACKEND_URL=http://localhost:8000
NEXT_PUBLIC_API_BASE=/api
NEXT_PUBLIC_LLM_PROVIDER=groq/llama-3.3-70b-versatile
\`\`\`

## Customization

### Design System

Edit `/app/globals.css` to customize:
- Color palette (primary: teal, accent: amber)
- Typography (Geist font family)
- Border radius and spacing scale

### Venue Data

Replace mock data in:
- `/app/page.tsx` - Home page venues
- `/app/discover/page.tsx` - Discovery page venues
- `/components/chat-pane.tsx` - Chat recommendations

### Backend Integration

Replace mock API routes in `/app/api/` with real backend calls:
- Connect to your LLM backend for agent messages
- Integrate with your database for reservations
- Implement authentication and authorization

## Deployment

### Vercel (Recommended)

1. **Push to GitHub** (or GitLab/Bitbucket)
2. **Connect to Vercel**: `https://vercel.com/new`
3. **Add environment variables** in project settings
4. **Deploy**: Automatic deployment on git push

### Production Build

\`\`\`bash
npm run build
npm start
\`\`\`

## Performance Optimizations

- Client-side caching with SWR
- Image lazy-loading with Next.js Image
- Skeleton loaders for better UX
- Optimized Tailwind CSS with purging
- API route caching where applicable

## Accessibility

- Semantic HTML elements
- ARIA labels and roles
- Keyboard navigation support
- Color contrast compliance (WCAG AA)
- Focus management in modals

## Contributing

Contributions are welcome! Please follow:
1. Feature branch from `main`
2. Commit with clear messages
3. Test on mobile and desktop
4. Submit pull request

## License

MIT

## Support

For issues or questions, please open an issue on GitHub or contact support.

## 📊 Database

The system includes 100 pre-populated venues:

- **10 Cuisines**: Italian, Indian, Chinese, French, Japanese, Mexican, Mediterranean, Thai, American, Korean
- **10 Cities**: New York, LA, Chicago, San Francisco, Boston, Seattle, Austin, Miami, Denver, Portland
- **Realistic Data**: Ratings (3.8-5.0), capacities (40-200), price tiers (1-4), tags, operating hours

Seed database:
\`\`\`bash
cd backend
python seed_data.py
\`\`\`

## 🧪 Testing

### Comprehensive LLM Agent Test
\`\`\`bash
python tests/test_llm_agent.py
\`\`\`

Tests:
- ✅ LLM connectivity and tool calling
- ✅ Search venues functionality
- ✅ Get venue details
- ✅ Check availability
- ✅ Create reservations
- ✅ Multi-turn conversations
- ✅ Context awareness

### Integration Tests
\`\`\`bash
python tests/test_integration.py
\`\`\`

Tests:
- ✅ Backend health
- ✅ Frontend health
- ✅ Agent endpoint (LLM + tool calling)
- ✅ Recommendations
- ✅ Reservation creation

## 📚 Documentation

- **[docs/BUSINESS_STRATEGY.md](docs/BUSINESS_STRATEGY.md)**: Complete business case, ROI analysis, market opportunity
- **[docs/CONVERSATION_FLOWS.md](docs/CONVERSATION_FLOWS.md)**: 10 example conversation patterns
- **[docs/AGENTIC_SYSTEM_EXPLAINED.md](docs/AGENTIC_SYSTEM_EXPLAINED.md)**: What makes this system agentic
- **[docs/SUBMISSION_CHECKLIST.md](docs/SUBMISSION_CHECKLIST.md)**: Requirements verification
- **[docs/LLM_AGENT_TEST_RESULTS.md](docs/LLM_AGENT_TEST_RESULTS.md)**: Test results and proof
- **[backend/QUICKSTART.md](backend/QUICKSTART.md)**: Backend setup guide
- **[backend/EMAIL_SETUP.md](backend/EMAIL_SETUP.md)**: Email configuration guide

## 🎯 Project Status

### ✅ Completed (Steps 1-5)
1. ✅ Python backend with FastAPI
2. ✅ Database with 100 venues
3. ✅ LLM integration (Groq/llama-3.3)
4. ✅ Frontend-backend integration
5. ✅ Business strategy document

### 🔄 In Progress (Steps 6-8)
6. ⏳ Test conversation flows
7. ⏳ Record demo video
8. ⏳ Polish documentation

## 🏆 Key Achievements

- **Full Stack**: Complete working system from UI to database
- **Real AI**: Actual LLM with tool calling, not mocked responses
- **100 Venues**: Realistic restaurant data across multiple cities
- **Tool Calling**: LLM decides which tools to use based on user intent
- **Production Ready**: Error handling, validation, CORS, environment config

## 🚀 Deployment

### Backend (Python)
- Deploy to: Railway, Render, or AWS
- Database: Upgrade to PostgreSQL for production
- Environment: Set LLM_API_KEY and DATABASE_URL

### Frontend (Next.js)
- Deploy to: Vercel (recommended)
- Environment: Set BACKEND_URL to production backend
- Build: `npm run build`

## 🤝 Contributing

This is a challenge submission project. For production use:
1. Add authentication (JWT, OAuth)
2. Upgrade to PostgreSQL
3. Add rate limiting
4. Implement caching (Redis)
5. Add monitoring (Sentry, DataDog)
6. Write comprehensive tests

## 📝 License

MIT

## 🙏 Acknowledgments

- Challenge by Sarvam AI
- Built with Next.js, FastAPI, and Groq
- UI components from shadcn/ui
- LLM: llama-3.3-70b-versatile

---

**Built for**: AI Agent Challenge - Restaurant Reservation System  
**Duration**: 4-6 hours  
**Stack**: Python (FastAPI) + Next.js + LLM (llama-3.3)  
**Status**: Functional MVP with business strategy
