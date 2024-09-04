import os
import requests
import tempfile
import mlflow
import pandas as pd
import plotly.express as px
from mlflow.data.pandas_dataset import PandasDataset
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Message
from .utils import get_rag_score
from dotenv import load_dotenv

load_dotenv()

API_MODEL_URL = os.getenv('API_MODEL_URL')
BERTOPIC_URL = os.path.join(API_MODEL_URL, 'api/inference/bertopic')
RAG_URL = os.path.join(API_MODEL_URL, 'api/inference/rag')
MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI ")

mlflow.set_tracking_uri(uri=MLFLOW_TRACKING_URI)
mlflow.set_experiment("User Feedback")


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
            Message.objects.create(
                user_message=question,
                bot_message=ai_res['content'],
                rag_score=rag_score)
        else:
            print(f"error, Status code: {rag_res.status_code}")
    messages = Message.objects.all()
    context['messages'] = messages
    
    negative_msg = {
        "question": [],
        "answer": [],
        "rag_score": [],
        "date": []
    }
    for msg in messages:
        likes = msg.likes.count()
        dislikes = msg.dislikes.count()
        if (likes + dislikes) > 0:
            ratio = likes / (likes + dislikes)
            if ratio < 0.5:
                negative_msg['question'].append(msg.user_message)
                negative_msg['answer'].append(msg.bot_message)
                negative_msg['rag_score'].append(msg.rag_score)
                negative_msg['date'].append(msg.timestamp)
    feedback_df = pd.DataFrame.from_dict(negative_msg)            
    if not feedback_df.empty:
        with mlflow.start_run(run_name="feedback_dataset"):
            with tempfile.TemporaryDirectory() as tmpdir:
                fname = os.path.join(tmpdir, 'feedback_df.csv')
                feedback_df.to_csv(fname, index=False)
                mlflow.log_artifact(fname) 
    return render(request, 'chat/chat.html', context)


def like_msg(request, id):
    if request.method == "POST":
        instance = Message.objects.get(id=id)
        if not instance.likes.filter(id=request.user.id).exists():
            instance.likes.add(request.user)
            instance.save() 
            return render(request, 'chat/likes.html', context={'message':instance})
        else:
            instance.likes.remove(request.user)
            instance.save()
            return render(request, 'chat/likes.html', context={'message':instance})


def dislike_msg(request, id):
    if request.method == "POST":
        instance = Message.objects.get(id=id)
        if not instance.dislikes.filter(id=request.user.id).exists():
            instance.dislikes.add(request.user)
            instance.save()
            return render(request, 'chat/dislikes.html', context={'message':instance})
        else:
            instance.dislikes.remove(request.user)
            instance.save()
            return render(request, 'chat/dislikes.html', context={'message':instance})
    


@login_required
def get_topic(request):
    if request.method == "POST":
        text = request.POST.get("abstract")
        auth = set_api_auth(request)
        response = requests.post(BERTOPIC_URL, params={"abstract": text}, headers=auth)
        data = response.json()
        if response.status_code == 200:
            dfs = [pd.DataFrame.from_dict(data[key]).to_html() for key in data.keys()]
            return render(request, 'chat/topic.html', context={"dfs": dfs})
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
                            x='x',
                            y='y',
                            z='z',
                            color='cluster')
        context['graph'] = fig.to_html(full_html=False)
        return render(request, 'chat/clustering.html', context)
    return render(request, 'chat/clustering.html')