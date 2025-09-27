from typing import Dict
import logging
from pathlib import Path
import json

DOC_DUMP = Path("dumps/")


class FileWriterTool:

    def __init__(self) -> None:
        self.log = logging.getLogger(__name__)
        self.name = "file_writer"
        self.description = """
            Write any datatype to a file in the dumps directory
            SHould allow writing bytes, strings, dicts, lists, etc
            to allow file creation
        """
        self.properties = {
            "data": {
                "type": "string",
                "description": "The data to write to the file"
            },
            "file_name": {
                "type": "string",
                "description": "The filename of the data dump"
            }
        }

    def __call__(self, data: str, file_name: str) -> str:
        file_path = DOC_DUMP / file_name
        print(f"Writing data to {file_path}")
        try:
            # Ensure the directory exists
            file_path.parent.mkdir(parents=True, exist_ok=True)

            # Write the data to the file
            with open(file_path.resolve(), 'w', encoding='utf-8') as file:
                file.write(json.dumps(data, indent=4))

            return f"Data successfully written to {file_path}"
        except OSError as e:
            return f"Error writing to file: {e}"

    @property
    def definition(self) -> Dict:
        return {
            "type": "function",
            "name": self.name,
            "description": self.description,
            "parameters": {
                "type": "object",
                "properties": self.properties,
                "required": ["data"],
            },
        }
