import os
from .pypi_mcp_test import mcp

def main() -> None:
    """Run the FAL AI Image Generator MCP server."""
    
    # Check for API key
    fal_api_key = os.getenv("FAL_API_KEY") or os.getenv("FAL_KEY")
    if not fal_api_key:
        raise ValueError("Neither FAL_API_KEY nor FAL_KEY environment variables are set")
    
    # Run the MCP server
    mcp.run()
