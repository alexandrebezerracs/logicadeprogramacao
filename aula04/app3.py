'''
    Programa 01 - Aula04 - 28/04
    Professor: Karynthon
    turma:2º ds
    sistema de sorteios 2.0
'''
import random
import os
import time
listadesorteados=[]
listadenomes=[]

print(30*'-','Bem vindo ao sistema de sorteios',30*'-')

while True:
    nome = input("Digite um nome para ser sorteado: ").title()
    listadenomes.append(nome)

    opcao=input("deseja adicionar mais? (s - Sim) ou enter para parar!: ").lower()

    if opcao!="s":
        break

while True:
    if not listadenomes:
        print('A lista de nomes está vazia!')
        break
    else:
        nomesorteado=random.choice(listadenomes)
        listadenomes.remove(nomesorteado)
        listadesorteados.append(nomesorteado)
        os.system("cls")

    for i in range(5,0,-1):
        time.sleep(1)
        os.system("cls")
        print(f"Contagem regressiva...{i}")
        
    print(f'O sorteado foi: {nomesorteado}')
    
    sortearnovamente=input('Deseja sortear outro nome? (s - Sim | n - não): ').lower()

    if sortearnovamente == "n":
        break

print(listadesorteados)
print("Fim do programa!")