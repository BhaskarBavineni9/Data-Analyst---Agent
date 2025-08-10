#!/usr/bin/env python3
"""
Interactive Chat with Data Analyst agent
Run this script to have a conversation with your team.
"""

import uuid
from teams.team import create_data_analyst_agent


def main():
    print("=" * 60)
    print(f"🤖 Welcome to Data Analyst agent Interactive Chat!")
    print("=" * 60)
    print("Type 'exit', 'quit', 'bye', or 'q' to end the conversation.")
    print("=" * 60)
    
    # Create team with session
    user_id = str(uuid.uuid4())
    session_id = str(uuid.uuid4())
    
    try:
        team = create_data_analyst_agent(
            user_id=user_id,
            session_id=session_id,
            debug_mode=True
        )
        
        print(f"\n✅ Data Analyst agent is ready!")
        print(f"Team Members: {', '.join([member.name for member in team.members])}")
        print("\nYou can start asking questions now...")
        
        while True:
            try:
                print("\n" + "-" * 50)
                
                user_input = input("You: ").strip()
                
                if user_input.lower() in ['exit', 'quit', 'bye', 'q']:
                    print("\n👋 Goodbye!")
                    break
                
                if not user_input:
                    print("Please enter a question...")
                    continue
                
                print(f"\n🤖 Data Analyst agent:")
                print("-" * 50)
                
                # Use the team's run method
                response = team.run(user_input)
                print(response)
                
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
                print("Please try again...")
                
    except Exception as e:
        print(f"❌ Failed to initialize Data Analyst agent: {e}")
        print("\nPlease check your configuration and environment variables.")


if __name__ == "__main__":
    main()
