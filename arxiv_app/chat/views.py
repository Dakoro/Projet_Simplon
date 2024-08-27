import requests
import os
import pandas as pd
import plotly.express as px
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Message
from .utils import get_coord, get_images, get_rag_score
from dotenv import load_dotenv

load_dotenv()

API_MODEL_URL = os.getenv('API_MODEL_URL')
BERTOPIC_URL = os.path.join(API_MODEL_URL, 'api/inference/bertopic')
RAG_URL = os.path.join(API_MODEL_URL, 'api/inference/rag')

def set_api_auth(request):
    token = request.session['token']
    auth = {
        "Authorization": f"Bearer {token}"
    }
    return auth


@login_required
def chat(request):
    context = {}
    if request.method == "POST":
        question = request.POST.get('question')
        auth = set_api_auth(request)
        rag_res = requests.post(RAG_URL, params={"question": question}, headers=auth)
        if rag_res.status_code == 200:
            data = rag_res.json()
            ai_res = data['openai']['choices'][0]['message']
            logprobs = data['openai']['choices'][0]['logprobs']['content']
            rag_score = get_rag_score(logprobs)
            relevants_docs = data['relevants_docs']
            coord_dict = get_coord(relevants_docs)
            images = get_images(coord_dict)
            context['images'] = images
            Message.objects.create(
                user_message=question,
                bot_message=ai_res['content'],
                rag_score=rag_score)
        else:
            print(f"error, Status code: {rag_res.status_code}")
    messages = Message.objects.all()
    context['messages'] = messages
    return render(request, 'chat/chat.html', context)


@login_required
def get_topic(request):
    if request.method == "POST":
        text = request.POST.get("abstract")
        auth = set_api_auth(request)
        response = requests.post(BERTOPIC_URL, params={"abstract": text}, headers=auth)
        data = response.json()
        if response.status_code == 200:
            df = pd.DataFrame.from_dict(data)
            return render(request, 'chat/topic.html', context={"df": df.to_html()})
    return render(request, 'chat/topic.html')


@login_required
def get_topic_over_time(request):
    context = {}
    if request.method == 'POST':
        auth = set_api_auth(request)
        topic_over_time_path = os.path.join(BERTOPIC_URL, 'topic_over_time')
        response = requests.get(topic_over_time_path, headers=auth)
        context['graph'] = response.json()
        return render(request, 'chat/topic_over_time.html', context=context)
    return render(request, 'chat/topic_over_time.html')


@login_required
def get_clustering(request):
    context = {}
    if request.method == 'POST':
        auth = set_api_auth(request)
        clustring_url = os.path.join(API_MODEL_URL, 'api/clustering')
        response = requests.get(clustring_url, headers=auth)
        data = response.json()
        df = pd.DataFrame.from_dict(data)
        fig = px.scatter_3d(df,
                            x='proj_x',
                            y='proj_y',
                            z='proj_z',
                            color='cluster')
        context['graph'] = fig.to_html(full_html=False)
        return render(request, 'chat/clustering.html', context)
    return render(request, 'chat/clustering.html')