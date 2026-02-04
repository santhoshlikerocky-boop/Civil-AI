import streamlit as st
import google.generativeai as genai

# Direct Key setup
GEMINI_KEY = "AIzaSyDPpONsYV2lTJw35wr8ZyHewj6p72-LYq4"
genai.configure(api_key=GEMINI_KEY)

st.set_page_config(page_title="Civil AI Pro", layout="wide")
st.title("🏗️ Civil AI Builder")

tab1, tab2 = st.tabs(["💬 Civil Chatbot", "🖼️ 3D Elevation"])

with tab1:
    st.header("Civil Q&A Assistant")
    query = st.text_input("Enna சந்தேகம்? (Ex: M20 concrete ratio?)", key="civil_query")
    if st.button("Ask Expert"):
        if query:
            try:
                # Force using v1 version to avoid 404 error
                model = genai.GenerativeModel(model_name='gemini-1.5-flash')
                res = model.generate_content(f"Act as a professional civil engineer. Answer in English and Tamil: {query}")
                st.success(res.text)
            except Exception as e:
                st.error(f"Error: {e}")

with tab2:
    st.header("Elevation & 3D Design")
    # Cleaned up prompt handling
    design_prompt = st.text_area("Ex: Modern house design, 2 floors")
    if st.button("Generate Design"):
        if design_prompt:
            encoded_prompt = design_prompt.replace(" ", "%20")
            image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"
            st.image(image_url, caption="Your Generated Design")
