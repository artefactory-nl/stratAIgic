"""Generate persona for business."""
from llm import call_gpt
import json
import re

MAX_RETRIES = 4

def generate_persona(
    business_attributes: dict[str, str], persona_attributes: dict[str, str]
) -> dict[str, str]:
    """Generate persona for business."""
    business_attributes = business_attributes
    persona_attributes = persona_attributes
    persona = create_persona_with_LLM(persona_attributes, business_attributes["product_category"], business_attributes["product_description"])
    return persona

def create_persona_with_LLM(persona_attributes, product_category, product_description):

    global MAX_RETRIES  # Declare MAX_RETRIES as a global variable

    prompt = f"""Generate a persona for marketing a {product_category} based on the following
    {{
      "gender": "{persona_attributes['gender']}",
      "country": "{persona_attributes['country']}",
      "age": "{persona_attributes['age']}",
      "comments": "{persona_attributes['comments']}"
    }}

    Our product's description is : {product_description}

    Each key of the following json should contain at least 3 sentences.THe keys are as follows:
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

    persona = transform_to_json(response_text)
    print(persona)
    persona = re.sub(r"(')(?=\w+:)|(?<=: )(')", '"', persona)
    persona = json.loads(persona)

    if "Name" not in persona.keys():
        print("Name key not found")
        persona = add_name_of_persona(persona=persona)

    # if persona does not contain all the keys, call the function again
    if len(persona.keys()) < 6:
        print("CALLING CREATE PERSONA AGAIN !!")
        MAX_RETRIES = MAX_RETRIES - 1
        print(f""" Retries left : {MAX_RETRIES}""")
        return create_persona_with_LLM(persona_attributes, product_category, product_description)
    else:
        print("PERSONA CREATED SUCCESSFULLY")
        print(persona)
        return json.dumps(persona)

def transform_to_json(input_str):
    json_prompt = f"""Convert the following into proper json containing 6 keys \n {input_str}.
    Do not add any other information."""
    response = call_gpt(role="user", full_prompt=json_prompt)
    json_response = response.choices[0].message.content
    json_response = re.sub(r"[\`\n\t]", "", json_response).replace("json", "")
    print(f"""This will be converted to json \n {json_response}""")
    json_response = json.loads(json_response)

    expected_keys = [
        "Name",
        "The struggles and pains of the persona",
        "The other products the persona thinks about",
        "The goals of the persona",
        "The benefits of our product for the persona",
        "Marketing tagline for the persona"
    ]

    expected_json = {}

    #for every key in the response find the closest value from expected keys
    for key in json_response.keys():
        closest_key_prompt = f"""Find the closest value for {key} from items below.

        The struggles and pains of the persona
        Name
        The other products the persona thinks about
        The goals of the persona
        The benefits of our product for the persona
        Marketing tagline for the persona

        Write only one value from the list. Do not add any other information"""

        closest_key_response = call_gpt(role="user", full_prompt=closest_key_prompt)
        closest_key = closest_key_response.choices[0].message.content
        if closest_key in expected_keys:
            expected_json[closest_key] = json_response[key]
        else:
            print(f"""json Key : {key} \n Closest Key : {closest_key} """)

    return json.dumps(expected_json)

def add_name_of_persona(persona):
    name_prompt = f"""Write the name of the person fron the following information. Do not add any other information.

    {persona}
    """

    name_response = call_gpt(role="user", full_prompt=name_prompt)
    name = name_response.choices[0].message.content
    persona["Name"] = name
    persona = json.dumps(persona) #convert to string
    persona = re.sub(r"(')(?=\w+:)|(?<=: )(')", '"', persona) # fix the single quotes issues
    return persona.loads(persona)



if __name__ == '__main__':
    persona_attributes = {
        'gender' : 'female',
        'country' : 'USA',
        'age' : '25',
        'comments' : 'student, loves to travel'
    }
    product_category = 'shoes'
    product_description = 'A pair of shoes that are comfortable and stylish'
    create_persona_with_LLM(persona_attributes, product_category, product_description)
