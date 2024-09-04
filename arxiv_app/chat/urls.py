from django.urls import path
from django.views.generic import TemplateView
from chat import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="base.html"), name='home'),
    path("chat/", views.chat, name='chat'),
    path("chat/like_msg/<int:id>", views.like_msg, name='like_msg'),
    path("chat/dislike_msg/<int:id>", views.dislike_msg, name='dislike_msg'),
    path("topic/", views.get_topic, name='get_topic'),
    path('clustering/', views.get_clustering, name="get_clustering"),
    path("topic_over_time/", views.get_topic_over_time, name='topic_over_time'),
]
