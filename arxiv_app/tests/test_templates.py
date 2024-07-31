import pytest

from django.urls import reverse

@pytest.mark.django_db
def test_home(client):
   url = reverse('home')
   response = client.get(url)
   assert response.status_code == 200


@pytest.mark.django_db
def test_chat_nologin(client):
   url = reverse('chat')
   response = client.get(url)
   assert response.status_code == 302


@pytest.mark.django_db
def test_chat_login(admin_client):
   url = reverse('chat')
   response = admin_client.get(url)
   assert response.status_code == 200


@pytest.mark.django_db
def test_topic_nologin(client):
   url = reverse('get_topic')
   response = client.get(url)
   assert response.status_code == 302


@pytest.mark.django_db
def test_topic_login(admin_client):
   url = reverse('get_topic')
   response = admin_client.get(url)
   assert response.status_code == 200


@pytest.mark.django_db
def test_topic_over_time_nologin(client):
   url = reverse('topic_over_time')
   response = client.get(url)
   assert response.status_code == 302


@pytest.mark.django_db
def test_topic_over_time_login(admin_client):
   url = reverse('topic_over_time')
   response = admin_client.get(url)
   assert response.status_code == 200


@pytest.mark.django_db
def test_clustering_nologin(client):
   url = reverse('get_clustering')
   response = client.get(url)
   assert response.status_code == 302


@pytest.mark.django_db
def test_clustering_login(admin_client):
   url = reverse('get_clustering')
   response = admin_client.get(url)
   assert response.status_code == 200


