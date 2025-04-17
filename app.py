import streamlit as st
from crew import run_crew

st.set_page_config(page_title="Multi-Agent Web Scraper", layout="wide")

st.title("🕸️ Multi-Agent Web Scraper avec CrewAI")

if st.button("Lancer le scraping multi-agents 🚀"):
    with st.spinner("Les agents travaillent..."):
        run_crew()
    st.success("Scraping terminé et fichier JSON généré ✅")
