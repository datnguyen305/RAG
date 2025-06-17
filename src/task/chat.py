def ask(llm, question: str) -> str:
    response = llm.invoke(question)
    return response

def stream(llm, question: str) -> str:
    full_response = "" 
    response = llm.stream(question)
    for token in response:
        if hasattr(token, 'content'):
            full_response += token.content
        else:
            full_response += str(token)
    return full_response