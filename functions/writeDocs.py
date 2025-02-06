from functions.cloneRepo import clone_repo
from functions.parseRepo import parse_repo
from functions.getEmbeddings import add_file_contents_to_db

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

def write_docs(context, prompt_instructions):

  llm = ChatOpenAI(model="gpt-4o-mini")
  if prompt_instructions:
    prompt = PromptTemplate(
      input_variables=['context', 'prompt_instructions'],
      template="""
      You are an assistant that writes documentation for GitHub repositories.

      Write documentation based on this source code: {context}
      Use these instructions when writing the documentation: {prompt_instructions}
      """
    )
    
    message = prompt.invoke({'context': context, 'prompt_instructions': prompt_instructions})


  else:
    prompt = PromptTemplate(
      input_variables=['context'],
      template="""
      You are an assistant that writes documentation for GitHub repositories.

      Write documentation based on this source code: {context}
      """
    )

    message = prompt.invoke({'context': context})
  
  response = llm.invoke(message)

  return response