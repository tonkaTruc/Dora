from typing import Dict


class ExampleTool:

    def _schema(self) -> Dict:
        return {
            "type": "function",
            "name": "mix_integers",
            "description": "Mix two given integer numbers together",
            "parameters": {
                "type": "object",
                "properties": {
                    "first": {
                        "type": "integer",
                        "description": "The first integer to mix"
                    },
                    "second": {
                        "type": "integer",
                        "description": "The second integer to mix"
                    },
                },
                "required": ["first", "second"],
            },
        }

    def define(self) -> Dict:
        return self._schema()

    def mix_integers(first: int, second: int) -> str:
        print(f"Mixing integers: {first} and {second}")
        return str(int(first) + int(second))