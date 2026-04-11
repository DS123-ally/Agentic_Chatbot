from langchain_core.tools import tool
from tavily import TavilyClient
from langgraph.prebuilt import ToolNode

@tool
def tavily_search(query: str) -> str:
    """Search the web for the given query."""
    client = TavilyClient()
    response = client.search(query=query, max_results=3)
    results = response.get("results", [])
    
    formatted_results = []
    for item in results:
         formatted_results.append(
             f"Title: {item.get('title', 'No Title')}\n"
             f"Content: {item.get('content', '')}\n"
             f"URL: {item.get('url', 'No URL')}"
         )
         
    return "\n\n".join(formatted_results)

def get_tools():
    """
    Return the list of tools to be used in the Chatbot.
    """
    tools=[tavily_search]
    return tools


def create_tool_node(tools):
    """
    Creates and returns a tool node for the graph.
    """ 
    return ToolNode(tools=tools)   