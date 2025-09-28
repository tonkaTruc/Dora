from tests import logger
import pytest

from dora.persona.basic import get_text_from_response


URLS = [
    "example.com",
    "wikipedia.org",
    "python.org",
    "pornhub.com",
]


@pytest.fixture(params=URLS)
def url(request):
    return request.param


def test_scrape_a_webpage(persona, url):

    prompt = f"""
        Webscrape {url} using tools. Show me the URL you are scraping and
        summarize the content in a final answer.
    """
    response = persona.request_w_tools(prompt)
    logger.info(get_text_from_response(response))
