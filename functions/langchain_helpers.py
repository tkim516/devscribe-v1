from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

def write_docs(source_code, api_spec):

  llm = ChatOpenAI(model="gpt-4o-mini")
  prompt = PromptTemplate(
    input_variables=['source_code', 'api_spec'],
    template="""
      You are an assistant that writes documentation APIs.

      Explain the purpose of the API and it's functionality.
       
      Here is the source code for the API: {source_code}

      Here is the OpenAPI specification for the API: {api_spec}
      """
  )
    
  message = prompt.invoke({'source_code': source_code, 'api_spec': api_spec})
  response = llm.invoke(message)

  return response