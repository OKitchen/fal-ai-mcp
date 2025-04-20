import os
from mcp.server.fastmcp import FastMCP
import fal_client


# Retrieve the API key from the environment variable
FAL_API_KEY = os.getenv("FAL_API_KEY") or os.getenv("FAL_KEY")
if not FAL_API_KEY:
    raise ValueError("Neither FAL_API_KEY nor FAL_KEY environment variables are set")

# The fal_client automatically uses the FAL_API_KEY environment variable
# No need to explicitly set the API key

mcp = FastMCP("fal-ai-image-generator", description="Generate images from text using HiDream-I1-Full model via Fal.ai")

@mcp.tool()
def text_to_image_fal(prompt: str) -> dict:
    """Generate an image from text using HiDream-I1-Full model via Fal.ai"""
    # Call Fal.ai's subscribe method to generate the image
    result = fal_client.subscribe(
        "fal-ai/hidream-i1-full",
        arguments={"prompt": prompt},
    )
    
    # Return the complete result with image URL, dimensions, and other metadata
    return result