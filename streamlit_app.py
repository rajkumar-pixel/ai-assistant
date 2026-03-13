import streamlit as st
from src.assistant import assistant
st.set_page_config(
page_title="BFSI AI Assistant",
page_icon="🤖"
)

st.title("BFSI AI Banking Assistant")
st.write("Ask your banking questions")

query=st.text_input("Enter your question:")
if st.button("Ask"):
    if query:
        response=assistant(query)
        st.success(response)
    else:
        st.warning("Please enter a question")