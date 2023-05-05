from llama_index import (
    SimpleDirectoryReader,
    GPTListIndex,
    GPTVectorStoreIndex,
    LLMPredictor,
    PromptHelper,
    ServiceContext,
    StorageContext,
    load_index_from_storage
)

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DATA_DIR = os.environ.get('DATA_DIR')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
STORE = os.environ.get('STORE')
def answer_me(question):
    storage_context = StorageContext.from_defaults(persist_dir=STORE)
    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine()
    response = query_engine.query(question)
    return response


# Answer a question using the index
# response = answer_me("but what did Krishna tell Arjuna abour Karma?")
# print(response)

# response = answer_me("How to act in the mode of goodness?")
# print(response)
