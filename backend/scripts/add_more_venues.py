#!/usr/bin/env python3
"""
Add more specific venues with unique characteristics
"""
from app.database import SessionLocal, Venue, init_db

# Premium/unique venues to add variety
PREMIUM_VENUES = [
    {
        "id": "v101",
        "name": "Eleven Madison Park",
        "cuisine": ["French", "Fine Dining"],
        "rating": 4.9,
        "capacity": 80,
        "price_tier": 4,
        "city": "New York",
        "address": "11 Madison Ave",
        "latitude": 40.7425,
        "longitude": -73.9871,
        "image": "/luxury-french-restaurant-elegant.jpg",
        "tags": ["Michelin Star", "Tasting Menu", "Romantic", "Wine Pairing"],
        "operating_hours": {
            "monday": "Closed",
            "tuesday": "17:30-22:00",
            "wednesday": "17:30-22:00",
            "thursday": "17:30-22:00",
            "friday": "17:30-22:30",
            "saturday": "17:30-22:30",
            "sunday": "17:30-21:00"
        },
        "phone": "+1-212-889-0905",
        "email": "reservations@elevenmadisonpark.com",
        "description": "Three Michelin-starred restaurant offering an exceptional tasting menu experience",
        "is_active": True
    },
    {
        "id": "v102",
        "name": "Nobu Malibu",
        "cuisine": ["Japanese", "Fusion"],
        "rating": 4.7,
        "capacity": 120,
        "price_tier": 4,
        "city": "Los Angeles",
        "address": "22706 Pacific Coast Hwy",
        "latitude": 34.0347,
        "longitude": -118.6803,
        "image": "/elegant-asian-dining-space.jpg",
        "tags": ["Oceanfront", "Celebrity Hotspot", "Sushi", "Sake Bar"],
        "operating_hours": {
            "monday": "12:00-22:00",
            "tuesday": "12:00-22:00",
            "wednesday": "12:00-22:00",
            "thursday": "12:00-22:00",
            "friday": "12:00-23:00",
            "saturday": "12:00-23:00",
            "sunday": "12:00-22:00"
        },
        "phone": "+1-310-317-9140",
        "email": "malibu@noburestaurants.com",
        "description": "Iconic Japanese-Peruvian fusion with stunning ocean views",
        "is_active": True
    },
]


def add_premium_venues():
    """Add premium venues to database"""
    init_db()
    db = SessionLocal()
    
    try:
        print("Adding premium venues...")
        for venue_data in PREMIUM_VENUES:
            # Check if exists
            existing = db.query(Venue).filter(Venue.id == venue_data["id"]).first()
            if existing:
                print(f"  Skipping {venue_data['name']} (already exists)")
                continue
            
            venue = Venue(**venue_data)
            db.add(venue)
            print(f"  ✅ Added {venue_data['name']}")
        
        db.commit()
        print(f"\n✅ Successfully added {len(PREMIUM_VENUES)} premium venues!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    add_premium_venues()
