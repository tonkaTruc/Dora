from tests import logger


def test_basic_maths(persona):
    
    prompt = """
        Mix some random numbers only using tools. show me the numbers you are mixing
        and then give me the results in a final answer.
    """
    response = persona.request_w_tools(prompt)
    logger.debug(f"Response: {response.model_dump_json(indent=2)}")
    logger.info(f"Response: {response.output[-1].content[-1].text}")