from langchain_openai import OpenAIEmbeddings
from config import EMBEDDING_CONFIG
from ..task import embedding

class EmbeddingModel:
    def __init__(self, embedding_config=EMBEDDING_CONFIG):
        """
        Initializes the EmbeddingModel with the specified configuration.
        
        :param embedding_config: Configuration for the embedding model.
        """
        self.embedding_model = OpenAIEmbeddings(
            model=embedding_config.get("model_name", "text-embedding-3-small")
        )
    
    def embed_query(self, documents):
        return embedding(self.embedding_model, documents)
    
    def connect_to_vector_store_embedding(self, connection_string=None, collection_name=None):
            """
            Connects to the vector store using the initialized embedding model.
            :return: The connected vector store instance.
            """
            from ..document_store import connect_to_vector_store
            return connect_to_vector_store(self.embedding_model, connection_string=connection_string, collection_name=collection_name)
