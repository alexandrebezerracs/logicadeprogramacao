"""
1.crie um programa que o usuário possa digitar quantos númeors quiser e ao terminar imprima a lista em ordem crescente

2. Crie um programa que o usuário possa digitar a quantidade de notas de um determinado aluno  (nota minima 0 e nota maxima 10) e o programa calcula a media desse aluno, e ao final 
imprima se o aluno esta aprevoado(nota>7) ou reprovado(nota<7)
"""
#NOTE - Programa01
import os
lista_num = []

while True:
    num = int(input('Digite o número: '))
    lista_num.append(num)
    opcao = input("Deseja adicionar mais? (s - sim) ou enter para parar!").lower()
    os.system('cls')
    if opcao != 's':
        break

lista_num.sort()
print(lista_num)

#NOTE - Programa02

print(30*'-',"Boletim escolar",30*'-')
nome=input('Digite o nome do aluno(a): ').title()
listadenotas=[]
while True:
    notas = input("Digite a nota do aluno(a): ").replace(",", ".")
    notas=float(notas)

    if notas>10 or notas<0:
        print("nota inválida!")
        break

    listadenotas.append(notas)

    colocarmaisnota=input('Deseja adicionar mais uma nota? (Enter - Sim | n - não): ').lower()
    
    if colocarmaisnota=="n":
        break

os.system("cls")
media=sum(listadenotas)/len(listadenotas)
result="Aprovado!" if media>=7 else "Reprovado!"
print(result)