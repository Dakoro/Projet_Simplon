from django.db import models
from django.conf import settings


class Message(models.Model):
    user_message = models.TextField()
    bot_message = models.TextField()
    rag_score = models.FloatField(default=-1.0)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="user_like")
    dislikes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="user_dislike")
    timestamp = models.DateTimeField(auto_now_add=True)
