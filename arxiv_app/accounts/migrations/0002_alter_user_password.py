# Generated by Django 5.0.2 on 2024-02-25 20:46

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default=accounts.models._create_hash, max_length=24),
        ),
    ]
