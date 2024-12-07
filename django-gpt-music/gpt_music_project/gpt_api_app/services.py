import openai

# Configuração da API Key do OpenAI
from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(BASE_DIR / Path(".env"))
env = environ.Env()
openai.api_key = env("OPENAI_API_KEY")  # Certifique-se de que esta linha está correta

def ask_music_question(question):
    """Envia uma pergunta para o ChatGPT e retorna a resposta."""
    try:
        # Chamada para o modelo de chat
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" se tiver acesso
            messages=[
                {"role": "system", "content": "Você é um assistente especializado em música."},
                {"role": "user", "content": question},
            ],
            max_tokens=100,  # Limite de tokens para a resposta
            temperature=0.7,  # Controle da criatividade da resposta
        )
        # Retorna o conteúdo da resposta
        return response['choices'][0]['message']['content'].strip()
    except openai.OpenAIError as e:
        # Trata erros específicos da API do OpenAI
        return f"Erro na API OpenAI: {str(e)}"
    except Exception as e:
        # Trata outros erros inesperados
        return f"Erro inesperado: {str(e)}"
