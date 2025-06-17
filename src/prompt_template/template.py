from langchain import hub

def load_prompt(context, question):
    """Tải prompt từ LangChain Hub và hoàn thành với biến truyền vào."""
    prompt = hub.pull("rlm/rag-prompt")
    return prompt
