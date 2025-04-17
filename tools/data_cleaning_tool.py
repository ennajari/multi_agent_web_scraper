from crewai_tools import BaseTool
import pandas as pd

class DataCleaningTool(BaseTool):
    name = "DataCleaningTool"
    description = "Nettoie les données, supprime les doublons, analyse les données"

    def _run(self, data):
        try:
            df = pd.DataFrame(data, columns=["text"])
            df.drop_duplicates(inplace=True)
            df.dropna(inplace=True)
            summary = df.describe(include='all')
            return df.to_dict(orient="records"), summary.to_string()
        except Exception as e:
            return f"Erreur lors du nettoyage: {str(e)}"
