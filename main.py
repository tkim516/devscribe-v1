import streamlit as st
from functions.git_helpers import extract_github_file
from functions.flask_parser import generate_openapi_spec
from functions.langchain_helpers import write_docs
from dotenv import load_dotenv
from io import BytesIO
import json
import os

st.set_page_config(layout="wide")
st.image("/Users/tyler/Downloads/ML/devscribe/design_resources/logo-white.svg", width=200)

# Load environment variables from .env file
load_dotenv()
github_token = os.getenv("GITHUB_TOKEN")

owner = st.text_input("Repository owner", value="tkim516")
repo = st.text_input("Repository name", value="devscribe-example-apis")
file_path = st.text_input("File path", value="flask_api.py")
submit = st.button("Generate")

if submit:
  file_obj = extract_github_file(owner, repo, file_path, github_token)
  #st.write(file_obj.read().decode())  # Read and print file contents

  source_code = file_obj.read()

  file_obj = BytesIO(source_code)
  openapi_spec = generate_openapi_spec(file_obj)
  response = write_docs(source_code, openapi_spec)


  col1, col2 = st.columns(2)
  
  with col1:
    st.write(response.content)

  with col2:
    st.header("Definition")
    st.json(openapi_spec)