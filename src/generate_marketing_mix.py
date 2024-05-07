from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from pathlib import Path
import re
import json
import streamlit as st
import toml

config = toml.load("config/config_details.toml")
banana_key = config["banana"].replace("AB", "")

client = ChatOpenAI(
    api_key=banana_key
)

def generate_marketing_mix(product_attributes: dict[str, str], demo=False) -> dict[str, str]:
    """Generate marketing mix for given product.

    The input, business_attributes, is a dictionary containing the following keys:
    - product_name: str
    - product_description: str
    - product_category: str
    - product_stage: str
    - product_pricing: str

    Based on this inputs, we will return a dictionary containing the following:
    """
    if demo:
        with open("sample_ins_and_outs/sample_mmx_output.json", "r") as f:
            sample_output = json.loads(f.read())
        return sample_output


    # Define paths
    path_to_prompts = Path('src/prompts')
    path_to_system_prompt = path_to_prompts / 'system_prompt.txt'
    path_to_marketing_mix_prompt = path_to_prompts / 'marketing_mix_prompt.txt'

    # PART ONE: SYSTEM
    with path_to_system_prompt.open(mode='r') as file:
        system_prompt = file.read()

    system_prompt_template = SystemMessagePromptTemplate.from_template(system_prompt)

    # PART TWO: MARKETING MIX
    with path_to_marketing_mix_prompt.open(mode='r') as file:
        mmx_prompt = file.read()

    mmx_prompt_template = HumanMessagePromptTemplate.from_template(mmx_prompt)

    # PART THREE: BUILD REQUEST
    chat_prompt_template = ChatPromptTemplate.from_messages([system_prompt_template, mmx_prompt_template])

    chat_prompt_request = chat_prompt_template.format_prompt(
        product_name=product_attributes['product_name'],
        product_description=product_attributes['product_description'],
        product_category=product_attributes['product_category'],
        product_stage=product_attributes['product_stage'],
        target_audience=product_attributes['target_audience'],
        region=product_attributes['region'],
        product_pricing=product_attributes['product_pricing'],
    ).to_messages()

    result = client(chat_prompt_request).content
    parsed_output = re.sub(r"[\`\n\t]", "", result).replace("json", "")
    json_output = json.loads(parsed_output)

    return json_output
