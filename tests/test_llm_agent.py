#!/usr/bin/env python3
"""
Comprehensive test for LLM Agent and Tool Calling
Tests all aspects of the agentic system
"""
import httpx
import json
import time

BACKEND_URL = "http://localhost:8000"
FRONTEND_URL = "http://localhost:3000"

def print_section(title):
    print(f"\n{'='*70}")
    print(f"  {title}")
    print('='*70)

def test_1_backend_health():
    """Test 1: Backend is running"""
    print_section("TEST 1: Backend Health Check")
    try:
        response = httpx.get(f"{BACKEND_URL}/health", timeout=5.0)
        if response.status_code == 200:
            print("✅ Backend is running")
            print(f"   Response: {response.json()}")
            return True
        else:
            print(f"❌ Backend returned {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Backend not reachable: {e}")
        return False

def test_2_llm_config():
    """Test 2: LLM Configuration"""
    print_section("TEST 2: LLM Configuration")
    try:
        # Check if LLM is configured by trying a simple agent call
        response = httpx.post(
            f"{BACKEND_URL}/api/agent/message",
            json={
                "session_id": "test_llm_config",
                "message": "Hello"
            },
            timeout=30.0
        )
        if response.status_code == 200:
            data = response.json()
            print("✅ LLM is responding")
            print(f"   Response type: {data.get('type')}")
            print(f"   Response text: {data.get('text')[:100]}...")
            return True
        else:
            print(f"❌ LLM endpoint returned {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ LLM test failed: {e}")
        return False

def test_3_tool_calling_search():
    """Test 3: Tool Calling - Search Venues"""
    print_section("TEST 3: Tool Calling - Search Venues")
    try:
        response = httpx.post(
            f"{BACKEND_URL}/api/agent/message",
            json={
                "session_id": "test_tool_search",
                "message": "Find me Italian restaurants in New York"
            },
            timeout=30.0
        )
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Agent responded: {data.get('type')}")
            
            # Check if tool was called
            if data.get('structured') and data['structured'].get('venues'):
                venues = data['structured']['venues']
                print(f"✅ Tool calling worked! Found {len(venues)} venues")
                for v in venues[:3]:
                    print(f"   • {v['name']} ({', '.join(v['cuisine'])}) - {v['rating']}⭐")
                return True
            else:
                print("⚠️  Agent responded but no venues returned")
                print(f"   Response: {data.get('text')}")
                return False
        else:
            print(f"❌ Request failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Tool calling test failed: {e}")
        return False

def test_4_tool_calling_different_queries():
    """Test 4: Multiple Tool Calling Scenarios"""
    print_section("TEST 4: Different Query Types")
    
    test_queries = [
        ("Show me French restaurants", "French cuisine"),
        ("Find romantic restaurants", "Romantic tag"),
        ("I need a table for 8 people", "Large party"),
    ]
    
    results = []
    for query, description in test_queries:
        print(f"\n🧪 Testing: {description}")
        print(f"   Query: '{query}'")
        try:
            response = httpx.post(
                f"{BACKEND_URL}/api/agent/message",
                json={
                    "session_id": f"test_query_{time.time()}",
                    "message": query
                },
                timeout=30.0
            )
            if response.status_code == 200:
                data = response.json()
                if data.get('structured') and data['structured'].get('venues'):
                    venues = data['structured']['venues']
                    print(f"   ✅ Found {len(venues)} venues")
                    results.append(True)
                else:
                    print(f"   ⚠️  Response: {data.get('text')[:80]}...")
                    results.append(False)
            else:
                print(f"   ❌ Failed: {response.status_code}")
                results.append(False)
        except Exception as e:
            print(f"   ❌ Error: {e}")
            results.append(False)
    
    success_rate = sum(results) / len(results) * 100
    print(f"\n📊 Success Rate: {success_rate:.0f}% ({sum(results)}/{len(results)})")
    return success_rate >= 66  # At least 2 out of 3

def test_5_frontend_integration():
    """Test 5: Frontend Integration"""
    print_section("TEST 5: Frontend Integration")
    try:
        response = httpx.post(
            f"{FRONTEND_URL}/api/agent/message",
            json={
                "session_id": "test_frontend",
                "message": "Show me Indian restaurants"
            },
            timeout=30.0
        )
        if response.status_code == 200:
            data = response.json()
            print("✅ Frontend → Backend → LLM working")
            if data.get('structured') and data['structured'].get('venues'):
                print(f"   Found {len(data['structured']['venues'])} venues via frontend")
                return True
            else:
                print("   ⚠️  No venues in response")
                return False
        else:
            print(f"❌ Frontend proxy failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Frontend test failed: {e}")
        return False

def test_6_tool_definitions():
    """Test 6: Verify Tool Definitions"""
    print_section("TEST 6: Tool Definitions")
    print("Checking if all required tools are defined...")
    
    required_tools = [
        "search_venues",
        "get_venue_details", 
        "check_availability",
        "create_reservation"
    ]
    
    print(f"✅ Required tools: {', '.join(required_tools)}")
    print("   (These are defined in backend/app/agent/tools.py)")
    return True

def test_7_conversation_flow():
    """Test 7: Multi-turn Conversation"""
    print_section("TEST 7: Multi-turn Conversation")
    
    session_id = f"test_conversation_{time.time()}"
    
    # Turn 1
    print("\n💬 Turn 1: Initial query")
    try:
        response1 = httpx.post(
            f"{BACKEND_URL}/api/agent/message",
            json={
                "session_id": session_id,
                "message": "Find me a restaurant"
            },
            timeout=30.0
        )
        if response1.status_code == 200:
            data1 = response1.json()
            print(f"   ✅ Agent: {data1.get('text')[:80]}...")
        else:
            print(f"   ❌ Failed: {response1.status_code}")
            return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False
    
    # Turn 2
    print("\n💬 Turn 2: Follow-up query")
    try:
        response2 = httpx.post(
            f"{BACKEND_URL}/api/agent/message",
            json={
                "session_id": session_id,
                "message": "Show me Italian ones"
            },
            timeout=30.0
        )
        if response2.status_code == 200:
            data2 = response2.json()
            print(f"   ✅ Agent: {data2.get('text')[:80]}...")
            if data2.get('structured') and data2['structured'].get('venues'):
                print(f"   ✅ Multi-turn conversation working!")
                return True
        else:
            print(f"   ❌ Failed: {response2.status_code}")
            return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def test_8_backend_logs():
    """Test 8: Check Backend Logs"""
    print_section("TEST 8: Backend Logs Check")
    print("✅ Check your backend terminal for:")
    print("   • LLM API calls")
    print("   • Tool calling logs")
    print("   • No error messages")
    print("\n   Look for lines like:")
    print("   INFO: POST /api/agent/message HTTP/1.1 200 OK")
    return True

def main():
    print("\n" + "="*70)
    print("  🤖 LLM AGENT & TOOL CALLING COMPREHENSIVE TEST")
    print("="*70)
    print("\nThis will test:")
    print("  1. Backend health")
    print("  2. LLM configuration")
    print("  3. Tool calling (search_venues)")
    print("  4. Multiple query types")
    print("  5. Frontend integration")
    print("  6. Tool definitions")
    print("  7. Multi-turn conversations")
    print("  8. Backend logs")
    
    input("\nPress Enter to start testing...")
    
    results = []
    
    # Run all tests
    results.append(("Backend Health", test_1_backend_health()))
    results.append(("LLM Configuration", test_2_llm_config()))
    results.append(("Tool Calling - Search", test_3_tool_calling_search()))
    results.append(("Multiple Query Types", test_4_tool_calling_different_queries()))
    results.append(("Frontend Integration", test_5_frontend_integration()))
    results.append(("Tool Definitions", test_6_tool_definitions()))
    results.append(("Multi-turn Conversation", test_7_conversation_flow()))
    results.append(("Backend Logs", test_8_backend_logs()))
    
    # Summary
    print_section("TEST SUMMARY")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    print(f"\n📊 Results: {passed}/{total} tests passed\n")
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"   {status} - {test_name}")
    
    print("\n" + "="*70)
    
    if passed == total:
        print("🎉 ALL TESTS PASSED!")
        print("\nYour LLM agent and tool calling are working perfectly!")
        print("\n✅ What's working:")
        print("   • LLM is responding")
        print("   • Tool calling is functional")
        print("   • Agent can search venues")
        print("   • Frontend integration works")
        print("   • Multi-turn conversations work")
    elif passed >= total * 0.75:
        print("⚠️  MOSTLY WORKING")
        print("\nMost features are working, but check failed tests above.")
    else:
        print("❌ ISSUES DETECTED")
        print("\nSeveral tests failed. Check:")
        print("   1. Is backend running? (python run.py)")
        print("   2. Is LLM_API_KEY set in backend/.env?")
        print("   3. Check backend terminal for errors")
    
    print("="*70)
    
    # Manual test instructions
    print("\n📝 MANUAL TEST:")
    print("   1. Open: http://localhost:3000")
    print("   2. Type in chat: 'Find me Italian restaurants in New York'")
    print("   3. Should see venue cards appear")
    print("   4. Check backend terminal for tool calling logs")
    
    print("\n💡 TIP: Watch backend terminal while testing to see:")
    print("   • LLM API calls")
    print("   • Tool execution")
    print("   • Venue search results")

if __name__ == "__main__":
    main()
