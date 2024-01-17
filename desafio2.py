# Faça um algoritmo para receber um número qualquer e imprimir na tela se o número é par ou ímpar, positivo ou negativo.

import random

numeros = random.randint(0,5000)
divisao = numeros // 2  
resto = numeros % 2

if resto == 0:
    print(f"{numeros} e um número PAR")
    print("POSITIVO")
else:
    print(f"{numeros} e um número ÍMPAR")
    print("NEGATIVO")