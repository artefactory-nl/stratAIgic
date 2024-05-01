import streamlit as st
from generate_persona import generate_persona
from generate_marketing_mix import generate_marketing_mix
import json

def generate_strategy(product_name, product_description, unique_selling_points, target_audience, region, marketing_goals, budget_range):
    return f"""
    **Marketing Strategy for {product_name}**

    **Target Audience**: {target_audience}
    **Region**: {region}
    **Budget**: {budget_range}

    **1. Recommended Marketing Channels:**
    - Online: Targeted social media ads, influencer partnerships
    - Offline: Local events, retail partnerships

    **2. Considered But Unsuitable Strategies:**
    - Mass Email Marketing: Due to low engagement rates.
    - Billboard Advertising: Not effective for targeted demographic.

    **3. Timeline and Milestones:**
    - Month 1-3: Social media campaign and influencer outreach.
    - Month 4-6: Evaluate campaign effectiveness and adjust.

    **4. Expected Outcomes:**
    - Increase brand awareness by 30%.
    - Achieve a market penetration of 5% within the first year.
    """

def main_page():
    st.title("StratAIgic: an AI-Powered Marketing Strategy Generator")
    st.subheader("Enter Product and Market Details")
    product_name = st.text_input("Product Name", key="product_name")
    product_description = st.text_area("Product Description", key="product_description")
    product_category = st.text_area("Product Category", key="product_category")
    product_stage = st.text_area("Product Stage", key="product_stage")
    target_audience = st.text_input("Target Audience", key="target_audience")
    region = st.selectbox("Region", ["North America", "Europe", "Asia", "South America", "Australia"], key="region")
    product_pricing = st.text_input("Product Pricing", key="product_pricing")
    submit_button = st.button("Create Persona")

    if submit_button:
        with st.spinner('Processing Strategy...'):

            business_attributes = {
            "product_name": product_name,
            "product_description": product_description,
            "product_category": product_category,
            "product_stage": product_stage,
            "target_audience": target_audience,
            "region": region,
            "product_pricing": product_pricing
        }
            st.session_state['business_attributes'] = business_attributes
            strategy = generate_marketing_mix(product_attributes=business_attributes)
            st.session_state['strategy'] = strategy

        st.success('Your marketing Startegy is being generated')
        st.session_state["strategy_generated"] = True
        st.experimental_rerun()
    
def persona_page():
    st.title("User Persona Information")
    gender = st.selectbox("Gender", ["Male", "Female", "Non-binary", "Prefer not to say"], key="gender")
    country = st.text_input("Country", key="country")
    age = st.slider("Age", 18, 100, 25, key="age")
    comments = st.text_area("Comments", key="comments")
    submit_button = st.button("Submit Persona Details")

    if submit_button:
        with st.spinner('Processing Persona...'):

            perosna_attributes = {
            "gender": gender,
            "country": country,
            "age": age,
            "comments": comments
        }

            business_attributes = st.session_state['business_attributes']
            persona = generate_persona(business_attributes, persona_attributes=perosna_attributes)
            st.session_state['persona'] = persona

        st.success('Your Persona is being generated')
        st.session_state["persona_submitted"] = True
        st.experimental_rerun()

def final_page():
    st.title("Generated marketing strategy")
    st.subheader("Product details")
    product_details = st.session_state['business_attributes']
    st.table(product_details)

    st.subheader("Persona details")
    persona = st.session_state['persona']
    try:
        st.write(f"Name: {persona['Name']}")
        st.write(f"Marketing tagline for the persona: {persona['Marketing tagline for the persona']}")
        st.write(f"The struggles and pains of the persona: {persona['The struggles and pains of the persona']}")
        st.write(f"The other products the persona thinks about: {persona['The other products the persona thinks about']}")
        st.write(f"The goals of the persona: {persona['The goals of the persona']}")
        st.write(f"The benefits of our product for the persona: {persona['The benefits of our product for the persona']}")
    except:
        persona_json = json.dumps(persona, indent=4)
        st.code(persona_json, language='json')
    
    st.subheader("Strategy")
    st.write(st.session_state['strategy'])


# Display the logo in the sidebar
logo_path = r"../lib/StratAIgic.png"
st.sidebar.image(logo_path, width=100)
st.sidebar.header("Generated Marketing Strategy")

# Setup pages
if "strategy_generated" not in st.session_state:
    main_page()
elif "persona_submitted" not in st.session_state:
    persona_page()
else:
    final_page()
