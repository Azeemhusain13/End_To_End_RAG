#Reading the Text file
from langchain_community.document_loaders import TextLoader
loader = TextLoader('/Users/admin/Desktop/practise/python/LangChain/Data ingestion/speech.txt')
doc = loader.load()
print("First document:", doc[0])

#Reading the PDF file
print("-------------------------------")
from langchain_community.document_loaders import PyPDFLoader
filepath = '/Users/admin/Desktop/practise/python/LangChain/Data ingestion/sample.pdf'
loader = PyPDFLoader(filepath)
doc1 = loader.load()
print("First document:", doc1[0])

#Reading the Web Based loader
print("-------------------------------")
from langchain_community.document_loaders import WebBaseLoader
import bs4
bs_kwargs = dict(
    parse_only=bs4.SoupStrainer(
        class_=("mw-page-title-main")
    )
)

loader = WebBaseLoader('https://en.wikipedia.org/wiki/Artificial_intelligence', bs_kwargs=bs_kwargs)
doc = loader.load()
print("First document:", doc[0])

#Text Splitter
print("-------------------------------")
from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
splits=text_splitter.split_text(doc1[0].page_content)
print("Number of splits:", len(splits))

#Embeddings (Tex into vector)
print("-------------------------------")
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["OPEN_API_KEY"] = os.getenv("OPEN_API_KEY")

from langchain_openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
embeddings
embed = embeddings.embed_query("What is Artificial Intelligence?")
print("Embedding vector:", embed)

#Store in Vector Database (ChromaDB)
print("-------------------------------")
from langchain_chroma import Chroma
db = Chroma.from_documents(splits, embeddings)

query = "What is Artificial Intelligence?"
results = db.similarity_search(query, k=2)
print("Search results:", results)


#embedding using ollama
from langchain_ollama import OllamaEmbeddings

embeddings_ollama = OllamaEmbeddings(
    model="llama3",
)
embed_ollama = embeddings_ollama.embed_query("What is Artificial Intelligence?")
embed_ollama