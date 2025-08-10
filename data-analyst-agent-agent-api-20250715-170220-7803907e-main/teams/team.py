#!/usr/bin/env python3
"""
Generated team: Data Analyst agent
Factory function to create the team with runtime context and enhanced memory.
"""

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.team import Team
from agno.tools.sql import SQLTools
from dotenv import load_dotenv
from loguru import logger
from typing import Optional, List, Dict, Any
import os


def create_data_analyst_agent(user_id: str = None, session_id: str = None, debug_mode: bool = False) -> Team:
    """
    Create and configure the Data Analyst agent.
    
    Args:
        user_id: User identifier for session management
        session_id: Session identifier for conversation tracking
        debug_mode: Enable debug logging
    
    Returns:
        Configured Team instance
    """
    # Load environment variables
    load_dotenv()
    
    # Create team members
    team_members = []
    
    # Create Intent agent
    intent_agent_model = OpenAIChat(id="gpt-4o", api_key=os.getenv("LLM_PROXY_API_KEY"), base_url=os.getenv("LLM_BASE_URL"))
    intent_agent_tools = [SQLTools(**{"db_url": None, "db_engine": None, "user": "", "password": os.getenv("PASSWORD"), "host": None, "port": None, "schema": None, "dialect": None, "tables": None, "list_tables": True, "describe_table": True, "run_sql_query": False})]
    intent_agent = Agent(
        name="Intent agent",
        description="Extracts survey question metadata for NL2SQL.",
        instructions="""You are the Survey Intent Agent. Your job is to read the user’s survey question
and output ONLY a JSON object with these four keys:

1. survey_type:
   – "single" if "diagnostic_id" appears in exactly one <entity>_data table
   – "multiple" if "diagnostic_id" appears in more than one <entity>_data table

2. question_type:
   – Determine by inspecting the column definitions (e.g. data_type) in the tables,
     not by guessing from language. If "value" is numeric for that diagnostic_id, use "quantitative"; if free-text, use "qualitative".

3. tables:
   – an array of <entity>_data table names containing the "diagnostic_id" column

4. diagnostic_id:
   – the numeric ID extracted verbatim from the user’s question, or null if none found

REQUIREMENTS:
  • ALWAYS start by calling list_tables() to list all tables.
  • FILTER to those ending in "_data".
  • CALL describe_table(table_name) on each filtered table.
  • DO NOT make any inferences from question wording—use only schema details for survey_type and question_type.
  • If any tool call fails, return {"error":"<error message>"}.

Example output:
{"survey_type":"multiple","question_type":"quantitative","tables":["customer_data","rating_data"],"diagnostic_id":42}""",
        model=intent_agent_model,
        tools=intent_agent_tools,
        debug_mode=True,
        show_tool_calls=True,
        markdown=True,
        user_id=user_id,
        session_id=session_id
    )
    team_members.append(intent_agent)
    
    # Create NL2Sql Agent
    nl2sql_agent_model = OpenAIChat(id="gpt-4o", api_key=os.getenv("LLM_PROXY_API_KEY"), base_url=os.getenv("LLM_BASE_URL"))
    nl2sql_agent_tools = [SQLTools(**{"db_url": None, "db_engine": None, "user": "", "password": os.getenv("PASSWORD"), "host": None, "port": None, "schema": None, "dialect": None, "tables": None, "list_tables": True, "describe_table": True, "run_sql_query": True})]
    nl2sql_agent = Agent(
        name="NL2Sql Agent",
        instructions=[""],
        model=nl2sql_agent_model,
        tools=nl2sql_agent_tools,
        debug_mode=True,
        show_tool_calls=True,
        markdown=True,
        user_id=user_id,
        session_id=session_id
    )
    team_members.append(nl2sql_agent)
    
    # Create Analysis agent and chart generation 
    analysis_agent_and_chart_generation__model = OpenAIChat(id="gpt-4o", api_key=os.getenv("LLM_PROXY_API_KEY"), base_url=os.getenv("LLM_BASE_URL"))
    analysis_agent_and_chart_generation__tools = []
    analysis_agent_and_chart_generation_ = Agent(
        name="Analysis agent and chart generation ",
        instructions=[""],
        model=analysis_agent_and_chart_generation__model,
        tools=analysis_agent_and_chart_generation__tools,
        debug_mode=True,
        show_tool_calls=True,
        markdown=True,
        user_id=user_id,
        session_id=session_id
    )
    team_members.append(analysis_agent_and_chart_generation_)
    
    # Create the team
    team = Team(
        name="Data Analyst agent",
        description="Orchestrates intent parsing, SQL generation, and result analysis.",
        instructions=[""],
        members=team_members,
        debug_mode=debug_mode
    )
    
    return team


def get_data_analyst_agent() -> Team:
    """Get a default instance of Data Analyst agent"""
    return create_data_analyst_agent()