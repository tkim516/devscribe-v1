import streamlit as st
from functions.check_api import check_openai_api_key
from functions.writeDocs import write_docs
from functions.cloneRepo import clone_repo
from functions.parseRepo import parse_repo
import os
from functions.add_embeddings import add_pdf_to_vector_store
from functions.initialize_vector_store import initialize_vector_store

# Page configuration
st.set_page_config(page_title="DevScribe", layout="wide")

st.image('design_resources/logo-white.svg', width=400)

st.write("")

pdf_vector_store = initialize_vector_store("devscribe-pdfs")
repo_vector_store = initialize_vector_store("devscribe-repos")

pdf_file = st.file_uploader("Upload a PDF", type=['pdf'])
pdf_submit = st.button('Submit')

if pdf_file and pdf_submit:
    vector_store = add_pdf_to_vector_store(pdf_file)
    st.write(vector_store)



# Initialize session state for target_repo
if 'target_repo' not in st.session_state:
    st.session_state['target_repo'] = ''

# Form for input
with st.form("input_form"):
    target_repo = st.text_input('Target Repo', value='https://github.com/tkim516/ml_homerun_predictor')
    
    file_types = st.multiselect('File Types', ['py', 'ipynb', 'java', 'js', 'ts', 'html', 'css', 'sql', 'json', 'xml', 'yaml', 'md', 'txt'])

    prompt_instructions = st.text_area('Input Prompt', value='Include information about potential improvements to the codebase.')
    
    repo_submit_button = st.form_submit_button('Submit')

    if repo_submit_button:
        st.session_state['target_repo'] = target_repo

# Use session state
if st.session_state['target_repo']:
    target_repo = clone_repo(st.session_state['target_repo'])

    st.write(file_types)

    parsed_repo = parse_repo(target_repo, file_types)
    st.write(parsed_repo)
    
    # Combine all file contexts
    for file, content in parsed_repo.items():
        context = f"File: {file}\nContent:\n{content}"

        # Append input_prompt to base prompt and generate documentation

        response = write_docs(context, prompt_instructions)
        st.write(response.content)
        st.write(response)
    st.header('Target Repo')
    st.write(st.session_state['target_repo'])