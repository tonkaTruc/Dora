
from tests import logger
from dora.api.response import create_response


def test_run_prompt():
    prompt = """
        Mix some random numbers only using tools. show me the numbers you are mixing
        and then give me the results in a final answer.
    """
    response = create_response(prompt)
    logger.debug(f"Response: {response.model_dump_json(indent=2)}")
    logger.info(f"Response: {response.output[-1].content[-1].text}")
