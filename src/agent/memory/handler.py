from typing import Dict, Any
from strands import Agent, tool
from strands_tools import mem0_memory
from strands.models import BedrockModel
from dotenv import load_dotenv
load_dotenv()

# System prompt
SYSTEM_PROMPT = """You are a helpful personal assistant that provides personalized responses based on user history.

Capabilities:
- Store information with mem0_memory (action="store")
- Retrieve memories with mem0_memory (action="retrieve")

Key Rules:
- Be conversational and natural
- Retrieve memories before responding
- Store new user information and preferences
- Share only relevant information
- Politely indicate when information is unavailable
"""

# Lambda handler
def memory(event: Dict[str, Any], _context) -> Any:
    user_id = event.get("user_id")
    action = event.get("action", "chat")
    content = event.get("content")

    if not user_id:
        return {"error": "Missing 'user' in event payload."}

    if not content and action not in ["list"]:
        return {"error": "Missing 'content' in event payload."}


    memory_agent = Agent(
        system_prompt=SYSTEM_PROMPT,
        tools=[mem0_memory],
    )

    try:
        if action == "store":
            result = memory_agent.tool.mem0_memory(
                action="store",
                content=content,
                user_id=user_id,
            )
        elif action == "retrieve":
            result = memory_agent.tool.mem0_memory(
                action="retrieve",
                content=content,
                user_id=user_id,
            )
        elif action == "list":
            result = memory_agent.tool.mem0_memory(
                action="list",
                user_id=user_id,
            )
        elif action == "chat":
            result = memory_agent("USER_ID:"+user_id+" - "+content)
        else:
            return {"error": f"Unknown action: {action}"}

        return {"result": "done"}

    except Exception as e:
        return {"error": str(e)}
