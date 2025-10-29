import os
import sys
import django


def setup_django() -> None:
    # Garante que o diretório raiz do projeto esteja no caminho de importação
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

    # Define a variável de ambiente para localizar o settings.py
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    # Inicializa o Django
    django.setup()
