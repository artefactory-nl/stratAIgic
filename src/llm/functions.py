#funtion to call open ai api

import os
from openai import OpenAI

client = OpenAI(
    api_key="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",
)

def test_gpt(input:str):
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)
    
def call_gpt():
    
    return ""

