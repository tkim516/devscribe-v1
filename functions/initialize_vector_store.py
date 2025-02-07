from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
import os

def initialize_vector_store(index_name: str):
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-large",
        openai_api_key=os.environ.get("OPENAI_API_KEY")
    )

    pc = Pinecone(api_key=os.environ.get('PINECONE_API_KEY'))
    index_name = index_name
    index = pc.Index(index_name)
    vector_store = PineconeVectorStore(embedding=embeddings, index=index)
   
    return vector_store