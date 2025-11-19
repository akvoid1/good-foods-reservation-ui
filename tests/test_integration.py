#!/usr/bin/env python3
"""
Test full stack integration (Frontend → Backend)
"""
import httpx
import time

FRONTEND_URL = "http://localhost:3000"
BACKEND_URL = "http://localhost:8000"

def test_backend_health():
    """Test backend is running"""
    print("1️⃣ Testing backend health...")
    try:
        response = httpx.get(f"{BACKEND_URL}/health", timeout=5.0)
        if response.status_code == 200:
            print("   ✅ Backend is running")
            return True
        else:
            print(f"   ❌ Backend returned {response.status_code}")
            return False
    except Exception as e:
        print(f"   ❌ Backend not reachable: {e}")
        return False

def test_frontend_health():
    """Test frontend is running"""
    print("\n2️⃣ Testing frontend health...")
    try:
        response = httpx.get(FRONTEND_URL, timeout=5.0)
        if response.status_code == 200:
            print("   ✅ Frontend is running")
            return True
        else:
            print(f"   ❌ Frontend returned {response.status_code}")
            return False
    except Exception as e:
        print(f"   ❌ Frontend not reachable: {e}")
        return False

def test_agent_via_frontend():
    """Test agent endpoint through frontend proxy"""
    print("\n3️⃣ Testing agent endpoint (Frontend → Backend)...")
    try:
        response = httpx.post(
            f"{FRONTEND_URL}/api/agent/message",
            json={
                "session_id": "integration_test",
                "message": "Find me Italian restaurants in New York"
            },
            timeout=30.0
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Agent responded: {data['type']}")
            if data.get('structured', {}).get('venues'):
                venues = data['structured']['venues']
                print(f"   ✅ Found {len(venues)} venues")
                for v in venues[:2]:
                    print(f"      • {v['name']} - {v['rating']}⭐")
            return True
        else:
            print(f"   ❌ Request failed: {response.status_code}")
            print(f"      {response.text}")
            return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def test_recommendations_via_frontend():
    """Test recommendations endpoint through frontend proxy"""
    print("\n4️⃣ Testing recommendations (Frontend → Backend)...")
    try:
        response = httpx.post(
            f"{FRONTEND_URL}/api/agent/recommend",
            json={
                "cuisine": "French",
                "city": "Los Angeles"
            },
            timeout=10.0
        )
        
        if response.status_code == 200:
            data = response.json()
            venues = data.get('venues', [])
            print(f"   ✅ Found {len(venues)} French restaurants")
            for v in venues[:2]:
                print(f"      • {v['name']} - {v['city']}")
            return True
        else:
            print(f"   ❌ Request failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def test_reservation_via_frontend():
    """Test reservation creation through frontend proxy"""
    print("\n5️⃣ Testing reservation creation (Frontend → Backend)...")
    try:
        response = httpx.post(
            f"{FRONTEND_URL}/api/reservations/create",
            json={
                "venue_id": "v001",
                "datetime": "2024-12-25T19:00:00",
                "party_size": 4,
                "contact": {
                    "name": "Integration Test",
                    "phone": "+1-555-TEST",
                    "email": "test@integration.com"
                },
                "notes": "Test reservation"
            },
            timeout=10.0
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Reservation created: {data['booking_id']}")
            print(f"      Venue: {data['venue_name']}")
            print(f"      Status: {data['status']}")
            return True
        else:
            print(f"   ❌ Request failed: {response.status_code}")
            print(f"      {response.text}")
            return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def main():
    print("🧪 Testing Full Stack Integration")
    print("=" * 60)
    print("\nMake sure both servers are running:")
    print("  Backend:  http://localhost:8000")
    print("  Frontend: http://localhost:3000")
    print("\n" + "=" * 60)
    
    time.sleep(1)
    
    results = []
    results.append(test_backend_health())
    results.append(test_frontend_health())
    
    if all(results):
        results.append(test_agent_via_frontend())
        results.append(test_recommendations_via_frontend())
        results.append(test_reservation_via_frontend())
    
    print("\n" + "=" * 60)
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print(f"✅ All {total} tests passed!")
        print("\n🎉 Full stack integration is working!")
        print("\n📝 Next steps:")
        print("   1. Open http://localhost:3000 in browser")
        print("   2. Test chat interface")
        print("   3. Try making a reservation")
        print("   4. Check backend logs for LLM calls")
    else:
        print(f"⚠️  {passed}/{total} tests passed")
        print("\nTroubleshooting:")
        print("   - Make sure backend is running: cd backend && python run.py")
        print("   - Make sure frontend is running: npm run dev")
        print("   - Check .env files are configured")

if __name__ == "__main__":
    main()
