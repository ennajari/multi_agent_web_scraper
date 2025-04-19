from scraper import fetch_page
from parser import parse_page
from storage import save_to_csv
from config import load_config

class SmartScraperAgent:
    def __init__(self):
        self.config = load_config()

    def run(self):
        url = self.config['scraper']['base_url']
        output_file = self.config['scraper']['output_file']

        print(f"[Agent] Scraping : {url}")
        page_content = fetch_page(url)

        if page_content:
            data = parse_page(page_content)
            save_to_csv(data, output_file)
            print(f"[Agent] Données sauvegardées dans {output_file}")
        else:
            print("[Agent] Échec du scraping.")
