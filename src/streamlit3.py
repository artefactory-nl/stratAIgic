import streamlit as st
st.write(st.secrets["OPENAI_API_KEY"])

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
    st.write(st.secrets["OPENAI_API_KEY"])
    product_name = st.text_input("Product Name", key="product_name")
    product_description = st.text_area("Product Description", key="product_description")
    product_category = st.text_area("Product Category", key="product_category")
    product_stage = st.text_area("Product Stage", key="product_stage")
    target_audience = st.text_input("Target Audience", key="target_audience")
    region = st.selectbox("Region", ["North America", "Europe", "Asia", "South America", "Australia"], key="region")
    product_pricing = st.text_input("Product Pricing", key="product_pricing")
    submit_button = st.button("Next")

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
    submit_button = st.button("Generate Persona and Marketing Strategy")

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
            st.session_state["persona_attributes"] = perosna_attributes

        st.success('Your Persona is being generated')
        st.session_state["persona_submitted"] = True
        st.experimental_rerun()

# Function to display the final marketing page
def final_page():
    # Set the title of the page
    st.title("Generated marketing strategy 🚀")

    # Create 2 columns layout for better organization
    card_col, dataframes_col = st.columns(2)

    # Add blank spaces
    dataframes_col.markdown("#")
    dataframes_col.markdown("##")

    # Retrieve product details from session state and display in a dataframe
    product_details = st.session_state['business_attributes']
    dataframes_col.dataframe(
        product_details,
        column_config={"": "Product Details", "value": ""},
        use_container_width=True
    )

    # # Placeholder for similar products, to be filled with AI response
    # similar_products = {} # TODO: Get the similar products as LLM response

    # # Display similar products in a dataframe
    # dataframes_col.dataframe(
    #     similar_products,
    #     column_config={"": "Similar Products - AI powered", "value": ""},
    #     use_container_width=True
    # )

    # Add tabs for persona and strategy sections
    persona_tab, strategy_tab = card_col.tabs(["Persona - AI Generated", "Marketing Startegy - AI Generated"])

    # Display persona information
    with persona_tab:
        # Retrieve persona data and parse JSON
        persona = st.session_state["persona"]
        persona_attributes = st.session_state["persona_attributes"]
        persona_data = json.loads(persona)
        img_col, description_col = st.columns(2)

        # Display persona image (placeholder for now)
        persona_image = r"../lib/persona_image.png" # created using OpenArt LLM
        img_col.image(persona_image, use_column_width=True) # TODO: add image generated by LLM

        # Display persona details
        try:
            description_col.write(f"""{persona_data["Name"]}""")
            if len(persona_data["Name"]) < 40:
                description_col.write(f"""Gender: {persona_attributes["gender"]}""")
                description_col.write(f"""Country: {persona_attributes["country"]}""")
                description_col.write(f"""Age: {persona_attributes["age"]}""")
            with st.expander("Marketing tagline", expanded=False):
                st.write(persona_data['Marketing tagline for the persona'])
            with st.expander("Struggles and pains", expanded=False):
                st.write(persona_data['The struggles and pains of the persona'])
            with st.expander("Other products they think about", expanded=False):
                st.write(persona_data['The other products the persona thinks about'])
            with st.expander("Goals", expanded=False):
                st.write(persona_data['The goals of the persona'])
            with st.expander("Benefits of our product", expanded=False):
                st.write(persona_data['The benefits of our product for the persona'])
        except:
            # If data is not structured as expected, display each key-value pair
            description_col.write(persona_data[0])
            for persona_dat_key in list(persona_data.keys())[1:]:
                with st.expander(persona_dat_key, expanded=False):
                    st.write(persona_data[persona_dat_key])
            st.warning("Bad JSON format!")

    # Display marketing strategy
    with strategy_tab:
        # Retrieve strategy data from session state
        strategy_data = st.session_state['strategy']
        emojis = ["✅", "🤔", "❌", "📝"]

        # Iterate over suggestion types and display strategy details
        for i, suggestion_type in enumerate(strategy_data):
            if suggestion_type != "Other options":
                st.write(f"{emojis[i]} **{suggestion_type}**:")
                for channel in strategy_data[suggestion_type]:
                    channel_name= channel[0]
                    channel_motivation = channel[1]
                    with st.expander(channel_name, expanded=False):
                        st.write(channel_motivation)
            else:
                # Display other options if available
                st.write(f"{emojis[-1]} **{suggestion_type}**:")
                st.write(strategy_data[suggestion_type])


# Set wide mode for the page layout
st.set_page_config(layout="wide")

# Display the logo in the sidebar
logo_path = r"lib/StratAIgic.png"
st.sidebar.image(logo_path, use_column_width=True)
st.sidebar.header("Unleash AI, Conquer Markets")

# Setup pages
if "strategy_generated" not in st.session_state:
    main_page()
elif "persona_submitted" not in st.session_state:
    persona_page()
else:
    final_page()
