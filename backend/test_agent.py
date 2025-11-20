#!/usr/bin/env python3
"""
Test the LLM agent with sample queries
"""
import asyncio
from app.database import SessionLocal, init_db
from app.agent.agent import Agent

# Sample test queries
TEST_QUERIES = [
    "Find me an Italian restaurant in New York",
    "I need a table for 4 tonight at 8pm",
    "Show me romantic restaurants",
    "What are some good Indian places?",
    "Find a quiet place for a business lunch",
]


async def test_agent():
    """Test agent with sample queries"""
    print("🤖 Testing GoodFoods AI Agent\n")
    print("=" * 80)
    
    init_db()
    db = SessionLocal()
    agent = Agent(db)
    
    session_id = "test_session_123"
    
    for i, query in enumerate(TEST_QUERIES, 1):
        print(f"\n{i}. User: {query}")
        print("-" * 80)
        
        try:
            response = await agent.process_message(
                session_id=session_id,
                message=query
            )
            
            print(f"Agent: {response['text']}")
            print(f"Type: {response['type']}")
            
            if response.get('structured') and response['structured'].get('venues'):
                venues = response['structured']['venues']
                print(f"\n📍 Found {len(venues)} venues:")
                for v in venues[:3]:
                    print(f"   • {v['name']} ({', '.join(v['cuisine'])}) - {v['rating']}⭐")
            
            if response.get('suggested_replies'):
                print(f"\n💬 Suggestions: {', '.join(response['suggested_replies'])}")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            print("\n⚠️  Make sure you have:")
            print("   1. Added LLM_API_KEY to .env")
            print("   2. Seeded the database (python seed_data.py)")
            print("   3. Correct LLM_BASE_URL and LLM_MODEL in .env")
            break
        
        print("=" * 80)
    
    db.close()
    print("\n✅ Agent test complete!")


if __name__ == "__main__":
    asyncio.run(test_agent())
