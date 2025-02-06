import streamlit as st
from functions.check_api import check_openai_api_key
from functions.writeDocs import write_docs
from functions.cloneRepo import clone_repo
from functions.parseRepo import parse_repo
import os

# Page configuration
st.set_page_config(page_title="Settings", layout="wide")

st.image('design_resources/logo-white.svg', width=400)

# Check if API key is stored in session state
check_openai_api_key(st.session_state)

# Choose models
st.subheader('Model Selection')

llm_model = st.selectbox('Select LLM', ['gpt-4o-mini', 'gpt-3.5-turbo'])

embedding_model = st.selectbox('Select Embedding Model', ['text-embedding-3-small', 'text-embedding-3-large'])