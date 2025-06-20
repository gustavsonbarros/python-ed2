import re

def limpar_texto(texto):
    """Deixa o texto mais uniforme pra comparar"""
    texto = texto.lower()  # Tudo minúsculo
    texto = re.sub(r'[^\w\s]', '', texto)  # Tira pontuação
    texto = re.sub(r'\d+', '', texto)  # Remove números
    return ' '.join(texto.split())  # Normaliza espaços

def ler_arquivo(caminho):
    """Lê o arquivo como um bom estagiário faria"""
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        return arquivo.read()