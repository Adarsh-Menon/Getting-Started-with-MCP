from mcp.server.fastmcp import FastMCP

#creation of an MCP SERVER

mcp = FastMCP("DEMO")

#Adding an tool for adding two numbers
def add(a:int,b:int) -> int:
    return a+b


#Adding a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name:str)->str:
    return f"hello , {name}!"