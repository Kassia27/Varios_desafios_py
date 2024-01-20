# Faça um algoritmo que leia um valor qualquer e imprima na tela com um reajuste de 5%.

valor = float(input("Digite um valor :"))
desconto = valor * 0.05
reajuste = valor - desconto

print(f"Você teve um reajuste de R${desconto} o seu valor atual e de R${reajuste} ")
