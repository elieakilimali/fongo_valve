from django.urls import path
from fongo_valve.apps.users.views import UserRegisterView,LoginView

urlpatterns = [
    path("register/",UserRegisterView.as_view()),
    path("login/",LoginView.as_view())
]