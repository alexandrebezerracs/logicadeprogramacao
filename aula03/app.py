#NOTE: Boletim Escolar

import os

print(30*"-""Boletim Escolar", 30*"-")

listadenotas =[]
nome =input("Digite o nome do Aluno: ").title()
curso=input("Digite o curso: ").upper()

while True:
    nota=float(input("Digite um nota: "))
    listadenotas.append(nota)
    print(listadenotas)
    opcao=input("Deseja adicionar mais notas? (enter - sim | n - não)").lower()

    if opcao =="n":
        break
media=sum(listadenotas)/len(listadenotas)

print(media)