from crewai import Task
from tools import serper_dev_tool
from agents import researcher_agent, news_writer_agent ,editor_agent, fact_checker_agent, data_analyst_agent ,publisher_agent, social_media_manager_agent, seo_specialist_agent

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

# Editor task
editor_task = Task(
    description=(
        "You are an experienced editor with a keen eye for detail. " \
        "Your task is to review the news article written by the News Writer, ensuring that it is clear, accurate, and engaging. " \
        "Provide constructive feedback and make necessary edits to enhance the quality of the article."
    ),
    expected_output="An edited version of the news article with improvements in clarity, accuracy, and engagement.",
    tools=[serper_dev_tool],
    agent=editor_agent,
    async_execution=False,  # Set to True if you want the task to run asynchronously
    output_file="./news_Articles/edited-blog-post.md"  # Optional: specify an output file for the edited news article
)

# Fact Checker task
fact_checker_task = Task(
    description=(
        "You are a meticulous fact checker. Your task is to verify the facts and sources in the news article written by the News Writer. " \
        "Ensure that all information is accurate and credible, providing references and sources where necessary."
    ),
    expected_output="A fact-checked version of the news article with verified facts and sources.",
    tools=[serper_dev_tool],
    agent=fact_checker_agent,
    async_execution=False,  # Set to True if you want the task to run asynchronously
)

# Data Analyst task
data_analyst_task = Task(
    description=(
        "You are a Data Analyst. Your task is to analyze the data related to the latest advancements in {topic} and provide insights on trends, patterns, and potential implications. " \
        "Use statistical methods and data visualization techniques to present your findings."
    ),
    expected_output="A detailed analysis report with insights on trends, patterns, and potential implications of the latest advancements in {topic}.",
    tools=[serper_dev_tool],
    agent=data_analyst_agent,
    async_execution=False,  # Set to True if you want the task to run asynchronously
)

# Publisher task
publisher_task = Task(
    description=(
        "You are a Publisher. Your task is to publish the final news article on the company's website and ensure it is optimized for search engines. " \
        "Make sure the article is formatted correctly and includes relevant keywords for SEO."
    ),
    expected_output="The news article has been successfully published on the company's website with proper SEO optimization.",
    tools=[serper_dev_tool],
    agent=publisher_agent,
    async_execution=False,  # Set to True if you want the task to run asynchronously
    output_file="./news_Articles/published-blog-post.md"  # Optional: specify an output file for the published news article
)

# Social Media Manager task
social_media_manager_task = Task(
    description=(
        "You are a Social Media Manager. Your task is to promote the news article on various social media platforms. " \
        "Create engaging posts, use relevant hashtags, and interact with followers to increase visibility and engagement."
    ),
    expected_output="A series of social media posts promoting the news article, including engagement metrics.",
    tools=[serper_dev_tool],
    agent=social_media_manager_agent,
    async_execution=False,  # Set to True if you want the task to run asynchronously
)

# SEO Specialist task
seo_specialist_task = Task(
    description=(
        "You are an SEO Specialist. Your task is to optimize the news article for search engines to improve its visibility and ranking. " \
        "Use relevant keywords, meta tags, and other SEO techniques to enhance the article's discoverability."
    ),
    expected_output="An optimized version of the news article with improved SEO elements.",
    tools=[serper_dev_tool],
    agent=seo_specialist_agent,
    async_execution=False,  # Set to True if you want the task to run asynchronously
)

