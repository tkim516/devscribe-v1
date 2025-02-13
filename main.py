from functions.cloneRepo import clone_repo
from functions.parseRepo import parse_repo
from functions.getEmbeddings import add_file_contents_to_db

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

def write_section_api_test(llm, instructions: str):

  llm = ChatOpenAI(model="gpt-4o-mini")
  
  prompt = PromptTemplate(
      input_variables=['instructions'],
      template="""
      You are an assistant that writes documentation for software projects.

      Instructions:
      {instructions}
    
      """
      )
  message = prompt.invoke({'instructions': instructions})
  response = llm.invoke(message)

  return response.content

