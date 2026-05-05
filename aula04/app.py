#for

#laço de for, ele é finito: quando eu sei  o número de repetições 
frutas=['melancia', 'abacaxi', 'melão', 'pera']
fruta = "melancia"

#for f in frutas:
    #print(f)

#for range(inicio, fim, salto)

#!SECTIONfor i in range(1,20,2):
    #print("repeti")

#num=int(input("Digite um número para sua tabuada: "))   #pede para o usuário inserir um número

#for i in range(1,11):   #cria um laço de repetição finito de 1 á 10
#    print(f"{i} X {num} = {i*num}")

'''
    Programa 01 - Aula04 - 28/04
    Professor: Karynthon
    turma:2º ds
    sistema de sorteios 1.0
'''
import os
import time
import random

listadenomes=['Arthur', 'Benjamin', 'Gael', 'Theo', 'Heitor', 'Heloísa', 'Maya', 'Aurora', 'Valentina',
'Cecília', 'Alex', 'Charlie', 'Taylor', 'Robin', 'Cris', 'Luna', 'Íris', 'Kai', 'Flora', 'Ravi']


for i, nome in enumerate(listadenomes):

    print(f"{i+1}º {nome}")

    nomebuscar=input("Digite um nome para buscar: ").title()

    if nomebuscar in listadenomes:
        print("Usuário encontrado")
    else:
        print("Usuário não encontrado")



'''
listasorteados=[]

sorteados=1
while sorteados==1:
    nomesorteado=random.choice(listadenomes)
    time.sleep(5)
    print(f"\nSorteado: {nomesorteado}")
    listasorteados.append(nomesorteado)

    print(f"Lista antes de remover: {len(listadenomes)}")

    listadenomes.remove(nomesorteado)

    print(f"Lista atualizada: {len(listadenomes)}\n{30*'-'}")

    sorteados+=1

print("\nfim do programa")
'''