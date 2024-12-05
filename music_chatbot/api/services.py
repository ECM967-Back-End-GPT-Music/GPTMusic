import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

if openai.api_key:
    print("Chave da OpenAI carregada com sucesso!")
else:
    print("Erro: Não foi possível carregar a chave da OpenAI.")

def ask_music_question(question):
    """Envia uma pergunta para o ChatGPT e retorna a resposta."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente especializado em música."},
                {"role": "user", "content": question},
            ],
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return str(e)