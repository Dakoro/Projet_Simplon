from django.shortcuts import render
from .models import Message
import requests
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_MODEL_URL = os.getenv('API_MODEL_URL')
BERTOPIC_URL = os.path.join(API_MODEL_URL, 'api/inference/bertopic')
RAG_URL = os.path.join(API_MODEL_URL, 'api/inference/rag')


def chat_view(request):
    if request.method == "POST":
        question = request.POST.get('question')
        rag_res = requests.post(RAG_URL, params={"question": question})
        data = rag_res.json()
        ai_res = data['answer']
        print(ai_res['content'])
        Message.objects.create(user_message=question,
                               bot_message=ai_res['content'])
    messages = Message.objects.all()
    return render(request, 'chat.html', {"messages": messages})


def get_topic(request):
    if request.method == "POST":
        text = request.POST.get("abstract")
        print(text)
        response = requests.post(BERTOPIC_URL, params={"abstract": text})
        data = response.json()
        df = pd.DataFrame.from_dict(data)
        print(df)
        return render(request, 'topic.html', context={"df": df.to_html()})
    return render(request, 'topic.html')

