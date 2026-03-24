import streamlit as st # type: ignore
from models import gemini_llm


st.title("Welcome to Gemini LLm Application")
st.subheader("practice llm")

user_input = st.text_area(
    "Enter your prompt",
    placeholder ="what is an animal?"3
)

if st.button("Send prompt"):
    if user_input.strip()=="":
        st.warning("Enter valid prompt.")
    else:
        with st.spinner("Generating content...."):
            answer= gemini_llm(user_input)
            st.success("Generated content...")
            st.write(answer)
