from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, JSON, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from datetime import datetime
from app.config import settings

engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False} if "sqlite" in settings.database_url else {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Venue(Base):
    __tablename__ = "venues"
    
    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    cuisine = Column(JSON, nullable=False)  # List of cuisines
    rating = Column(Float, default=0.0)
    capacity = Column(Integer, nullable=False)
    price_tier = Column(Integer, default=2)  # 1-4 scale
    city = Column(String, nullable=False)
    address = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    image = Column(String)
    tags = Column(JSON)  # List of tags
    operating_hours = Column(JSON)  # Dict of day -> hours
    phone = Column(String)
    email = Column(String)
    description = Column(String)
    is_active = Column(Boolean, default=True)


class Reservation(Base):
    __tablename__ = "reservations"
    
    id = Column(String, primary_key=True, index=True)
    booking_id = Column(String, unique=True, nullable=False, index=True)
    venue_id = Column(String, nullable=False, index=True)
    venue_name = Column(String, nullable=False)
    session_id = Column(String, nullable=False, index=True)
    datetime = Column(DateTime, nullable=False)
    party_size = Column(Integer, nullable=False)
    status = Column(String, default="confirmed")  # confirmed, pending, cancelled
    contact_name = Column(String, nullable=False)
    contact_phone = Column(String, nullable=False)
    contact_email = Column(String, nullable=False)
    notes = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    Base.metadata.create_all(bind=engine)
