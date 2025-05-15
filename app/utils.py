import json
from app.scraper import Website
from app.ollama_client import query_ollama
from app.prompts import get_links_user_prompt, get_links_system_prompt

def get_links(url):
    website = Website(url)
    messages = [
        {"role": "system", "content": get_links_system_prompt()},
        {"role": "user", "content": get_links_user_prompt(website)}
    ]
    response = query_ollama(messages, format="json")
    return json.loads(response)

def get_all_details(url):
    result = "## 🔗 **Landing Page**\n"
    main_site = Website(url)
    result += main_site.get_contents()

    try:
        links = get_links(url)
        for link in links["links"]:
            result += f"\n\n---\n\n### 🔍 **{link['type'].capitalize()}**\n"
            sub_page = Website(link["url"])
            result += sub_page.get_contents()
    except Exception as e:
        result += f"\n\n❌ Failed to get related pages: {e}"

    return result
