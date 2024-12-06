from django.urls import path
from .views import handle_music_question

urlpatterns = [
    path('musicgpt/', handle_music_question, name='handle_music_question'),
]