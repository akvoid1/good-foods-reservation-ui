from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.database import init_db
from app.routers import agent, reservations

app = FastAPI(
    title="GoodFoods API",
    description="AI-powered restaurant reservation system",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database
@app.on_event("startup")
async def startup_event():
    init_db()

# Include routers
app.include_router(agent.router, prefix="/api/agent", tags=["agent"])
app.include_router(reservations.router, prefix="/api/reservations", tags=["reservations"])

@app.get("/")
async def root():
    return {"message": "GoodFoods API", "status": "running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
