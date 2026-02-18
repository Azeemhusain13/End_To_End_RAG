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