from crewai import Crew
from tasks import scrape_data_task, clean_data_task, convert_to_json_task

crew = Crew(
    agents=[scrape_data_task.agent, clean_data_task.agent, convert_to_json_task.agent],
    tasks=[scrape_data_task, clean_data_task, convert_to_json_task],
    verbose=True
)

def run_crew():
    result = crew.kickoff()
    print("\n\033[92m### Résultat Final ###\033[0m\n")
    print(result)
