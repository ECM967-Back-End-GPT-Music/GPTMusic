from django.shortcuts import render
from django.http import JsonResponse
from .services import ask_music_question
from .tinydb_manager import save_question_and_answer, get_all_questions
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

@csrf_exempt
def music_question(request):
    """Recebe uma pergunta e retorna a resposta do ChatGPT."""
    if request.method == "POST":
        body = json.loads(request.body)
        question = body.get("question", "")
        if not question:
            return JsonResponse({"error": "Sem pergunta"}, status=400)

        # Obter resposta da API
        answer = ask_music_question(question)

        # Salvar no TinyDB
        save_question_and_answer(question, answer)

        return JsonResponse({"answer": answer})

    return JsonResponse({"error": "Método não implementado"}, status=405)

@csrf_exempt
def list_questions(request):
    """Retorna o histórico de perguntas e respostas."""
    if request.method == "GET":
        questions = get_all_questions()
        return JsonResponse({"questions": questions}, safe=False)

    return JsonResponse({"error": "Método não implementado"}, status=405)
