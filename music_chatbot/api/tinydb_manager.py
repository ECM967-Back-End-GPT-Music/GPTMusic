from tinydb import TinyDB, Query

# Configuração do banco de dados TinyDB
db = TinyDB('db.json')

def save_question_and_answer(question, answer):
    """Salva uma pergunta e resposta no banco de dados."""
    db.insert({"question": question, "answer": answer})

def get_all_questions():
    """Retorna todas as perguntas e respostas salvas."""
    return db.all()