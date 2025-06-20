import hashlib

def criar_digitos_magicos(num_digitos=100):
    """Cria várias funções de hash diferentes"""
    return [
        lambda x, s=i: int(hashlib.sha1(f"{s}{x}".encode()).hexdigest(), 16)
        for i in range(num_digitos)
    ]

def calcular_digital(pedacos, funcoes_hash):
    """Cria a 'digital' compacta do texto"""
    digital = []
    for funcao in funcoes_hash:
        menor_hash = min(funcao(pedaco) for pedaco in pedacos)
        digital.append(menor_hash)
    return digital

def comparar_digitais(digital1, digital2):
    """Calcula o quão parecidas são as digitais"""
    iguais = sum(1 for a, b in zip(digital1, digital2) if a == b)
    return iguais / len(digital1)