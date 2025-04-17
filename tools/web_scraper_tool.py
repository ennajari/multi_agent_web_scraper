from crewai_tools import BaseTool
import requests
from bs4 import BeautifulSoup

class WebScraperTool(BaseTool):
    name = "WebScraperTool"
    description = "Scrape toutes les pages d'un site web donné"

    def _run(self, url: str):
        results = []
        page = 1
        while True:
            try:
                response = requests.get(f"{url}?page={page}")
                if response.status_code != 200:
                    break
                soup = BeautifulSoup(response.text, 'html.parser')
                items = soup.find_all("div", class_="item")  # à adapter selon la structure du site
                if not items:
                    break
                for item in items:
                    results.append(item.get_text(strip=True))
                page += 1
            except Exception as e:
                break
        return results
