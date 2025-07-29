## Serper API Tool
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
load_dotenv()
import os

os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")


# Initialize the Serper API tool
serper_dev_tool = SerperDevTool(
    name="Serper API",
    description="A tool to search the web for the latest news and information using the Serper API.",
    api_key=os.getenv("SERPER_API_KEY"),
    verbose=True,
)