""" Faça um algoritmo que leia quatro notas obtidas por um aluno, calcule a média das 
nota obtidas, imprima na tela o nome do aluno e se o aluno foi aprovado ou reprovado. 
Para o aluno ser considerado aprovado sua média final deve ser maior ou igual a 7. """

notas = sum([1.0, 8.0, 6.0])
media = notas / 3
aluno = "Caio"

if media >= 7:
    print(f"Aluno {aluno} - APROVADO!")
elif media < 7:
    print(f"Aluno {aluno} - REPROVADO! ")
