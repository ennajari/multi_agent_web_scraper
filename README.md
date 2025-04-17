# Multi-Agent System with CrewAI and Gemini

This project implements a multi-agent system using CrewAI and Google's Gemini 1.5 Flash model. It consists of three agents:
1. **Web Scraper**: Scrapes textual content from a specified website.
2. **Data Cleaner & EDA**: Removes duplicates and performs exploratory data analysis.
3. **Data Exporter**: Converts cleaned data to JSON and generates a downloadable file.

## Prerequisites
- Python 3.8+
- Google Gemini API key

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd multiagent_project
   multiagent_project/
├── agents/
│   ├── __init__.py
│   ├── scraper_agent.py
│   ├── cleaner_eda_agent.py
│   └── exporter_agent.py
├── tasks/
│   ├── __init__.py
│   ├── scraping_task.py
│   ├── cleaning_eda_task.py
│   └── export_task.py
├── tools/
│   ├── __init__.py
│   ├── custom_tools.py
│   └── gemini_llm.py
├── data/
│   ├── input/
│   │   └── urls.txt
│   ├── output/
│   │   ├── scraped_data.txt
│   │   ├── cleaned_data.csv
│   │   └── output.json
│   └── logs/
│       └── execution.log
├── config/
│   ├── __init__.py
│   └── settings.py
├── main.py
├── requirements.txt
├── README.md
└── .env