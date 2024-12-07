from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import openai
from openai import OpenAIError
from .serializers import ChatGPTRequestSerializer
from db_app.models import QuestionAnswer
from db_app.views import save_to_tinydb
from .services import ask_music_question

# Configuração da API Key do OpenAI
from pathlib import Path
import environ
import os

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(BASE_DIR / Path(".env"))
env = environ.Env()
OPENAI_API_KEY = env("OPENAI_API_KEY")

class AskGPTAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Valida o corpo da requisição usando o serializer
        serializer = ChatGPTRequestSerializer(data=request.data)
        if serializer.is_valid():
            question = serializer.validated_data['question']
            try:
                # Faz a consulta à API do ChatGPT
                answer = ask_music_question(question)

                # Salva no banco de dados do Django
                question_answer_instance = QuestionAnswer.objects.create(
                    question=question,
                    answer=answer
                )

                # Salva no TinyDB (opcional)
                save_to_tinydb(question_answer_instance)

                # Retorna a resposta com status 200
                return Response({'question': question, 'answer': answer}, status=status.HTTP_200_OK)

            except OpenAIError as e:
                # Trata erros da API do ChatGPT
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Retorna erro de validação do serializer
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
