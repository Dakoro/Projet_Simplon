from django.urls import path
from django.views.generic import TemplateView
from chat import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="base.html"), name='home'),
    path("chat/", views.chat, name='chat'),
    path("topic/", views.get_topic, name='get_topic'),
    path("topic_over_time/",
         views.get_topic_over_time,
         name='topic_over_time'),
]
