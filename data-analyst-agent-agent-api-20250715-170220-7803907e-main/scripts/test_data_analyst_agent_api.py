#!/usr/bin/env python3
"""
API Test Script for Data Analyst agent
Test the team through the FastAPI endpoints.
"""

import requests
import json
import time


def test_team_api(base_url: str = "http://localhost:8000"):
    """Test the team API endpoints"""
    
    print(f"Testing Data Analyst agent API at {base_url}")
    print("=" * 60)
    
    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/health")
        print(f"✅ Health check: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return
    
    # Test team endpoint
    test_query = "Analyze the sales data for the last quarter"
    
    payload = {
        "message": test_query,
        "user_id": "test_user_123",
        "session_id": "test_session_456"
    }
    
    try:
        print(f"\n🤖 Testing team with query: '{test_query}'")
        print("-" * 50)
        
        start_time = time.time()
        response = requests.post(
            f"{base_url}/v1/teams/run",
            json=payload,
            timeout=60
        )
        end_time = time.time()
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Time: {end_time - start_time:.2f}s")
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Success!")
            print(f"Response: {result.get('response', 'No response field')}")
        else:
            print(f"❌ Error: {response.text}")
            
    except requests.exceptions.Timeout:
        print("❌ Request timed out (>60s)")
    except Exception as e:
        print(f"❌ Request failed: {e}")


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description=f"Test Data Analyst agent API")
    parser.add_argument("--url", default="http://localhost:8000", 
                       help="Base URL of the API server")
    args = parser.parse_args()
    
    test_team_api(args.url)


if __name__ == "__main__":
    main()
