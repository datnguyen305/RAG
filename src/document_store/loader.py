import os
from langchain_community.document_loaders import PyPDFLoader

class DocumentStoring:
    def __init__(self, directory=os.getenv("LangChainDocument_PATH")):
        self.directory = directory
        self.documents = []
        self.documents_sources = []

    def store_document(self):
        all_docs = []
        document_sources = []

        if not os.path.exists(self.directory):
            raise FileNotFoundError(f"❌ Directory does not exist: {self.directory}")

        for file_name in os.listdir(self.directory):
            if file_name.lower().endswith(".pdf"):
                file_path = os.path.join(self.directory, file_name)
                print(f"📄 Loading: {file_path}")
                loader = PyPDFLoader(file_path)
                docs = loader.load()
                print(f"📃 Preview: {docs[0].page_content[:100]}...")
                print(f"📌 Metadata: {docs[0].metadata}")
                all_docs.extend(docs)
                document_sources.append(docs[0].metadata)

        self.documents = all_docs
        self.documents_sources = document_sources

        return self.documents, self.documents_sources
