# Faça um algoritmo que receba um número inteiro e imprima na tela o seu antecessor e o seu sucessor.

import random

numeros_aleatorios = random.randint(1,100)
numero = (numeros_aleatorios)

print(f"O valor antecessor de {numero} é: {numero -1}")
print(f"O valor sucessor de {numero} é: {numero +1}")

