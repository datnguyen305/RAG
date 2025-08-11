from langchain import hub
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate

def load_prompt(context, question):
    """Tải prompt từ template đơn giản cho RAG."""
    system_template = """You are a helpful AI assistant. Use the following pieces of context to answer the question at the end.
If you don't know the answer, just say that you don't know, don't try to make up an answer."""

    human_template = """Context information is below:
---------------------
{context}
---------------------

Question: {question}

Answer:"""

    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages([
        system_message_prompt, human_message_prompt
    ])
    return chat_prompt
