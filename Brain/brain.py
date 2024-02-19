import openai

def get_api_key():
    with open("Data\\api.txt", "r") as fileopen:
        api_key = fileopen.read().strip()
    return api_key

openai.api_key = get_api_key()
completion = openai.Completion()

def ReplyBrain(question, chat_log=None):
    with open("Database\\FileLog.txt", "r") as filelog:
        chat_log_template = filelog.read()

    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}You: {question}\nJarvis: '
    response = completion.create(model="gpt-3.5-turbo-instruct",
                                 prompt=prompt,
                                 temperature=0.5,
                                 max_tokens=60,
                                 top_p=0.3,
                                 frequency_penalty=0.5,
                                 presence_penalty=0,
                                 )
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nYou: {question}\nJarvis: {answer}"
    
    with open("Database\\FileLog.txt", "w") as filelog:
        filelog.write(chat_log_template_update)

    return answer