from crewai_tools import BaseTool
import json

class JsonTool(BaseTool):
    name = "JsonTool"
    description = "Convertit les données en JSON et les enregistre"

    def _run(self, data):
        try:
            with open("output.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            return "Les données ont été enregistrées dans output.json"
        except Exception as e:
            return f"Erreur lors de l'enregistrement JSON: {str(e)}"
