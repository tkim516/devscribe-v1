from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec
from langchain.schema import Document
from dotenv import load_dotenv
import os

def add_file_contents_to_db(files_dict):
  embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

  pc = Pinecone(api_key=os.environ.get('PINECONE_API_KEY'))
  index_name = "repo-embeddings"
  index = pc.Index(index_name)
  vector_store = PineconeVectorStore(embedding=embeddings, index=index)

  text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True
    )
  
  # Process and add file contents to the vector store
  for file_path, file_content in files_dict.items():
        # Convert file content to Document objects with metadata
        document = [Document(page_content=file_content, metadata={"file_path": file_path})]
        
        # Split the file content into chunks
        all_splits = text_splitter.split_documents(document)
        
        # Add the chunks to the vector store
        _ = vector_store.add_documents(documents=all_splits)
    
  return vector_store