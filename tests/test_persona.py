from dora.persona.basic import BasicPersona
from tests import logger


def test_basic_persona(persona):
    logger.info(persona)


def test_basic_persona_tools(persona):
    for tool in persona.tools:
        logger.info(tool.definition)
        assert isinstance(tool.definition, dict)

