import json
from fastmcp import FastMCP
from src.server import app


mcp = FastMCP.from_fastapi(
    app= app,
    name="Expense-Tracking-System"

)

@mcp.resource("info://server")
def server_info() ->str:
    """
    Get information about this server
    """
    info = {
        "name": "Expense-Tracking-System Server",
        "version": "1.0.0",
        "description": "Expense tracker MCP server that tracks and gives insight about the expenses",
        "author": "Sharanch Mukhia"
    }

    return json.dumps(info, indent=2)



if __name__ == "__main__":
    mcp.run(transport="http", host = "0.0.0.0", port = 8000)
