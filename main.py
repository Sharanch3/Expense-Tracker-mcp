from fastmcp import FastMCP
from src.server import app


mcp = FastMCP.from_fastapi(
    app= app,
    name="Expense-Tracking-System"

)


if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
