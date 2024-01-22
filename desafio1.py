"""  Faça um algoritmo que leia os valores de A, B, C e em seguida imprima na tela a 
    soma entre A e B é mostre se a soma é menor que C. """

A = 20
B = 13
C = 54

soma = A + B
resultado = soma < C 

print(f"{A} + {B} = {soma}")

if soma < C:
    print(f"{soma} e menor que {C}:{resultado} ")
else:
    print(f"{soma} e maio que {C}:{resultado}")