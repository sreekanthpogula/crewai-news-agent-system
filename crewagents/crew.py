from crewai import Crew, Process
from agents import researcher_agent, news_writer_agent ,editor_agent, fact_checker_agent, data_analyst_agent ,publisher_agent, social_media_manager_agent, seo_specialist_agent
from tasks import researcher_task, news_writer_task, editor_task, fact_checker_task, data_analyst_task, publisher_task, social_media_manager_task, seo_specialist_task
from tools import serper_dev_tool

# Forming the Crew instance with the necessary tools
crew = Crew(
    agents=[researcher_agent, news_writer_agent, editor_agent, fact_checker_agent, data_analyst_agent, publisher_agent, social_media_manager_agent, seo_specialist_agent],
    tasks=[researcher_task, news_writer_task, editor_task, fact_checker_task, data_analyst_task, publisher_task, social_media_manager_task, seo_specialist_task],
    process=Process.sequential,  # Define the execution order of tasks
    tools=[serper_dev_tool],  # Include the Serper API tool
)

# Start the crew process with enhanced feedback

result = crew.kickoff(inputs={"topic": "Elon Musk's impact on space exploration"})
print("Crew process completed successfully.")
print("Final output:", result)
