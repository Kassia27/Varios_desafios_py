""" Faça um algoritmo que leia o valor do salário mínimo e o valor do salário de um usuário,
    calcule quantos salários mínimos esse usuário ganha e imprima na tela o resultado. 
    (Base para o Salário mínimo R$ 1.293,20)."""


salario = float(input("Digite aqui seu salário: "))
salario_minimo = 1293.20
divisao = int(salario // salario_minimo)

if salario > salario_minimo:
     print(f"Você ganha {divisao} salários minimos.")
elif salario == salario_minimo:
     print(f"Você ganha {divisao} salários minimos.")
else:
     print("Vocễ ganha menos que um salário minimo!")