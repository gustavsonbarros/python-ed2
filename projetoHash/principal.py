import argparse
from faxineiro import limpar_texto, ler_arquivo
from cortador import cortar_em_pedacos
from minhash_simplao import criar_digitos_magicos, calcular_digital, comparar_digitais

def main():
    print("🐍 HashSimPy - Comparador de Textos Simplão")
    
    parser = argparse.ArgumentParser()
    parser.add_argument('arquivo1', help='Primeiro arquivo')
    parser.add_argument('arquivo2', help='Segundo arquivo')
    parser.add_argument('-k', type=int, default=3, help='Tamanho dos pedaços (padrão: 3)')
    parser.add_argument('--digitos', type=int, default=100, help='Número de digitais (padrão: 100)')
    
    args = parser.parse_args()
    
    try:
        # Passo 1: Limpeza
        texto1 = limpar_texto(ler_arquivo(args.arquivo1))
        texto2 = limpar_texto(ler_arquivo(args.arquivo2))
        
        # Passo 2: Cortar
        pedacos1 = cortar_em_pedacos(texto1, args.k)
        pedacos2 = cortar_em_pedacos(texto2, args.k)
        
        # Passo 3: Criar digitais
        funcoes_hash = criar_digitos_magicos(args.digitos)
        digital1 = calcular_digital(pedacos1, funcoes_hash)
        digital2 = calcular_digital(pedacos2, funcoes_hash)
        
        # Passo 4: Comparar
        similaridade = comparar_digitais(digital1, digital2)
        
        # Mostrar resultado
        print(f"\n🔍 Resultado: Os textos são {similaridade:.0%} parecidos")
        print(f"(Usando pedaços de {args.k} palavras e {args.digitos} digitais)")
        
    except FileNotFoundError:
        print("❌ Arquivo não encontrado! Verifique os nomes.")
    except Exception as e:
        print(f"💥 Oops! Algo deu errado: {e}")

if __name__ == "__main__":
    main()