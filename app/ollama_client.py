import ollama

MODEL = "llama3.2"

def query_ollama(messages, model=MODEL):
    response = ollama.chat(
        model=model,
        messages=messages
    )
    return response["message"]["content"]
