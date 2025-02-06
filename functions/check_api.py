import openai
import streamlit as st
import time
import os

def check_openai_api_key(session_state):
  if 'OPENAI_API_KEY' in os.environ:
    st.session_state['OPENAI_API_KEY'] = os.environ['OPENAI_API_KEY']

  elif 'OPENAI_API_KEY' not in session_state:
    st.session_state['OPENAI_API_KEY'] = None
  
  def validate_key(user_api_key):
    client = openai.OpenAI(api_key=user_api_key)
    try:
        client.models.list()
    except openai.AuthenticationError:
        return False
    else:
        return True
  
  if st.session_state['OPENAI_API_KEY'] is None:
    open_api_key = st.text_area('Enter your OpenAI API Key')
    submit_button = st.button('Submit')
    
    if submit_button and open_api_key:

      if validate_key(open_api_key):
          st.session_state['OPENAI_API_KEY'] = open_api_key
          os.environ['OPENAI_API_KEY'] = st.session_state['OPENAI_API_KEY']
          st.success("API key successfully stored!")
          time.sleep(1)
          st.rerun()

      else:
          st.error("Invalid OpenAI API Key. Please try again.")

  else:
      st.subheader("OpenAI API")
      st.write(f"Using Key: {st.session_state['OPENAI_API_KEY'][0:10]}......")