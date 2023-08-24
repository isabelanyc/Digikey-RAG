import os
from dotenv import load_dotenv
from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma


# load all the pdfs in the data directory
# type of loader is the UnstructuredPDFLoader
loader = DirectoryLoader('data', glob="**/*.pdf", loader_cls=UnstructuredPDFLoader, show_progress=True)

# create a text splitter and chunk up the documents
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 10000,
    chunk_overlap  = 1000,
    length_function = len,
    add_start_index = True,
)
docs = loader.load_and_split(text_splitter)

num_docs = len(docs)
print(f'Number of docs: {num_docs}')

# Use Chroma to create the embdeddings and create the vector store
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
db = Chroma.from_documents(docs, OpenAIEmbeddings())

# test with a similarity search
query = input("Query: ")
similar_docs = db.similarity_search(query)
similar_page_content = [similar_docs[i].page_content for i in range(len(similar_docs))]
print(similar_docs)

