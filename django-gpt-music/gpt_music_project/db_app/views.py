from django.shortcuts import render
from db_app.tinydb_utils import get_tinydb_instance
from db_app.models import QuestionAnswer
from db_app.serializers.question_serializer import QuestionAnswerSerializer

def save_to_tinydb(question_answer_instance):
    """
    Salva os dados de um objeto QuestionAnswer no TinyDB.
    """
    db = get_tinydb_instance()
    # Adiciona os dados no TinyDB
    db.insert({
        'question': question_answer_instance.question,
        'answer': question_answer_instance.answer,
        'created_at': question_answer_instance.created_at.isoformat()
    })
