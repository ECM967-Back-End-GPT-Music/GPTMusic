from tinydb import TinyDB
from django.conf import settings

# Inicializa o TinyDB com o arquivo configurado no settings.py
db = TinyDB(settings.TINYDB_FILE)

def get_tinydb_instance():
    return db