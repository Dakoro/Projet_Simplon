# Create your views here.
import os
import requests
import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from accounts.forms import UserRegisterForm
from dotenv import load_dotenv
load_dotenv()

API_MODEL_URL = os.getenv('API_MODEL_URL')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            print(username)
            print(raw_password)
            # login to app
            user = authenticate(username=username, password=raw_password)
            print(user)
            if user is not None:
                login(request, user)

                signup_url = f'{API_MODEL_URL}/api/signup'
                login_url = f'{API_MODEL_URL}/api/login'
                
                credentials = json.dumps({
                    "username": username,
                    "password": raw_password
                })
                
                credentials_login = {
                    "username": username,
                    "password": raw_password
                }

                res_signup = requests.post(signup_url, data=credentials)
                print(res_signup.content)

                res_login = requests.post(login_url, data=credentials_login)
                print(res_login.content)

                messages.success(
                    request, f"""Your account has been created
                    and you are now logged in as {username}"""
                )
                return redirect("home")
            else:
                messages.error(
                    request, "Authentification failed"
                )
                return redirect('register')
    else:
        form = UserRegisterForm()
    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request=request, user=user)
            login_url = f'{API_MODEL_URL}/api/login'
            credentials = {
                "username": username,
                "password": password,
            }

            res_login = requests.post(login_url, data=credentials)
            token = res_login.json()['access_token']
            request.session['token'] = token

            messages.success(request,
                             message=f"you are now logged in as {username}")
            return redirect('home')
        else:
            messages.error(request,
                           message="Authentification failed")

    return render(request, "accounts/login.html")


@login_required
def logout_view(request):
    logout(request)
    return render(request, 'accounts/logout.html')
