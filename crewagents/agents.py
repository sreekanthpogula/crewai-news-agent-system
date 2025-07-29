from crewai import Agent
from tools import serper_dev_tool
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Initialize the Google Generative AI model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.2,
    google_api_key=os.getenv("GOOGLE_API_KEY"))


# Creating a senior research agent with memory and verbose mode
researcher_agent = Agent(
    role="Senior Researcher",
    goal="Uncover the groundbreaking technologies and innovations in {topic} that are shaping the future.",
    verbose=True,
    memory=True,
    backstory="You are a Senior Researcher with expertise in cutting-edge technologies. Your task is to explore and analyze the latest advancements in various fields, including AI, quantum computing, biotechnology, and more. You will provide detailed insights and summaries of your findings.",
    llm=llm,
    tools=[],
    allow_delegation=True,
)

# Creating a writer agent with  custom tools responsible in writing news articles
news_writer_agent = Agent(
    role="News Writer",
    goal="Write a comprehensive and engaging news article about the latest advancements in {topic}.",
    verbose=True,
    memory=True,
    backstory="You are a skilled news writer with a knack for storytelling. Your task is to take the research findings from the Senior Researcher and craft them into a compelling news article. You will ensure that the article is informative, engaging, and accessible to a wide audience.",
    llm=llm,
    tools=[],
    allow_delegation=True,
)

