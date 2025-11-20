#!/usr/bin/env python3
"""
Test backend setup and database
"""
from app.database import SessionLocal, Venue, init_db
from app.services.venue_service import VenueService
from sqlalchemy import func

def test_setup():
    """Test database and services"""
    print("🧪 Testing GoodFoods Backend Setup\n")
    
    # Test 1: Database connection
    print("1️⃣ Testing database connection...")
    try:
        init_db()
        db = SessionLocal()
        count = db.query(func.count(Venue.id)).scalar()
        print(f"   ✅ Database connected! Found {count} venues\n")
        
        if count == 0:
            print("   ⚠️  No venues found. Run: python seed_data.py\n")
            return
        
    except Exception as e:
        print(f"   ❌ Database error: {e}\n")
        return
    
    # Test 2: Venue service
    print("2️⃣ Testing venue service...")
    try:
        service = VenueService(db)
        
        # Test search
        italian = service.search_venues(cuisine="Italian", limit=3)
        print(f"   ✅ Search by cuisine: Found {len(italian)} Italian restaurants")
        
        # Test city search
        ny = service.search_venues(city="New York", limit=3)
        print(f"   ✅ Search by city: Found {len(ny)} restaurants in New York")
        
        # Test party size
        large = service.search_venues(party_size=100, limit=3)
        print(f"   ✅ Search by capacity: Found {len(large)} venues for 100+ people")
        
        # Test get venue
        if italian:
            venue = service.get_venue(italian[0].id)
            print(f"   ✅ Get venue details: {venue.name}\n")
        
    except Exception as e:
        print(f"   ❌ Service error: {e}\n")
        return
    
    # Test 3: Sample venues
    print("3️⃣ Sample venues:")
    venues = db.query(Venue).limit(5).all()
    for v in venues:
        print(f"   • {v.name} ({', '.join(v.cuisine)}) - {v.city} - {v.rating}⭐ - {'$' * v.price_tier}")
    
    print("\n✅ All tests passed! Backend is ready.")
    print("\n📝 Next steps:")
    print("   1. Add your LLM API key to .env")
    print("   2. Run: python run.py")
    print("   3. Test at: http://localhost:8000/health")
    
    db.close()


if __name__ == "__main__":
    test_setup()
