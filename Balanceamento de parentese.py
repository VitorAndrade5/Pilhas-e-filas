# verificar o balanceamento de parentese 
from collections import deque
def verificar_parenteses_balanceados(expressao):
    pilha = []   
    pares = {')': '(', '}': '{', ']': '['}  
    posicoes = [] 
    erros = []  

    for i, caractere in enumerate(expressao):
        if caractere in "({[":
            pilha.append((caractere, i))  
        elif caractere in ")}]":
            if not pilha:
                erros.append(f"Parêntese de fechamento '{caractere}' extra na posição {i}.")
            else:
                ultimo_aberto, posicao = pilha.pop()
                if pares[caractere] != ultimo_aberto:
                    erros.append(f"Parêntese '{caractere}' na posição {i} não corresponde a '{ultimo_aberto}' na posição {posicao}.")
    
    while pilha:
        ultimo_aberto, posicao = pilha.pop()
        erros.append(f"Parêntese de abertura '{ultimo_aberto}' sem fechamento na posição {posicao}.")
    
    return erros

expressao = input("Digite uma conta com parêntese: ")
erros = verificar_parenteses_balanceados(expressao)

if not erros:
    print("Parênteses balanceados.")
else:
    print("Erros encontrados:")
    for erro in erros:
        print("-", erro)
