from src.document_store.loader import DocumentStoring
from src.document_store.splitter import split_text
from src.document_store.document_indexing import indexing
from dotenv import load_dotenv
import os
from langchain import hub

def test_document_pipeline():
    try:
        # Load environment variables
        load_dotenv("../../.env")
        # Define the path to the document directory
        LangChainDocument_PATH = os.getenv("LangChainDocument_PATH")
        # Create an embedding model instance
        from src.model import EmbeddingModel
        embedding = EmbeddingModel()
        print("🔄 Initializing Embedding Model...")
        # Initialize the document storing instance
        document_storing = DocumentStoring(LangChainDocument_PATH)
        print("📂 Initializing Document Storing...")
        # Loading documents
        docs, docs_sources = document_storing.store_document()
        print("📂 Loading documents...")
        # Splitting documents into chunks
        print("🔄 Splitting documents into chunks...")
        chunks = split_text(docs)
        # Connect to vector store
        connection_string = os.getenv("CONNECTION_STRING")
        collection_name = "medallion_architecture"  # Set a specific collection name
        print(f"🔑 Connection String: {connection_string}")
        print("🔄 Connecting to vector store...")
        vector_store = embedding.connect_to_vector_store_embedding(
            connection_string, 
            collection_name=collection_name
        )
        print("✅ Successfully connected to vector store")
        # Indexing documents
        print("🔄 Indexing documents...")
        indexing(vector_store, chunks)
        print("✅ Documents indexed successfully")  
        return vector_store
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return None

if __name__ == "__main__":
    test_document_pipeline()

