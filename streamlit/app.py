import streamlit as st
import time
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
parser = StrOutputParser()
from langchain_groq import ChatGroq
import os
api_key = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="llama3-8b-8192", api_key=api_key)
st.title('ReciteAI')
st.header('Enter text to complete:')

user_input = st.text_area('Write the description of story', height=200)
max_length = st.slider("Select max story length:", min_value=50, max_value=200, value=100, step=10)
num_sequences = st.selectbox("Select number of stories to generate:", options=[1, 2, 3], index=0)

if st.button('Generate Story'):
    with st.spinner('Generating Story...'):
        messages = [
          SystemMessage(content="You're an author"),
          HumanMessage(content=f"Write {num_sequences} number of stories of {max_length} sentences for {user_input}"),
                  ]
        response = parser.invoke(model.invoke(messages))
        st.write(response)
        st.markdown("---")

st.sidebar.markdown("## Guide")
st.sidebar.info("This tool uses GroQ inferencing to generate a story of your provided text. Adjust the sliders to change the story length and number of stories generated. The model is optimized for short to medium length paragraphs.")
st.sidebar.info("By Soham Mhatre")
st.sidebar.markdown("### Examples")
st.sidebar.write("1. Paste a beginning to see how the AI completes it.")
st.sidebar.write("2. Try different settings to see how the story changes.")
