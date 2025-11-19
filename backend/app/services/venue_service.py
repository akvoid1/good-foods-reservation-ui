from sqlalchemy.orm import Session
from app.database import Venue
from typing import List, Optional
from datetime import datetime


class VenueService:
    def __init__(self, db: Session):
        self.db = db
    
    def search_venues(
        self,
        cuisine: Optional[str] = None,
        city: Optional[str] = None,
        party_size: Optional[int] = None,
        price_tier: Optional[int] = None,
        tags: Optional[List[str]] = None,
        limit: int = 10
    ) -> List[Venue]:
        """
        Search venues with filters
        """
        query = self.db.query(Venue).filter(Venue.is_active == True)
        
        if cuisine:
            # SQLite JSON search
            query = query.filter(Venue.cuisine.contains(cuisine))
        
        if city:
            query = query.filter(Venue.city.ilike(f"%{city}%"))
        
        if party_size:
            query = query.filter(Venue.capacity >= party_size)
        
        if price_tier:
            query = query.filter(Venue.price_tier == price_tier)
        
        if tags:
            for tag in tags:
                query = query.filter(Venue.tags.contains(tag))
        
        # Order by rating
        query = query.order_by(Venue.rating.desc())
        
        return query.limit(limit).all()
    
    def get_venue(self, venue_id: str) -> Optional[Venue]:
        """
        Get venue by ID
        """
        return self.db.query(Venue).filter(Venue.id == venue_id).first()
    
    def check_availability(
        self,
        venue_id: str,
        datetime_str: str,
        party_size: int
    ) -> bool:
        """
        Check if venue has availability
        Simple logic: check capacity
        """
        venue = self.get_venue(venue_id)
        if not venue:
            return False
        
        # Check if party size fits
        if party_size > venue.capacity:
            return False
        
        # TODO: Check existing reservations for that time slot
        # For now, always return True if capacity fits
        return True
    
    def get_all_venues(self) -> List[Venue]:
        """
        Get all active venues
        """
        return self.db.query(Venue).filter(Venue.is_active == True).all()
