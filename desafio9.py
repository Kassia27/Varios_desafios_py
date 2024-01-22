""" Faça um algoritmo que calcule o IMC (Índice de Massa Corporal) de uma pessoa, leia o seu peso e sua altura e imprima na tela sua condição 
de acordo com a tabela abaixo:

Fórmula do IMC = peso / (altura) ²
Tabela Condições IMC

 Abaixo de 18,5   | Abaixo do peso          
 Entre 18,6 e 24,9 | Peso ideal (parabéns)  
 Entre 25,0 e 29,9 | Levemente acima do peso
 Entre 30,0 e 34,9 | Obesidade grau I 
 Entre 35,0 e 39,9 | Obesidade grau II (severa)
 Maior ou igual a 40 | Obesidade grau III (mórbida) """


altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = int(peso / (altura * altura))

if imc >= 40:
    print(" Você está com Obesidade grau III - MÓRBIDA")
elif imc >= 35.0 and imc <= 39.9:
    print("Você está com Obesidade grau II -SERVERA")
elif imc >= 30 and imc <= 34.9:
    print("Você está com Obesidade grau I")
elif imc >= 25 and imc <= 29.9:
    print("Você está levemente acima do peso")
elif imc >= 18.6 and imc <= 24.9:
    print(" Você está com o peso ideal - PARABÉNS!")
else:
    print("Você está abaixo do peso!")