#funtion to call open ai api

import os
from openai import OpenAI
from openai.types import Completion

client = OpenAI(
    api_key="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",
)
model = "gpt-4"
    
def call_gpt(role:str,full_prompt:str):
    messages = [
        {
        "role": role,
        "content": full_prompt
    }
    ]

    gpt_response = client.chat.completions.create(
        messages=messages,
        model=model
    )

    return gpt_response


