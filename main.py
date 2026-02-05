from fastmcp import FastMCP
from src.server import app


mcp = FastMCP.from_fastapi(
    app= app,
    name="Expense-Tracking-System"

)


if __name__ == "__main__":
    mcp.run()