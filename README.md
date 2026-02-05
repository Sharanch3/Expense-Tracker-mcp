# 📝 Problem Statement

Tracking expenses manually using spreadsheets or traditional apps is tedious and error-prone. This project provides an **AI-powered expense tracking system** where users can speak naturally to add expenses, retrieve records, and get summarized insights—**eliminating manual data entry** while giving instant, actionable financial information.


This project addresses these challenges through a **conversational AI interface** built on the **Model Context Protocol (MCP)**, enabling natural language interaction with a robust FastAPI backend.

# 💰 Expense Tracking System

A FastAPI-based expense tracking application with Model Context Protocol (MCP) integration for AI-powered expense management.



## ✨ Features

- ✅ Add single or multiple expenses in one request
- 📅 Fetch expenses for a specific date
- 📊 List expenses within a date range
- 📈 Category-wise expense summary with percentages
- 🤖 MCP integration for AI-powered interactions
- 🔄 RESTful API design
- 📝 Automatic API documentation (Swagger/OpenAPI)

## 🛠 Tech Stack

- **Framework**: FastAPI
- **ORM**: SQLAlchemy
- **Database**: MySQL 
- **Validation**: Pydantic
- **MCP**: FastMCP
- **Server**: Uvicorn


## 🤖 MCP Integration

The MCP (Model Context Protocol) integration allows AI assistants like Claude to interact with your expense tracking system directly.

### What is MCP?

MCP is a protocol that enables AI models to connect to external tools and data sources. With this integration, you can:

- Ask an AI to add expenses via natural language
- Query your expenses conversationally
- Get insights and summaries through AI analysis

### MCP Server Setup

The `mcp_server.py` file wraps your FastAPI application with FastMCP:



### Using with Claude Desktop

1. **Configure Claude Desktop** to connect to your MCP server
2. **Start the MCP server**: `python mcp_server.py`
3. **Interact naturally**: "Add a $50 food expense for today" or "Show me my spending summary for last month"

---

**Made with ❤️ using FastAPI and MCP**