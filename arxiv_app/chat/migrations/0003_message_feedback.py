# Generated by Django 5.0.3 on 2024-08-13 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_message_rag_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='feedback',
            field=models.BooleanField(default=False),
        ),
    ]
