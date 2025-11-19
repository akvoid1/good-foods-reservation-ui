# 📋 Manual MVC Reorganization Guide

## Quick Overview

We're splitting the project into:
- **frontend/** - All Next.js frontend code (MVC pattern)
- **backend-api/** - All Python backend code (MVC pattern)
- **docs/** - Documentation (stays at root)
- **tests/** - Tests (stays at root)

## Step-by-Step Instructions

### Step 1: Move Frontend Files

```bash
# Move Next.js app
move app frontend\src\app
move components frontend\src\components
move hooks frontend\src\hooks
move public frontend\public
move styles\globals.css frontend\src\styles\globals.css

# Move lib to services/utils
move lib\api.ts frontend\src\services\api-client.ts
move lib\session.ts frontend\src\utils\session.ts
move lib\utils.ts frontend\src\utils\cn.ts

# Move config files
move package.json frontend\
move package-lock.json frontend\
move next.config.mjs frontend\
move tsconfig.json frontend\
move tailwind.config.ts frontend\
move components.json frontend\
move postcss.config.mjs frontend\
move .env.local frontend\
move .env.example frontend\
move next-env.d.ts frontend\
```

### Step 2: Move Backend Files

```bash
# Move main files
move backend\run.py backend-api\
move backend\seed_data.py backend-api\
move backend\requirements.txt backend-api\
move backend\.env backend-api\
move backend\.env.example backend-api\
move backend\.gitignore backend-api\
move backend\goodfoods.db backend-api\

# Move app files
move backend\app\main.py backend-api\
move backend\app\database.py backend-api\models\
move backend\app\models.py backend-api\models\schemas.py
move backend\app\config.py backend-api\config\settings.py

# Move routers to controllers
move backend\app\routers backend-api\controllers

# Move services
move backend\app\services backend-api\services

# Move agent
move backend\app\agent backend-api\agent
```

### Step 3: Create __init__.py Files

Create empty `__init__.py` in:
- backend-api/
- backend-api/models/
- backend-api/views/
- backend-api/controllers/
- backend-api/services/
- backend-api/agent/
- backend-api/config/
- backend-api/utils/

### Step 4: Update Imports

#### Backend Import Updates

**In backend-api/main.py:**
```python
# Old
from app.routers import agent, reservations
from app.database import engine, Base

# New
from controllers import agent, reservations
from models.database import engine, Base
```

**In backend-api/controllers/*.py:**
```python
# Old
from app.services import venue_service
from app.models import VenueResponse

# New
from services import venue_service
from models.schemas import VenueResponse
```

**In backend-api/services/*.py:**
```python
# Old
from app.database import get_db
from app.models import Venue

# New
from models.database import get_db, Venue
```

#### Frontend Import Updates

**In frontend/src/app/page.tsx:**
```typescript
// Old
import { ChatPane } from '@/components/chat-pane'
import { api } from '@/lib/api'

// New
import { ChatPane } from '@/components/chat-pane'
import { api } from '@/services/api-client'
```

**In frontend/src/components/*.tsx:**
```typescript
// Old
import { cn } from '@/lib/utils'
import { getSessionId } from '@/lib/session'

// New
import { cn } from '@/utils/cn'
import { getSessionId } from '@/utils/session'
```

### Step 5: Update Configuration

**frontend/tsconfig.json:**
```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"],
      "@/components/*": ["./src/components/*"],
      "@/services/*": ["./src/services/*"],
      "@/utils/*": ["./src/utils/*"],
      "@/hooks/*": ["./src/hooks/*"]
    }
  }
}
```

**backend-api/run.py:**
```python
# Update import
import uvicorn
from main import app  # Changed from app.main

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
```

### Step 6: Test Everything

```bash
# Test backend
cd backend-api
python run.py

# Test frontend (new terminal)
cd frontend
npm install
npm run dev

# Run tests (new terminal)
python tests/test_integration.py
```

## Final Structure

```
good-foods-reservation-ui/
├── frontend/                    # Frontend (Next.js)
│   ├── src/
│   │   ├── app/                # Controllers (pages & API routes)
│   │   ├── components/         # Views (UI components)
│   │   ├── services/           # Models (API clients)
│   │   ├── utils/              # Utilities
│   │   ├── hooks/              # React hooks
│   │   └── styles/             # Styles
│   ├── public/                 # Static assets
│   ├── package.json
│   └── ...config files
│
├── backend-api/                # Backend (Python)
│   ├── models/                 # Models (data layer)
│   ├── views/                  # Views (response formatters)
│   ├── controllers/            # Controllers (request handlers)
│   ├── services/               # Business logic
│   ├── agent/                  # AI agent
│   ├── config/                 # Configuration
│   ├── utils/                  # Utilities
│   ├── main.py
│   ├── run.py
│   └── requirements.txt
│
├── docs/                       # Documentation
├── tests/                      # Tests
├── README.md
└── QUICK_START.md
```

## Verification Checklist

- [ ] Frontend files moved to frontend/
- [ ] Backend files moved to backend-api/
- [ ] All imports updated
- [ ] Backend starts without errors
- [ ] Frontend starts without errors
- [ ] Tests pass
- [ ] All features work

## Rollback Plan

If something goes wrong:
1. The old `backend/` folder still exists
2. The old root-level frontend files still exist
3. Simply delete `frontend/` and `backend-api/` folders
4. Everything returns to original state

## Benefits

✅ Clear separation of frontend and backend
✅ Proper MVC structure in both layers
✅ Easy to navigate and maintain
✅ Scalable architecture
✅ Team-friendly organization

---

**Ready to reorganize!** 🏗️
