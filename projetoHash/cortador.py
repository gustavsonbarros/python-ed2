def cortar_em_pedacos(texto, tamanho=3):
    """
    Corta o texto em pedaços de 'tamanho' palavras
    Ex: "O gato caçou o rato" vira {"O gato caçou", "gato caçou o", "caçou o rato"}
    """
    palavras = texto.split()
    pedacos = set()
    
    for i in range(len(palavras) - tamanho + 1):
        pedaco = ' '.join(palavras[i:i+tamanho])
        pedacos.add(pedaco)
    
    return pedacos