# Web Scraper & Brochure Generator 🌐📚

A Python-based tool for extracting website content and generating professional brochures with AI analysis.

![Demo Screenshot](![alt text](image.png))

## Features ✨
- Website content scraping with intelligent filtering
- AI-powered link analysis and categorization
- Automated brochure generation in markdown format
- Streamlit-based web interface
- Customizable prompts for different use cases

## Tech Stack 💻
- **Web Scraping**: `BeautifulSoup4`, `requests`
- **AI Integration**: `Ollama`/LLM prompts
- **Frontend**: `Streamlit`
- **Content Processing**: `regex`, `markdown`
- **Packaging**: `pip`, `virtualenv`

## Installation 🛠️
1. Clone the repository:
```bash
git clone https://github.com/farhanaliarshad1/web-scraper-app.git
cd web-scraper-app

## Create and activate virtual environment:
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows

##Install dependencies:
pip install -r requirements.txt

##Start the Streamlit app:
streamlit run streamlit_app.py

