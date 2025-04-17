from crewai import Agent
from tools.web_scraper_tool import WebScraperTool
from tools.data_cleaning_tool import DataCleaningTool
from tools.json_tool import JsonTool

web_scraper_tool = WebScraperTool()
data_cleaning_tool = DataCleaningTool()
json_tool = JsonTool()

# Agent 1: Web Scraper
web_scraper_agent = Agent(
    role="Web Scraper",
    goal="Extraire les données de toutes les pages d'un site web donné",
    backstory="Expert en scraping web avec une connaissance approfondie des structures HTML.",
    tools=[web_scraper_tool],
    verbose=True
)

# Agent 2: Nettoyage et EDA
eda_agent = Agent(
    role="Data Cleaner and Analyst",
    goal="Nettoyer les données extraites, supprimer les doublons et réaliser une analyse exploratoire",
    backstory="Spécialiste des données avec une expertise en nettoyage et analyse de données.",
    tools=[data_cleaning_tool],
    verbose=True
)

# Agent 3: Convertisseur JSON
json_converter_agent = Agent(
    role="JSON Converter",
    goal="Convertir les données analysées en JSON et les sauvegarder dans un fichier",
    backstory="Expert en formats de données, notamment JSON, et automatisation des sauvegardes.",
    tools=[json_tool],
    verbose=True
)
