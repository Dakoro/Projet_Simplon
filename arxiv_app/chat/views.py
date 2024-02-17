from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Message
import requests
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_MODEL_URL = os.getenv('API_MODEL_URL')
BERTOPIC_URL = os.path.join(API_MODEL_URL, 'api/inference/bertopic')
RAG_URL = os.path.join(API_MODEL_URL, 'api/inference/rag')


@login_required
def chat(request):
    if request.method == "POST":
        question = request.POST.get('question')
        rag_res = requests.post(RAG_URL, params={"question": question})
        data = rag_res.json()
        ai_res = data['answer']
        print(ai_res['content'])
        Message.objects.create(user_message=question,
                               bot_message=ai_res['content'])
    messages = Message.objects.all()
    return render(request, 'chat/chat.html', {"messages": messages})


@login_required
def get_topic(request):
    if request.method == "POST":
        text = request.POST.get("abstract")
        print(text)
        response = requests.post(BERTOPIC_URL, params={"abstract": text})
        data = response.json()
        df = pd.DataFrame.from_dict(data)
        return render(request, 'chat/topic.html', context={"df": df.to_html()})
    return render(request, 'chat/topic.html')


@login_required
def get_topic_over_time(request):
    context = {}
    if request.method == 'POST':
        response = requests.get(os.path.join(BERTOPIC_URL, 'topic_over_time'))
        context['graph'] = response.json()
        return render(request, 'chat/topic_over_time.html', context=context)
    return render(request, 'chat/topic_over_time.html')
