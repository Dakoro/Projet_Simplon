from django.urls import path
import accounts.views as user_views

urlpatterns = [
    path("register/", user_views.register, name="register"),
    path("login/", user_views.login_view, name="login"),
    path("logout/", user_views.logout_view, name="logout"),
]
