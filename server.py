from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My APP")

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b
