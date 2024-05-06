"""Generate persona for business."""
from llm import call_gpt

def generate_persona(
    business_attributes: dict[str, str], persona_attributes: dict[str, str]
) -> dict[str, str]:
    """Generate persona for business."""
    business_attributes = business_attributes
    persona_attributes = persona_attributes
    persona = create_persona_with_LLM(persona_attributes, business_attributes["product_category"], business_attributes["product_description"])
    return persona

def create_persona_with_LLM(persona_attributes, product_category, product_description):

    prompt = f"""Generate a persona for marketing a {product_category} based on the following
    {{
      "gender": "{persona_attributes['gender']}",
      "country": "{persona_attributes['country']}",
      "age": "{persona_attributes['age']}",
      "comments": "{persona_attributes['comments']}"
    }}

    Our product's description is : {product_description}

    Each key should contain at least 3 sentences:
    {{
    "Name":
    "The struggles and pains of the persona":
    "The other products the persona thinks about":
    "The goals of the persona":
    "The benefits of our product for the persona:"
    "Marketing tagline for the persona":
    }}

    Do not add any other information."""

    gpt_response = call_gpt(role="user", full_prompt=prompt)

    response_text = gpt_response.choices[0].message.content
    
    return transform_to_json(response_text)

def transform_to_json(input_str):
    prompt = f"""Convert the following 6 persona details: {input_str} in a json format containing 5 keys,
    one for each detail. Don't modify the persona details at all when you use them as key,
    don't lowercase them and keep the whitespaces.

    Always answer in the following json format:

    {{
        "<persona detail key>":"<persona detail value>",
        "<persona detail key>":"<persona detail value>",
        "<persona detail key>":"<persona detail value>",
        "<persona detail key>":"<persona detail value>",
        "<persona detail key>":"<persona detail value>",
        "<persona detail key>":"<persona detail value>",
    }}


    ----------------------------------------
    
    ONLY JSON IS ALLOWED as an answer. No explanation or other text is allowed.

    """
    response = call_gpt(role="user", full_prompt=prompt)
    return response.choices[0].message.content
