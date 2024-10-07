from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import retrieval_qa
from langchain_community.vectorstores import FAISS
import os
from pathlib import Path
from langchain_community.embeddings import HuggingFaceBgeEmbeddings


PROJECT_PATH = Path(__file__,).parent.parent.parent.parent
DATA_PATH = os.path.join(PROJECT_PATH, 'data')
text_file = os.path.join(DATA_PATH, 'nvda_news_1.txt')

#### STEP-1 : Load the text from the file
documents = TextLoader(text_file).load()


#### STEP-2 : Split the text into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=10,
    length_function=len
)
chunks = text_splitter.split_documents(documents)
print(f"Number of chunks: {len(chunks)}")


#### STEP-3 : Create embedinngs for each chunk
model_name = "BAAI/bge-small-en"
model_kwargs = {"device": "cpu"}
encode_kwargs = {"normalize_embeddings": True}
bge_embeddings = HuggingFaceBgeEmbeddings(
    model_name=model_name, model_kwargs=model_kwargs, encode_kwargs=encode_kwargs
)

#### STEP-4 : Create a vector store for efficient similarity search
knowledge_base = FAISS.from_documents(chunks, bge_embeddings)
query1 = "what is daily loss of the nvidia stock?"

# # STEP-5 : Perform similarity search and retrieve relevant documents
query1_response = knowledge_base.similarity_search(query1)
# print('query1_response - ', query1_response[0].page_content)

# # STEP-6 : Retrieve similarity scores for each document
similarity_score = knowledge_base.similarity_search_with_score(query1)
print('query1_response_with_score - ', similarity_score)



# # STEP-4 : Create a chain to answer questions

# qa_chain = retrieval_qa.Chain.from_llm(
#     bge_embeddings,
#     retriever=knowledge_base.as_retriever(),
#     chain_type="simple_chain",
# )

# answer1 = qa_chain.invoke(query1)






