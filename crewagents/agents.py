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

# Creating a Editor agent with custom tools responsible for editing the news articles
editor_agent = Agent(
    role="Editor",
    goal="Review and edit the news article to ensure clarity, accuracy, and engagement.",
    verbose=True,
    memory=True,
    backstory="You are an experienced editor with a keen eye for detail. Your task is to review the news article written by the News Writer, ensuring that it is clear, accurate, and engaging. You will provide constructive feedback and make necessary edits to enhance the quality of the article.",
    llm=llm,
    tools=[],
    allow_delegation=True,
)

# Creating a fact-checker agent with custom tools responsible for verifying the facts in the news articles
fact_checker_agent = Agent(
    role="Fact Checker",
    goal="Verify the facts and sources in the news article to ensure accuracy and credibility.",
    verbose=True,
    memory=True,
    backstory="You are a meticulous fact-checker with a strong commitment to accuracy. Your task is to verify the facts and sources in the news article written by the News Writer. You will ensure that all information is accurate and credible, providing references and sources where necessary.",
    llm=llm,
    tools=[serper_dev_tool],  # Include the Serper API tool for fact-checking
    allow_delegation=True,
)

# Creating a social media manager agent with custom tools responsible for promoting the news articles
social_media_manager_agent = Agent(
    role="Social Media Manager",
    goal="Promote the news article on social media platforms to reach a wider audience.",
    verbose=True,
    memory=True,
    backstory="You are a savvy social media manager with expertise in digital marketing. Your task is to promote the news article on various social media platforms, ensuring that it reaches a wide audience. You will create engaging posts, use relevant hashtags, and interact with followers to increase visibility and engagement.",
    llm=llm,
    tools=[],
    allow_delegation=True,
)

# Creating a SEO specialist agent with custom tools responsible for optimizing the news articles for search engines
seo_specialist_agent = Agent(
    role="SEO Specialist",
    goal="Optimize the news article for search engines to improve its visibility and ranking.",
    verbose=True,
    memory=True,
    backstory="You are a skilled SEO specialist with a deep understanding of search engine algorithms. Your task is to optimize the news article for search engines, ensuring that it ranks well and is easily discoverable by readers. You will use relevant keywords, meta tags, and other SEO techniques to enhance the article's visibility.",
    llm=llm,
    tools=[],
    allow_delegation=True,
)

# Creating a data analyst agent with custom tools responsible for analyzing the performance of the news articles
data_analyst_agent = Agent(
    role="Data Analyst",
    goal="Analyze the performance of the news article and provide insights for future improvements.",
    verbose=True,
    memory=True,
    backstory="You are a data analyst with expertise in digital analytics. Your task is to analyze the performance of the news article, including metrics such as views, engagement, and social media shares. You will provide insights and recommendations for future articles based on the data collected.",
    llm=llm,
    tools=[],
    allow_delegation=True,
)

# Creating A Publisher agent with custom tools responsible for publishing the news articles
publisher_agent = Agent(
    role="Publisher",
    goal="Publish the news article on the website and ensure it is accessible to readers.",
    verbose=True,
    memory=True,
    backstory="You are a seasoned publisher with experience in managing online content. Your task is to publish the news article on the website, ensuring that it is formatted correctly and accessible to readers. You will also manage any necessary updates or revisions to the article after publication.",
    llm=llm,
    tools=[],
    allow_delegation=True,
)

