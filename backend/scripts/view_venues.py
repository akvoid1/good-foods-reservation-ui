#!/usr/bin/env python3
"""
View venues in the database
"""
from app.database import SessionLocal, Venue
from sqlalchemy import func

def view_venues(limit: int = 10):
    """Display venues from database"""
    db = SessionLocal()
    
    try:
        # Get total count
        total = db.query(func.count(Venue.id)).scalar()
        print(f"📊 Total Venues: {total}\n")
        
        # Get sample venues
        venues = db.query(Venue).limit(limit).all()
        
        print(f"Showing first {limit} venues:\n")
        print("-" * 80)
        
        for venue in venues:
            print(f"ID: {venue.id}")
            print(f"Name: {venue.name}")
            print(f"Cuisine: {', '.join(venue.cuisine)}")
            print(f"City: {venue.city}")
            print(f"Rating: {venue.rating} ⭐")
            print(f"Price: {'$' * venue.price_tier}")
            print(f"Capacity: {venue.capacity} people")
            print(f"Tags: {', '.join(venue.tags) if venue.tags else 'None'}")
            print("-" * 80)
        
        # Stats by cuisine
        print("\n📊 Venues by Cuisine:")
        cuisines = {}
        all_venues = db.query(Venue).all()
        for v in all_venues:
            cuisine = v.cuisine[0] if v.cuisine else "Unknown"
            cuisines[cuisine] = cuisines.get(cuisine, 0) + 1
        
        for cuisine, count in sorted(cuisines.items(), key=lambda x: x[1], reverse=True):
            print(f"  {cuisine}: {count}")
        
        # Stats by city
        print("\n🌆 Venues by City:")
        cities = {}
        for v in all_venues:
            cities[v.city] = cities.get(v.city, 0) + 1
        
        for city, count in sorted(cities.items(), key=lambda x: x[1], reverse=True):
            print(f"  {city}: {count}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    import sys
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    view_venues(limit)
