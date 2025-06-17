from langchain_core.documents import Document
from typing_extensions import List, TypedDict
from . import load_prompt, test_document_pipeline
from langchain_openai import ChatOpenAI
from .task import retrieve, generate

class State(TypedDict):
    question: str
    context: List[Document]
    answer: str




