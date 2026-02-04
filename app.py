import streamlit as st
import google.generativeai as genai

# Direct Key setup for quick fix
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
                # Correct way to call the model
                model = genai.GenerativeModel('gemini-1.5-flash')
                res = model.generate_content(f"Act as a professional civil engineer. Answer in English and Tamil: {query}")
                st.success(res.text)
            except Exception as e:
                st.error(f"Error: {e}")

with tab2:
    st.header("Elevation & 3D Design")
    prompt = st.text_area("Ex: Modern house with wood and glass exterior, 2 floors")
    if st.button("Generate Design"):
        if prompt:
            # Image generation (Always works independently)
            image_url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}?width=1024&height=1024&seed=42&nologo=true"
            st.image(image_url, caption="Your Generated Design")

