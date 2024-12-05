from django.urls import path
from .views import music_question, list_questions

urlpatterns = [
    path('music-question/', music_question, name='music_question'),
    path('questions/', list_questions, name='list_questions'),
]
