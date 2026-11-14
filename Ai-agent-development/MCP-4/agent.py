from openai import OpenAI
from dotenv import load_dotenv
from mcp_client import *
import os
import asyncio
# Load configuration
load_dotenv()

#create ai agent
ai_client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)


async def main():
    client = await connect()
    tools = await discover_tools(
        client
    )
    print()
    print("Available tools")
    print("------------")
    tool_descriptions = build_tool_description(tools)
    print(tool_descriptions)
    user_input = input("User: ")
    tool_selected = planner(user_input, tool_descriptions)
    print("Tool selected: ",tool_selected)
    await disconnect(client)
    print("mcp connection disconnected")

def planner(user_input, tool_description):
    prompt= f"""Check the available tools and user input and give me the best suitable tool based on the tools available: {tool_description} and return tool name as a result in case no tool matching return message as 'No relevant tool available'"""
    response = ai_client.chat.completions.create(model=os.getenv("MODEL"), messages=[{"role":"system","content":prompt},{
        "role":"user",
        "content":user_input
    }])
    return response.choices[0].message.content


def build_tool_description(tools):
    descriptions = ""
    for tool in tools:
        descriptions += f"""Tool: {tool.name} Description:{tool.description}---------------------
                        """
    return descriptions


if __name__ == "__main__":
    asyncio.run(main())