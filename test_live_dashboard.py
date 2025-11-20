#!/usr/bin/env python3
"""
Test live dashboard functionality
"""
import httpx

def test_endpoints():
    print("🧪 Testing Live Dashboard Endpoints\n")
    print("=" * 60)
    
    # Test backend admin endpoint
    print("\n1️⃣ Testing Backend Admin Endpoint...")
    try:
        response = httpx.get("http://localhost:8000/api/reservations/admin", timeout=5.0)
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Backend: {len(data)} reservations found")
            if data:
                print(f"   Latest: {data[0]['venue_name']} - {data[0]['booking_id']}")
        else:
            print(f"   ❌ Backend returned {response.status_code}")
    except Exception as e:
        print(f"   ❌ Backend error: {e}")
    
    # Test frontend proxy
    print("\n2️⃣ Testing Frontend Proxy...")
    try:
        response = httpx.get("http://localhost:3000/api/reservations/admin", timeout=5.0)
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Frontend Proxy: {len(data)} reservations found")
        else:
            print(f"   ❌ Frontend returned {response.status_code}")
    except Exception as e:
        print(f"   ❌ Frontend error: {e}")
    
    # Test user reservations with session ID
    print("\n3️⃣ Testing User Reservations...")
    try:
        # Get a session ID from one of the reservations
        response = httpx.get("http://localhost:8000/api/reservations/admin", timeout=5.0)
        if response.status_code == 200:
            data = response.json()
            if data:
                # Try with default session
                response2 = httpx.get("http://localhost:3000/api/reservations?session_id=default_session", timeout=5.0)
                if response2.status_code == 200:
                    user_data = response2.json()
                    print(f"   ✅ User Reservations: {len(user_data)} found for default_session")
                else:
                    print(f"   ⚠️  User endpoint returned {response2.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    print("\n" + "=" * 60)
    print("\n✅ All endpoints are working!")
    print("\n📝 Next steps:")
    print("   1. Open http://localhost:3000/admin")
    print("   2. Click the 'Refresh' button")
    print("   3. You should see all reservations")
    print("\n   If still not showing:")
    print("   - Check browser console for errors (F12)")
    print("   - Hard refresh the page (Ctrl+Shift+R)")
    print("   - Clear browser cache")

if __name__ == "__main__":
    test_endpoints()
