#!/usr/bin/env python3
"""
Seed database with 100 realistic restaurant venues
"""
from app.database import SessionLocal, Venue, init_db
import random

# Restaurant data templates
CUISINES = {
    "Italian": ["Trattoria", "Osteria", "Ristorante", "Pizzeria"],
    "Indian": ["Spice", "Curry", "Tandoor", "Masala"],
    "Chinese": ["Dragon", "Jade", "Golden", "Lotus"],
    "French": ["Le", "La", "Chez", "Bistro"],
    "Japanese": ["Sakura", "Zen", "Koi", "Sushi"],
    "Mexican": ["El", "La", "Casa", "Cantina"],
    "Mediterranean": ["Olive", "Azure", "Aegean", "Santorini"],
    "Thai": ["Bangkok", "Siam", "Thai", "Orchid"],
    "American": ["Grill", "Steakhouse", "Diner", "Tavern"],
    "Korean": ["Seoul", "Kimchi", "BBQ", "Hanok"],
}

SUFFIXES = [
    "House", "Kitchen", "Table", "Room", "Place", "Spot", "Corner",
    "Garden", "Palace", "Lounge", "Bar", "Cafe", "Restaurant"
]

CITIES = [
    "New York", "Los Angeles", "Chicago", "San Francisco", "Boston",
    "Seattle", "Austin", "Miami", "Denver", "Portland"
]

TAGS_POOL = [
    "Outdoor seating", "Vegetarian friendly", "Vegan options", "Gluten-free",
    "Wine selection", "Craft cocktails", "Private rooms", "Group friendly",
    "Romantic", "Family friendly", "Business casual", "Fine dining",
    "Quiet", "Live music", "Rooftop", "Waterfront", "Pet friendly",
    "Late night", "Brunch", "Happy hour", "Reservations recommended"
]

DESCRIPTIONS = {
    "Italian": "Authentic Italian cuisine with fresh pasta and wood-fired pizzas",
    "Indian": "Traditional Indian flavors with aromatic spices and tandoor specialties",
    "Chinese": "Classic Chinese dishes with modern presentation and fresh ingredients",
    "French": "Elegant French dining with seasonal ingredients and fine wines",
    "Japanese": "Fresh sushi and traditional Japanese dishes in a serene setting",
    "Mexican": "Vibrant Mexican flavors with handmade tortillas and fresh salsas",
    "Mediterranean": "Mediterranean-inspired dishes with olive oil and fresh herbs",
    "Thai": "Authentic Thai cuisine with bold flavors and aromatic curries",
    "American": "Contemporary American fare with locally sourced ingredients",
    "Korean": "Traditional Korean BBQ and dishes with bold, spicy flavors",
}

IMAGES = [
    "/upscale-indian-restaurant-interior.jpg",
    "/modern-italian-restaurant-ambiance.jpg",
    "/elegant-asian-dining-space.jpg",
    "/luxury-french-restaurant-elegant.jpg",
]


def generate_venue_name(cuisine: str) -> str:
    """Generate a realistic restaurant name"""
    prefix = random.choice(CUISINES[cuisine])
    suffix = random.choice(SUFFIXES)
    
    # Sometimes add "The" prefix
    if random.random() > 0.6:
        return f"The {prefix} {suffix}"
    return f"{prefix} {suffix}"


def generate_venues(count: int = 100):
    """Generate venue data"""
    venues = []
    
    for i in range(count):
        # Pick cuisine
        cuisine = random.choice(list(CUISINES.keys()))
        
        # Generate name
        name = generate_venue_name(cuisine)
        
        # Pick city
        city = random.choice(CITIES)
        
        # Generate other attributes
        rating = round(random.uniform(3.8, 5.0), 1)
        capacity = random.choice([40, 60, 80, 100, 120, 150, 200])
        price_tier = random.choices([1, 2, 3, 4], weights=[0.2, 0.4, 0.3, 0.1])[0]
        
        # Generate tags (2-4 random tags)
        num_tags = random.randint(2, 4)
        tags = random.sample(TAGS_POOL, num_tags)
        
        # Generate coordinates (mock)
        latitude = round(random.uniform(25.0, 48.0), 6)
        longitude = round(random.uniform(-122.0, -71.0), 6)
        
        # Operating hours
        operating_hours = {
            "monday": "11:00-22:00",
            "tuesday": "11:00-22:00",
            "wednesday": "11:00-22:00",
            "thursday": "11:00-22:00",
            "friday": "11:00-23:00",
            "saturday": "10:00-23:00",
            "sunday": "10:00-21:00"
        }
        
        venue = {
            "id": f"v{str(i+1).zfill(3)}",
            "name": name,
            "cuisine": [cuisine] + (["Fusion"] if random.random() > 0.7 else []),
            "rating": rating,
            "capacity": capacity,
            "price_tier": price_tier,
            "city": city,
            "address": f"{random.randint(100, 9999)} {random.choice(['Main', 'Oak', 'Elm', 'Park', 'Market'])} St",
            "latitude": latitude,
            "longitude": longitude,
            "image": random.choice(IMAGES),
            "tags": tags,
            "operating_hours": operating_hours,
            "phone": f"+1-{random.randint(200, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}",
            "email": f"info@{name.lower().replace(' ', '').replace('the', '')}.com",
            "description": DESCRIPTIONS[cuisine],
            "is_active": True
        }
        
        venues.append(venue)
    
    return venues


def seed_database():
    """Seed the database with venues"""
    print("Initializing database...")
    init_db()
    
    print("Generating 100 venues...")
    venues_data = generate_venues(100)
    
    db = SessionLocal()
    try:
        # Clear existing venues
        db.query(Venue).delete()
        db.commit()
        
        print("Inserting venues into database...")
        for venue_data in venues_data:
            venue = Venue(**venue_data)
            db.add(venue)
        
        db.commit()
        print(f"✅ Successfully seeded {len(venues_data)} venues!")
        
        # Print some stats
        cuisines = {}
        for v in venues_data:
            cuisine = v["cuisine"][0]
            cuisines[cuisine] = cuisines.get(cuisine, 0) + 1
        
        print("\n📊 Venue Distribution:")
        for cuisine, count in sorted(cuisines.items(), key=lambda x: x[1], reverse=True):
            print(f"  {cuisine}: {count}")
        
        print(f"\n🌆 Cities: {len(set(v['city'] for v in venues_data))}")
        print(f"💰 Price Tiers: 1-4")
        print(f"⭐ Ratings: 3.8-5.0")
        
    except Exception as e:
        print(f"❌ Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
