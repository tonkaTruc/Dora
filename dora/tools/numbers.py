from typing import Dict


class NumberTool:

    def __init__(self) -> None:
        self.name = "mix_integers"
        self.description = "Mix two given integer numbers together"
        self.properties = {
            "first": {
                "type": "integer",
                "description": "The first integer to mix"
            },
            "second": {
                "type": "integer",
                "description": "The second integer to mix"
            },
        }

    def __call__(self, first: int, second: int) -> str:
        return str(int(first) + int(second))

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
