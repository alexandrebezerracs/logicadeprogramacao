'''
Criar um sistema de controle de carros usando CRUD
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
        modelo = input("Digite o modelo do carro: ").title()
        preco = float(input('Digite o preço do carro: ').replace(',','.'))
        marca = input("Digite a marca: ").title()

        carro ={
            "id": proximo_id,
            "modelo": modelo,
            "preço": preco,
            "marca": marca

        }
        carros.append(carro)
        proximo_id +=1

        print('✅Carro cadastrado')

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
            print("❌Carro não encontrado!")
                
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
                print("✅Carro deletado com sucesso")
                encontrado=True
                break

        if not encontrado:
            print("❌Carro não encontrado!")

    #sair
    elif opcao == "0":
        os.system("cls")
        total =20
        barra=""
        print("saindo do sistema...")
        for i in range(1,total+1):
            barra +="🟩"
            porcentagem = int((i/total)*100)
            vazio = "-" * (total-1)
            print(f'\r[{barra}] {porcentagem}%', end="")
        time.sleep(0.3)
        break
    
    else:
        print('❌opçaõ inválida')