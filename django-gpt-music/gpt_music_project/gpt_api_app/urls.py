from django.urls import path
from .views import ChatGPTView

urlpatterns = [
    path('musicgpt/', ChatGPTView),
]