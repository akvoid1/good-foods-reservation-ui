from pydantic import BaseModel, EmailStr
from typing import List, Optional, Dict, Any
from datetime import datetime


# Agent Models
class AgentMessageRequest(BaseModel):
    session_id: str
    message: str
    context: Optional[Dict[str, Any]] = None


class VenueStructured(BaseModel):
    id: str
    name: str
    distance_km: Optional[float] = None
    score: Optional[float] = None
    cuisine: List[str]
    rating: float
    price_tier: int
    capacity: int
    image: Optional[str] = None
    tags: Optional[List[str]] = None


class AgentResponse(BaseModel):
    type: str  # 'llm_response' or 'tool_result'
    text: str
    suggested_replies: Optional[List[str]] = None
    structured: Optional[Dict[str, Any]] = None


class RecommendRequest(BaseModel):
    city: Optional[str] = None
    cuisine: Optional[str] = None
    datetime: Optional[str] = None
    party_size: Optional[int] = None
    prefs: Optional[Dict[str, Any]] = None


# Reservation Models
class ContactInfo(BaseModel):
    name: str
    phone: str
    email: EmailStr


class CreateReservationRequest(BaseModel):
    venue_id: str
    datetime: str
    party_size: int
    contact: ContactInfo
    notes: Optional[str] = None


class ReservationResponse(BaseModel):
    id: str
    venue_id: str
    venue_name: str
    datetime: str
    party_size: int
    status: str
    contact: ContactInfo
    notes: Optional[str] = None
    booking_id: str


# Venue Models
class VenueResponse(BaseModel):
    id: str
    name: str
    cuisine: List[str]
    rating: float
    capacity: int
    price_tier: int
    city: str
    address: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    image: Optional[str] = None
    tags: Optional[List[str]] = None
    phone: Optional[str] = None
    description: Optional[str] = None
