from dora.api.gpt import c_openai
from dora.api.tools.example import ExampleTool
from typing import Dict
import json 
import logging

log = logging.getLogger(__name__)

GPT_MODEL = "gpt-3.5-turbo"


def create_response(prompt: str, role: str = "user"):
    
    input_list = [{"role": role, "content": prompt}]
    
    resp = c_openai.responses.create(
        model=GPT_MODEL,
        tools=[
            ExampleTool().define()
        ],
        input=input_list
    )

    input_list += resp.output

    # Process any calls to tools
    for item in resp.output:
        if item.type == "function_call":
            if item.name == "mix_integers":
                tool_response = ExampleTool.mix_integers(**json.loads(item.arguments))
                # Add the tool response to the conversation
                tool_output = {
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": json.dumps({"result": tool_response})
                }
                input_list.append(tool_output)

    log.debug("Generated function calls:")
    for line in input_list:
        log.debug(f"\t{line}")

    return c_openai.responses.create(
        model=GPT_MODEL,
        tools=[
            ExampleTool().define()
        ],
        input=input_list
    )

    