from typing import Dict
import requests
from bs4 import BeautifulSoup
import logging


class WebscrapeTool:

    def __init__(self) -> None:
        self.log = logging.getLogger(__name__)
        self.name = "web_scrape"
        self.description = "Scrape the content of a webpage given its URL"
        self.properties = {
            "url": {
                "type": "string",
                "description": "The URL of the webpage to scrape"
            }
        }

    def __call__(self, url: str) -> str:
        self.log.debug(f"Getting content of {url}")
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text()
            return text[:100]  # Limit characters to avoid overload
        except requests.RequestException as e:
            return f"Error fetching the URL: {e}"

    @property
    def definition(self) -> Dict:
        return {
            "type": "function",
            "name": self.name,
            "description": self.description,
            "parameters": {
                "type": "object",
                "properties": self.properties,
                "required": [x for x in self.properties.keys()],
            },
        }
