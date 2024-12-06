from pathlib import Path
import environ
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import openai
from openai import OpenAIError
from db_app.models import QuestionAnswer
from db_app.views import save_to_tinydb  # Função para salvar no TinyDB
from .serializers import ChatGPTRequestSerializer


# Inicializa o django-environ
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(BASE_DIR / Path(".env"))
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Exemplo de leitura de uma variável de ambiente
OPENAI_API_KEY = env('OPENAI_API_KEY')

class ChatGPTView(APIView):
    """
    API para lidar com perguntas sobre música enviadas ao ChatGPT.
    """

    def post(self, request):
        # Valida os dados recebidos
        serializer = ChatGPTRequestSerializer(data=request.data)
        if serializer.is_valid():
            question = serializer.validated_data['question']

            try:
                # Consulta o ChatGPT
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=f"Responda sobre música: {question}",
                    max_tokens=100
                )
                answer = response['choices'][0]['text'].strip()

                # Salva no banco de dados do Django
                question_answer_instance = QuestionAnswer.objects.create(
                    question=question,
                    answer=answer
                )

                # Opcional: Salva no TinyDB
                save_to_tinydb(question_answer_instance)

                # Retorna a resposta
                return Response({'question': question, 'answer': answer}, status=status.HTTP_200_OK)

            except OpenAIError as e:
                # Trata erros da API do OpenAI
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Retorna erros de validação
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
