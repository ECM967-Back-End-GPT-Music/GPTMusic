from django.urls import path
from .views import AskGPTAPIView

urlpatterns = [
    path('musicgpt/', AskGPTAPIView.as_view(), name='ask_gpt_music'),
]