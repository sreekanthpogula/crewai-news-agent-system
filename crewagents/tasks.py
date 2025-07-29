from crewai import Task
from tools import serper_dev_tool
from agents import researcher_agent, news_writer_agent

# Research task
researcher_task = Task(
    description=(
        "You are a Senior Researcher with expertise in cutting-edge technologies.Your task is to explore and analyze the latest advancements in {topic}, it's market potential, and its impact on society. "
    ),
    expected_output="A detailed report on the latest advancements in {topic}, including key technologies, market trends, and societal impact.",
    tools=[serper_dev_tool],
    agent=researcher_agent,
)

# Writer task
news_writer_task = Task(
    description=(
        "You are a skilled news writer with a knack for storytelling. " \
        "Your task is to take the research findings from the Senior Researcher and craft them into a compelling news article. " \
        "Ensure that the article is informative, engaging, and accessible to a wide audience."
    ),
    expected_output="A comprehensive and engaging news article about the latest advancements in {topic}.",
    tools=[serper_dev_tool],
    agent=news_writer_agent,
    async_execution=False,  # Set to True if you want the task to run asynchronously
    output_file="./news_Articles/new-blog-post.md"  # Optional: specify an output file for the news article
)

