
import pytest

from dora.persona.basic import get_text_from_response
from dora.tools.files import DOC_DUMP
from tests import logger


@pytest.fixture(scope="function", autouse=True)
def remove_test_file():
    # Remove test.txt if it exists before the test
    test_file = DOC_DUMP / "test.txt"
    if test_file.exists():
        test_file.unlink()
    yield
    # Clean up after the test
    if test_file.exists():
        test_file.unlink()


def test_write_a_file(persona):

    prompt = f"""
        Write a file called test.txt using tools. The file should contain the 
        text Hello, World! and then give me the filename in a final answer.
    """
    response = persona.request_w_tools(prompt)
    logger.info(get_text_from_response(response))

    for file in DOC_DUMP.glob("test.txt"):
        logger.info(f"Found file: {file}")
        content = file.read_text()
        logger.info(f"File content: {content}")
        assert content == '"Hello, World!"'
