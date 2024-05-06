#funtion to call open ai api

import os
from openai import OpenAI
from openai.types import Completion
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env

client = OpenAI(
    api_key=os.getenv("API_KEY"),
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




