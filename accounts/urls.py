from django.urls import path

from .views import SignupView, CustomAuthToken

urlpatterns = [
    path("signup/", SignupView.as_view()),
    path("login/", CustomAuthToken.as_view()),
]
