
from haystack import Pipeline
from haystack.components.writers import DocumentWriter
from haystack.components.preprocessors import DocumentSplitter
# from haystack.components.embedders import SentenceTransformersDocumentEmbedder
from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
from haystack.components.converters import PyPDFToDocument
from pathlib import Path # type: ignore
import os
from dotenv import load_dotenv
from QASystem.utils import pinecone_config
from haystack.components.preprocessors import DocumentCleaner
from haystack.document_stores.in_memory import InMemoryDocumentStore

document_store = InMemoryDocumentStore()
def ingest(document_store):

	# configuring pinecone database
	document_store = PineconeDocumentStore(
		index="default",
		namespace="default",
		dimension=5
	)
pipeline = Pipeline()
pipeline.add_component("converter", PyPDFToDocument())
pipeline.add_component("cleaner", DocumentCleaner())
pipeline.add_component("splitter", DocumentSplitter(split_by="sentence", split_length=5))
pipeline.add_component("writer", DocumentWriter(document_store=document_store))
pipeline.connect("converter", "cleaner")
pipeline.connect("cleaner", "splitter")
pipeline.connect("splitter", "writer")
pipeline.run({"converter": {"sources": [Path("/Users/admin/Desktop/sample_project/End to end RAG/data/iesc111 1.35.25 PM.pdf")]}})

	#adding the components in pipeline
	# indexing.add_component("converter", PyPDFToDocument())
	# indexing.add_component("splitter", DocumentSplitter(split_by="sentence", split_length=2))
	# indexing.add_component("embedder", SentenceTransformersDocumentEmbedder())
	# indexing.add_component("writer", DocumentWriter(document_store))

	# #coneecting all the components of pipeline
	# indexing.connect("converter", "splitter")
	# indexing.connect("splitter", "embedder")
	# indexing.connect("embedder", "writer")

	#stroing the data as a embedding in the database
	# indexing.run({"converter": {"sources": [Path("/Users/admin/Desktop/sample_project/End to end RAG/data/iesc111 1.35.25 PM.pdf")]}})
 
 
if __name__ == "__main__":
    #loading the environment variable
    load_dotenv()
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY
    
    print("Import Successfully")
    document_store=pinecone_config()
    
    ingest(document_store)
