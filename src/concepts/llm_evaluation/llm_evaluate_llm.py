import os
import giskard.llm
import giskard.llm.embeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import pandas as pd
import giskard
from giskard.rag import KnowledgeBase, generate_testset
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from giskard.llm.embeddings import set_default_embedding

from dotenv import load_dotenv
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# model_name = "BAAI/bge-small-en"
# model_kwargs = {"device": "cpu"}
# encode_kwargs = {"normalize_embeddings": True}
# bge_embeddings = HuggingFaceBgeEmbeddings(
#     model_name=model_name, model_kwargs=model_kwargs, encode_kwargs=encode_kwargs
# )

import google.generativeai as genai
from giskard.llm.client.gemini import GeminiClient
genai.configure(api_key=GEMINI_API_KEY)
giskard.llm.set_default_client(GeminiClient())
# giskard.llm.embeddings.set_default_embedding(bge_embeddings)


URLs = [
    'https://medium.com/data-science-at-microsoft/evaluating-llm-systems-metrics-challenges-and-best-practices-664ac25be7e5',
    'https://towardsdatascience.com/how-to-evaluate-rag-if-you-dont-have-ground-truth-data-590697061d89',
    'https://medium.com/@celaguleiva/good-questions-lead-to-great-answers-metrics-for-using-rag-with-cosine-similarity-and-maximal-a7cdbcb15e54'

        ]

loader = WebBaseLoader(URLs)
documents = loader.load()


text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=10,
        length_function=len
    )
chunks = text_splitter.split_documents(documents)
print('chunks - ', len(chunks))

## save data in a pandas dataframe

df = pd.DataFrame([chunk.page_content for chunk in chunks], columns=['text'])
print(df.head())

## Create a KnowledgeBase
knowledge_base = KnowledgeBase(df)

## Generate test set
testset = generate_testset(
    knowledge_base,
    num_questions=10,
    language='en',
    agent_description='A chatbot answering questions about LLM evaluation techniques'
)


# Save the generated testset
testset.save("my_testset.jsonl")

# You can easily load it back
from giskard.rag import QATestset

loaded_testset = QATestset.load("my_testset.jsonl")

# Convert it to a pandas dataframe
df_questions = loaded_testset.to_pandas()
print(df_questions.head())