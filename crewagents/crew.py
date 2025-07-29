from crewai import Crew, Process
from agents import researcher_agent, news_writer_agent
from tasks import researcher_task, news_writer_task
from tools import serper_dev_tool

# Forming the Crew instance with the necessary tools
crew = Crew(
    agents=[researcher_agent, news_writer_agent],
    tasks=[researcher_task, news_writer_task],
    process=Process.sequential,  # Define the execution order of tasks
    tools=[serper_dev_tool],  # Include the Serper API tool
)

# Start the crew process with enhanced feedback

result = crew.kickoff(inputs={"topic": "AI in Healthcare"})
print("Crew process completed successfully.")
print("Final output:", result)
