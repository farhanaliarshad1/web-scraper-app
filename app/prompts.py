LINK_SYSTEM_PROMPT = """You are provided with a list of links found on a webpage. 
You are able to decide which of the links would be most relevant to include in a brochure about the company, 
such as links to an About page, or a Company page, or Careers/Jobs pages.
You should respond in JSON as in this example:
{
    "links": [
        {"type": "about page", "url": "https://full.url/goes/here/about"},
        {"type": "careers page", "url": "https://another.full.url/careers"}
    ]
}
"""

def get_links_user_prompt(website):
    user_prompt = f"""Website Analysis Request for: {website.url}
    
    Scraped Content Overview:
    - Main Title: {website.title}
    - Detected Sections: {[s['title'] for s in website.structured_content['sections']]}
    
    Links to Evaluate (keep brochure under 10 pages):
    {website.links[:50]}  [showing first 50 links]
    """
    return user_prompt

def get_brochure_user_prompt(company_name, url):
    return f"""Generate a professional brochure for {company_name} ({url}) with:
    
    1. Brand-consistent terminology (correct casing: {company_name})
    2. 3-4 key feature sections with technical specifications
    3. Call-to-action blocks for lead generation
    4. Responsive content structure for both print and digital
    5. Integrated SEO keywords from the scraped content
    
    Include these elements:
    - Company overview (50-75 words)
    - Core offerings table
    - Technical capabilities matrix
    - Client success metrics
    - Compliance certifications
    - Next-step engagement flow
    
    Tone: Professional yet approachable
    """