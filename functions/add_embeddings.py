from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from langchain_community.document_loaders import PyPDFLoader
from tempfile import NamedTemporaryFile
from langchain.schema import Document  # Import the Document class
import os
import streamlit as st

def add_pdf_to_vector_store(uploaded_file):
  embeddings = OpenAIEmbeddings(
      model="text-embedding-3-large",
      openai_api_key=os.environ.get("OPENAI_API_KEY")
  )

  pc = Pinecone(api_key=os.environ.get('PINECONE_API_KEY'))
  index_name = "devscribe-pdfs"
  index = pc.Index(index_name)

  vector_store = PineconeVectorStore(embedding=embeddings, index=index)

  with NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.getbuffer())
        temp_file_path = temp_file.name

  try:
        # Use the temporary file path with PyPDFLoader
        loader = PyPDFLoader(temp_file_path)
        pages = []
        for page in loader.lazy_load():
            pages.append(page)

        # Split the PDF into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2500,
            chunk_overlap=500,
            add_start_index=True
        )
        all_splits = text_splitter.split_documents(pages)

        # Convert splits into Document objects
        documents = [
            Document(page_content=split.page_content, metadata={"chunk_index": i})
            for i, split in enumerate(all_splits)
        ]

        with st.expander("Show Chunked Document"):
          st.write(documents)

        _ = vector_store.add_documents(documents=documents)

        return vector_store
  
  finally:
        # Clean up: delete the temporary file
        os.remove(temp_file_path)

