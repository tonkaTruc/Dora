from dora.persona.basic import BasicPersona
from tests import logger


def test_basic_persona(persona):
    logger.info(persona)
    assert isinstance(persona, BasicPersona)


def test_basic_persona_tools(persona):
    for tool in persona.tools.values():
        logger.info(tool.definition)
        assert isinstance(tool.definition, dict)
