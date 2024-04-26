import os
from openai import OpenAI
from openai.types import Completion

def test_placeholder() -> None:
    """To be replaced with actual tests."""
    pass


client = OpenAI(
    api_key="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",
)
model = "gpt-4"


def test_gpt():
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model=model
    )
    return chat_completion