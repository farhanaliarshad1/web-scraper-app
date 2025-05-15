import requests
from bs4 import BeautifulSoup
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

class Website:
    """
    Enhanced website scraper with structured content extraction
    """
    def __init__(self, url):
        self.url = url
        self._validate_url()
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        self.body = response.content
        soup = BeautifulSoup(self.body, 'html.parser')
        
        self.title = self._clean_text(soup.title.string) if soup.title else "No title found"
        self.links = self._process_links(soup)
        self.structured_content = self._extract_structured_content(soup)

    def _validate_url(self):
        """Ensure URL format is correct"""
        if not re.match(r'^https?://', self.url):
            raise ValueError("Invalid URL format")

    def _clean_text(self, text):
        """Clean and normalize text content"""
        return re.sub(r'\s+', ' ', text).strip()

    def _process_links(self, soup):
        """Extract and deduplicate links with filtering"""
        seen = set()
        return [
            link.get('href') for link in soup.find_all('a')
            if (link.get('href') and 
                link.get('href') not in seen and 
                not seen.add(link.get('href')))
        ]

    def _extract_structured_content(self, soup):
        """Hierarchical content extraction"""
        content = {"sections": []}
        current_section = None
        
        # Clean unwanted tags
        for tag in soup(['script', 'style', 'img', 'input', 'noscript', 'footer']):
            tag.decompose()

        for element in soup.find_all(['h1', 'h2', 'h3', 'p', 'ul']):
            if element.name in ['h1', 'h2', 'h3']:
                current_section = {
                    "title": self._clean_text(element.get_text()),
                    "level": int(element.name[1]),
                    "content": []
                }
                content["sections"].append(current_section)
            elif current_section and element.name == 'p':
                text = self._clean_text(element.get_text())
                if len(text) > 40:
                    current_section["content"].append(text)
            elif current_section and element.name == 'ul':
                list_items = [self._clean_text(li.get_text()) 
                             for li in element.find_all('li')]
                current_section["content"].extend(list_items)
        
        return content

    def get_contents(self):
        """Generate markdown output with improved structure"""
        markdown = [f"## **Page Title:** {self.title}\n"]
        
        for section in self.structured_content["sections"]:
            level = min(section["level"] + 1, 6)  # Prevent excessive nesting
            markdown.append(f"{'#' * level} {section['title']}")
            
            for item in section["content"]:
                if isinstance(item, list):
                    markdown.extend([f"- {point}" for point in item])
                else:
                    markdown.append(f"\n{item}\n")
        
        return "\n".join(markdown)