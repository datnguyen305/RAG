from langchain_openai.chat_models import ChatOpenAI
from config import LLM_CONFIG
from ..task import ask, stream

class MyChatBot:
    def __init__(self, llm_config=LLM_CONFIG):
        self.llm = ChatOpenAI(
            temperature=llm_config.get("temperature", 0.1),
            model_name=llm_config.get("model_name", "gpt-4o-mini"),
            streaming=llm_config.get("streaming", False)
        )

    def ask(self, question):
        """
        Ask a question to the chatbot and return the response.
        :param question: The question to ask.
        :return: The response from the chatbot.
        """
        return ask(self.llm, question)
    
    def stream(self, question):
        """
        Stream the response from the chatbot for a given question.
        :param question: The question to ask.
        :return: The full response from the chatbot as a string.
        """
        return stream(self.llm, question)