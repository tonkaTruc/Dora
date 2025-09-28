from dora.persona.basic import get_text_from_response
from tests import logger


def test_basic_maths(persona):

    prompt = """
        Mix some random numbers only using tools. show me the numbers you are mixing
        and then give me the results in a final answer.
    """
    response = persona.request_w_tools(prompt)
    logger.info(get_text_from_response(response))
