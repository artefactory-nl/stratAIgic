import streamlit as st
from generate_persona import generate_persona
from generate_marketing_mix import generate_marketing_mix

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
    unique_selling_points = st.text_area("Unique Selling Points", key="usp")
    target_audience = st.text_input("Target Audience", key="target_audience")
    region = st.selectbox("Region", ["North America", "Europe", "Asia", "South America", "Australia"], key="region")
    marketing_goals = st.text_input("Marketing Goals", key="marketing_goals")
    budget_range = st.slider("Budget Range in EUR", 10000, 100000, (20000, 50000), key="budget_range")
    submit_button = st.button("Create Persona")

    if submit_button:
        with st.spinner('Processing Strategy...'):

            business_attributes = {
            "product_name": product_name,
            "product_description": product_description,
            "unique_selling_points": unique_selling_points,
            "target_audience": target_audience,
            "region": region,
            "marketing_goals": marketing_goals,
            "budget_range": budget_range,
        }
            st.session_state['business_attributes'] = business_attributes
            strategy = generate_marketing_mix(business_attributes=business_attributes)
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
        st.success('Your marketing Startegy is being generated')
        st.session_state['persona'] = persona
        st.session_state["persona_submitted"] = True

def final_page():
    st.title("Generated marketing strategy")
    st.subheader("Product details")
    product_details = st.session_state['business_attributes']
    st.table(product_details)
    # st.write(f"Product Name: {product_details['product_name']}")
    # st.write(f"Product Description: {product_details['product_description']}")
    # st.write(f"Unique Selling Points: {product_details['unique_selling_points']}")
    # st.write(f"Target Audience: {product_details['target_audience']}")
    # st.write(f"Region: {product_details['region']}")
    # st.write(f"Marketing Goals: {product_details['marketing_goals']}")
    # st.write(f"Budget Range: {product_details['budget_range']}")

    st.subheader("Persona details")
    persona = st.session_state['persona']
    st.table(persona)
    # st.write(f"Name: {persona['Name']}")
    # st.write(f"Marketing tagline for the persona: {persona['Marketing tagline for the persona']}")
    # st.write(f"The struggles and pains of the persona: {persona['The struggles and pains of the persona']}")
    # st.write(f"The other products the persona thinks about: {persona['The other products the persona thinks about']}")
    # st.write(f"The goals of the persona: {persona['The goals of the persona']}")
    # st.write(f"The benefits of our product for the persona: {persona['The benefits of our product for the persona']}")
    
    st.subheader("Strategy")
    st.write(".....")


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
