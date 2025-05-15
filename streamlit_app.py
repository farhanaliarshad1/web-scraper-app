import streamlit as st
from app.scraper import Website
from app.ollama_client import query_ollama
from app.prompts import LINK_SYSTEM_PROMPT as link_system_prompt, get_links_user_prompt, get_brochure_user_prompt

st.set_page_config(page_title="📄 Smart Web Scraper", layout="wide")
st.title("🕸️ Company Web Scraper + Brochure Generator")

url = st.text_input("🔗 Enter a website URL")

if st.button("Scrape & Analyze"):
    website = Website(url)

    st.subheader("📃 Scraped Website Content")
    st.markdown(website.get_contents())  # Renders Markdown, keeps formatting

    st.subheader("🧠 Brochure Link Suggestions (from Ollama)")
    messages = [
        {"role": "system", "content": link_system_prompt},
        {"role": "user", "content": get_links_user_prompt(website)}
    ]
    response = query_ollama(messages)
    st.code(response, language="json")

    st.subheader("📘 Brochure Content")
    brochure_prompt = [
        {"role": "system", "content": "You are a company brochure generator."},
        {"role": "user", "content": get_brochure_user_prompt("Company", url)}
    ]
    brochure = query_ollama(brochure_prompt)
    st.markdown(brochure)
