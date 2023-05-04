# Initialize the streamlit app to create a simple text box interface for text input and output summary
import streamlit as st
import openai
import os
from functions import summarize

st.title("Text Summarizer")

try:
  openai.api_key = os.getenv('OPENAI_KEY') # set key per instructions available at https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety 
  assert openai.api_key , "missing key"
  # initialize state variable 
  if "summary" not in st.session_state:
        st.session_state["summary"] = ""
    
  # define text input area for the streamlit app 
  input_text = st.text_area(label="Enter full text:", value="", height=250)
  st.button(
        "Submit",
        on_click=summarize,
        kwargs={"prompt": input_text},
    )
   
  # define text output area for the streamlit app 
  output_text = st.text_area(label="Summarized text:", value=st.session_state["summary"], height=250)
except:
  st.write('There was an error =')
