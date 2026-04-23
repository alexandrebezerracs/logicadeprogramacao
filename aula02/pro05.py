import os

os.system("cls")

nome = input("Digite o nome do aluno: ").title()
turma = input("Digite o nome da turma: ").upper()
nota1 = input("Digite a primeira nota do aluno: ").replace(",", ".")
nota2 = input("Digite a segunda nota do aluno: ").replace(",", ".")
nota3 = input("Digite a terceira nota do aluno: ").replace(",", ".")
nota4 = input("Digite a quarta nota do aluno: ").replace(",", ".")
nota5 = input("Digite a quinta nota do aluno: ").replace(",", ".")

nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
nota4 = float(nota4)
nota5 = float(nota5)

media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

resultado = None

if media >= 7:
    resultado = "Aprovado"
elif media >= 5:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"

os.system("cls")

print(30*"=", "Boletim Escolar", 30*"=")
print("Nome do Aluno:", nome, "|Turma:", turma)
print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Nota 3:", nota3)
print("Nota 4:", nota4)
print("Nota 5:", nota5)
print(70*"=")
print("Média:", media)
print("Situação:", resultado)





    