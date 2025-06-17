from langchain_postgres import PGVector
from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv
dotenv_path = "../../.env"
load_dotenv(dotenv_path)
conn_str = os.getenv("CONNECTION_STRING")
print("🔑 Kết nối:", conn_str)
# Khởi tạo embedding model
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
CONNECTION_STRING="postgresql+psycopg2://postgres:test@localhost:5432/vector_db"
# Tạo kết nối vector store
vector_store = PGVector(
    embeddings=embeddings,
    collection_name="testing",
    connection=CONNECTION_STRING
)
print("✅ Vector store connected!")