# app.py (Streamlit UI)
import streamlit as st
from coding_agent import coding_agent

st.title("🤖 Python Coding Assistant")
st.caption("Powered by Hugging Face smolagents")

code_input = st.text_area("Enter your Python code:", height=200)
task = st.selectbox("Select task:", ["Suggest Improvements", "Debug", "Generate Docs", "Format Code"])

if st.button("Execute"):
    with st.spinner("Agent is working..."):
        response = coding_agent.run(
            f"{task} for this code: {code_input}",
            display=True
        )
        st.code(response, language="python")
