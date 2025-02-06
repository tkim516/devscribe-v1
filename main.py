from functions.cloneRepo import clone_repo
from functions.parseRepo import parse_repo
from functions.getEmbeddings import add_file_contents_to_db

target_repo = clone_repo('https://github.com/tkim516/ml_homerun_predictor')
parsed_repo = parse_repo(target_repo)

print(target_repo)
print(len(target_repo))

db = add_file_contents_to_db(parsed_repo)
print(db)

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate



def get_response_from_query(vector_store, query, k=4):
  retrieved_docs = vector_store.similarity_search(query, k=k)
  retrieved_content = "\n\n".join(doc.page_content for doc in retrieved_docs)

  llm = ChatOpenAI(model="gpt-4o-mini")

  prompt = PromptTemplate(
    input_variables=['context'],
    template="""
    You are an assistant that writes documentation for GitHub repositories.

    Write documentation based on this source code: {context}
    """
  )

  message = prompt.invoke({
    'question': query,
    'context': retrieved_content})
  
  response = llm.invoke(message)

  return response

print(get_response_from_query(db, 'what is the purpose of this repository'))
