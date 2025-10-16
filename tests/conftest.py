import pytest
from dora.persona.basic import BasicPersona

PERSONAS = [
    BasicPersona(
        name="test-basic",
        description="A helpful assistant that can perform basic arithmetic operations like addition and subtraction."
    ),
    BasicPersona(
        name="test-rude",
        description="""
            Generally has a rude attitude towards humans, always includes an insult in responses
        """
    ),
]


@pytest.fixture(scope="session", params=PERSONAS, ids=lambda p: p.name)
def persona(request):
    return request.param
