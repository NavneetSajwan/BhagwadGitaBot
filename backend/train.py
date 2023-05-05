import os
from dotenv import load_dotenv

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
from langchain import OpenAI

# Load environment variables from .env file
load_dotenv()

DATA_DIR = os.environ.get('DATA_DIR')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

def create_index(path):
    max_input = 4096
    tokens = 200
    chunk_size = 600 # for LLM, we need to define chunk size
    max_chunk_overlap = 20
    
    # Define prompt
    prompt_helper = PromptHelper(max_input, tokens, max_chunk_overlap, chunk_size_limit=chunk_size)
    
    # Define LLM
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-ada-001", max_tokens=tokens))
    
    # Load data
    docs = SimpleDirectoryReader(path).load_data()
    
    return prompt_helper, llm_predictor, docs



# Create the index
prompt_helper, llm_predictor, docs = create_index(path=DATA_DIR)

# Create the vector index
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)
vector_index = GPTVectorStoreIndex.from_documents(documents=docs, service_context=service_context)
vector_index.storage_context.persist(persist_dir='Store')

