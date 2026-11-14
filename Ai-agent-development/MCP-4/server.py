from datetime import datetime
from fastmcp import FastMCP
import random 

mcp = FastMCP(
    "Time Server"
)


@mcp.tool() 
def current_time():
    """ Return the current date and time"""

    return datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )

@mcp.tool()
def roll_dice():
    """Roll a six-sided dice."""
    return random.randint(1,6)


if __name__=="__main__":
    print("Starting MCP Server...")
    mcp.run()


