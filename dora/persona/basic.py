
from dora.tools.numbers import NumberTool
from openai import OpenAI
from typing import List, Dict
import logging
import json

GPT_MODEL = "gpt-3.5-turbo"
TOOLS = [
    NumberTool
] 

class BasicPersona:

    def __init__(self, name: str, description: str) -> None:
       self.log = logging.getLogger(__name__)
       self.name = name
       self.role = "user"
       self.description = description
       self.tools = self._load_tools()
       self.c_openai = OpenAI()

    def __str__(self) -> str:
        return f"{self.name}: {self.description}"
    
    def _load_tools(self) -> list: 
        return [x() for x in TOOLS]
    
    def _create_response(self, input_list: list[Dict]=None) -> Dict:
        
        return self.c_openai.responses.create(
            model=GPT_MODEL,
            tools=[
                tool.definition for tool in self.tools
            ],
            input=input_list
        )
    
    def _context(self) -> List[Dict]:
        return [{"role": "system", "content": self.description}]

    def request_w_tools(self, prompt: str) -> List[dict]:

        input_list = self._context() + [{"role": self.role, "content": prompt}]
        resp = self._create_response(input_list)
        input_list += resp.output

        # Process any calls to tools
        for item in resp.output:
            
            if item.type == "function_call":

                # Get the tool function from the tools list
                try:
                    func = next((t for t in self.tools if t.name == item.name), None)
                except AttributeError as e:
                    self.log.error(f"Function {item.name} not found: {e}")
                    raise e
                
                # Call the tool function with the provided arguments
                args = json.loads(item.arguments)
                try:
                    tool_response = func(**args)
                except TypeError as e:
                    self.log.error(f"Error calling function {item.name} with arguments {args}: {e}")
                    raise e
                
                input_list.append({
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": json.dumps({"result": tool_response})
                })

        self.log.debug("Generated function calls:")
        for line in input_list:
            self.log.debug(f"\t{line}")
        
        return self._create_response(input_list)
