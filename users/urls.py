from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.login_page, name="login_page"),
    path("signup/", views.signup_page, name="signup_page"),
]