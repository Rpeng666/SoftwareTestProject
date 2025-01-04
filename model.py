import ollama


def generateCode(messages = '', model = 'codellama:latest'):
    # print("debug content: ", messages)
    response = ollama.chat(model=model, messages=[
        {
        'role': 'user',
        'content': messages,
        }
    ])
    # print("debug response: ", response)
    return response['message']['content']