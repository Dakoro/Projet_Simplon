import os
import openai
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
CLIENT = openai.OpenAI(api_key=OPENAI_API_KEY)

def api_call(messages, model):
    return CLIENT.chat.completions.create(
        model=model,
        messages=messages,
        stop=["\n\n"],
        max_tokens=200,
        temperature=0.0,
        logprobs=True,
    )

def test_openai_api_call():
    assert isinstance(OPENAI_API_KEY, str)
    question = "Who is Robert Oppenheimer ?"
    messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": f"""Answer the following Question
                              with some key facts.
                              {question}
            Answer:\n""",
            },
        ]
    
    response = api_call(messages=messages, model="gpt-3.5-turbo-0125")
    assert response.object == "chat.completion"
    keywords = [
        'physicist',
        'atomic',
        'quantum',
        'mechanics'
    ]
    content = response.choices[0].message.content
    assert isinstance(content, str)
    for word in keywords:
        assert word in content.lower().split()    
    