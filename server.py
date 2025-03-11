
#Importing the FastMCP class from the fastmcp module    
from mcp.server.fastmcp import FastMCP


#Creation of a new FastMCP instance
mcp = FastMCP("My APP")


#Creation of a new tool
@mcp.tool()
def add(name:str) -> str:
    return f"{name} is added"
