#!/usr/bin/env python3
"""
Team Operator for Data Analyst agent
Provides different operational interfaces for the team.
"""

from teams.team import create_data_analyst_agent


def get_team():
    """Get the default team instance"""
    return create_data_analyst_agent()


def get_team_with_config(user_id: str = None, session_id: str = None, debug_mode: bool = False):
    """Get team with custom configuration"""
    return create_data_analyst_agent(
        user_id=user_id,
        session_id=session_id, 
        debug_mode=debug_mode
    )


# For backwards compatibility
def get_agent():
    """Get the team (for API compatibility)"""
    return get_team()
