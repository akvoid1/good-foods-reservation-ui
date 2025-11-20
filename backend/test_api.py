#!/usr/bin/env python3
"""
Test API endpoints
"""
import httpx
import json

BASE_URL = "http://localhost:8000"

def test_health():
    """Test health endpoint"""
    response = httpx.get(f"{BASE_URL}/health")
    print(f"✅ Health: {response.json()}")

def test_recommend():
    """Test recommendation endpoint"""
    response = httpx.post(
        f"{BASE_URL}/api/agent/recommend",
        json={"cuisine": "Italian", "city": "New York"}
    )
    data = response.json()
    print(f"\n✅ Recommendations: Found {len(data.get('venues', []))} venues")
    for v in data.get('venues', [])[:3]:
        print(f"   • {v['name']} - {v['rating']}⭐")

def test_agent_message():
    """Test agent message endpoint"""
    response = httpx.post(
        f"{BASE_URL}/api/agent/message",
        json={
            "session_id": "test123",
            "message": "Show me Italian restaurants in New York"
        },
        timeout=30.0
    )
    data = response.json()
    print(f"\n✅ Agent Response:")
    print(f"   Type: {data['type']}")
    print(f"   Text: {data['text'][:100]}...")
    if data.get('structured', {}).get('venues'):
        print(f"   Venues: {len(data['structured']['venues'])}")

if __name__ == "__main__":
    print("🧪 Testing GoodFoods API\n")
    print("=" * 60)
    
    try:
        test_health()
        test_recommend()
        test_agent_message()
        print("\n" + "=" * 60)
        print("✅ All API tests passed!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
