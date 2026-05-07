'''

Desenvolva um sistema de gerenciamento de veiculos, permita cadastrar o veículo pegando do usuário os seguintes dados (modelo, marca, preço)
    - Os dados devem ser armazenados em um arquivo.
    - o usuário deve poder cadastrar quantos carros quiser sem ter que rodar o sistema novamente.
    - deve ter a opção de ler os carros existentes
    - devem ser cadastrados eu um arquivo .txt e usar dicionário.

'''
import time
import os
carros=[]
proximo_id=1


os.system("cls")
while True:
    print("\n----------------- Sistema de carros 🚗 -----------------")
    print('1. cadastrar carros')
    print('2. listar carros')
    print('3. Atualizar carros')
    print('4. deletar carros')
    print('0. sair')

    opcao=input("escolha uma das opções: ")

    #create
    if opcao=="1":
        os.system("cls")
        while True:
            modelo = input("Digite o modelo do carro: ").title()
            preco = input('Digite o preço do carro: ').replace(',','.')
            marca = input("Digite a marca: ").title()

            carro ={
                "id": proximo_id,
                "modelo": modelo,
                "preço": preco,
                "marca": marca

            }
            with open("carros.txt", "a")as arquivo:
                arquivo.write(f'ID: {carro['id']} | Modelo: {carro['modelo']} | Preço: {carro['preço']} | Marca: {carro['marca']} \n')

            proximo_id +=1
            print('✅ Carro cadastrado')
            sair=input("Deseja sair do sistema? s/n: ").lower()
            if sair =="s":
                break
            

        

    #read
    elif opcao =="2":
        os.system("cls")
        print('\n📋 Lista de carros')
        with open("carros.txt", "r")as arquivos:
            for linha in arquivo:
                print(linha.strip())
       

    #update
    elif opcao =='3':
        os.system("cls")
        print('\n📋 Lista de carros')
        for carro in carros:
            print(f'ID: {carro['id']} | Modelo: {carro['modelo']} | Preço: {carro['preço']} | Marca: {carro['marca']}')
        id_busca = int(input("Digite o id do carro para deletar: "))

        encontrado=False
        for carro in carros:
            if carro['id']==id_busca:
                novo_modelo = input('Digite o novo modelo: ').title()
                novo_preco = input('Digite o novo preço: ').replace(',','.')
                nova_marca = input('Digite a nova marca: ').title()

                carro["modelo"] = novo_modelo
                carro["preço"] = novo_preco
                carro["marca"] = nova_marca

                print("✅ Carro encontrado com sucesso! ")
                encontrado = True
                break
        if not encontrado:
            print("❌ Carro não encontrado!")
                
    #delete
    elif opcao =='4':
        os.system("cls")
        print('\n📋 Lista de carros')
        for carro in carros:
            print(f'ID: {carro['id']} | Modelo: {carro['modelo']} | Preço: {carro['preço']} | Marca: {carro['marca']}')
        id_busca = int(input("Digite o id do carro para deletar: "))
       
        encontrado=False

        for carro in carros:
            if carro['id']==id_busca:
                carros.remove(carro)
                print("✅ Carro deletado com sucesso")
                encontrado=True
                break

        if not encontrado:
            print("❌ Carro não encontrado!")

    #sair
    elif opcao == '0':
        total = 20
        barra =""
        print('Saindo do Sistema...')
        for i in range(1, total +1):
            barra +="🟩"
            porcentagem = int((i / total *100))
            vazio = "-" * (total -1)
            print(f'\r[{barra}] {porcentagem}%', end="")
            time.sleep(0.2)
        break

    else:
        print('❌ Opção inválida.')