from crewai import Task
from agents import web_scraper_agent, eda_agent, json_converter_agent

# Task 1: Scraper les données
scrape_data_task = Task(
    description="Scraper les données de toutes les pages d'un site web donné. Assure-toi de parcourir toutes les pages et d'extraire les informations pertinentes.",
    expected_output="Données extraites sous forme de texte brut ou table structurée.",
    agent=web_scraper_agent
)

# Task 2: Nettoyer les données et faire de l'EDA
clean_data_task = Task(
    description="Nettoyer les données extraites, supprimer les doublons, corriger les valeurs manquantes, puis effectuer une analyse exploratoire basique.",
    expected_output="Données nettoyées et résumées avec un aperçu statistique.",
    agent=eda_agent
)

# Task 3: Convertir en JSON et sauvegarder
convert_to_json_task = Task(
    description="Convertir les données finales en format JSON et les sauvegarder localement dans un fichier 'output.json'.",
    expected_output="Fichier JSON nommé 'output.json'.",
    agent=json_converter_agent
)
