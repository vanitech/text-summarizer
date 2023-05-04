import openai
import streamlit as st

def summarize(prompt):
    augmented_prompt = f"summarize this text: {prompt}"
    try:
        st.session_state["summary"] = openai.Completion.create(
            model="text-davinci-003",
            prompt=augmented_prompt,
            temperature=.5, # temperature parameter is set between 0 (less random) to 2 (more random)
            max_tokens=1000, # token count of the prompt plus max_tokens cannot exceed the model's context length (4096 for davinci-003)
        )["choices"][0]["text"]
    except:
        st.write('There was an error =(')
