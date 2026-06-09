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

open("carros.txt", "a").close()


with open("carros.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:

        dados=linha.strip().split(";")

        if len(dados)==4:

            carro ={
                "id": int(dados[0]),
                "modelo": dados[1],
                "preço": dados[2],
                "marca": dados[3]
            }

            carros.append(carro)

            if carro["id"] >= proximo_id:
                proximo_id = carro["id"] + 1


with open("carros.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:

        dados=linha.strip().split(";")

        if len(dados)==4:

            carro ={
                "id": int(dados[0]),
                "modelo": dados[1],
                "preço": dados[2],
                "marca": dados[3]
            }

            carros.append(carro)

            if carro["id"] >= proximo_id:
                proximo_id = carro["id"] + 1
# Menu
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
            
            carros.append(carro)
            proximo_id +=1
            print('✅ Carro cadastrado')
            sair = input("Deseja adicionar mais? (s - sim) ou enter para parar!").lower()
            if sair !="s":
                break

    #read
    elif opcao =="2":
        os.system("cls")
        if not carros:
            print('⚠️ Nenhum carro encontrado')
        else:
            print('\n📋 Lista de carros')
            for carro in carros:
                print(f'ID: {carro['id']} | Modelo: {carro['modelo']} | Preço: {carro['preço']} | Marca: {carro['marca']}')

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
        with open("carros.txt", "w", encoding="utf-8") as arquivo:
            for carro in carros:
                linha = (
                    f"{carro['id']};"
                    f"{carro['modelo']};"
                    f"{carro['preço']};"
                    f"{carro['marca']}\n"
                )
                arquivo.write(linha)
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