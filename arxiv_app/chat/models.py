from django.db import models


class Message(models.Model):
    user_message = models.TextField()
    bot_message = models.TextField()
    rag_score = models.FloatField(default=-1.0)
    feedback = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
