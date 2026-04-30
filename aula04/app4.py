"""
    sistema : calculadora
"""

while True:
    print(30*'-', "Calculadora", 30*'-')
    num1=float(input("Digite um número: "))
    num2=float(input("Digite outro número: "))
    print('1. Soma')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    opcao=input("Digite a operação: (+,-,/,*): ")

    match opcao:
        case "+":
            resultado=num1+num2
            print(f"{num1} + {num2} = {resultado}")
            break
        case '-':
            resultado=num1-num2
            print(f"{num1} - {num2} = {resultado}")
            break
        case '/':
            if num1 != 0 and num2!= 0:
                resultado=num1/num2
                print(f"{num1} / {num2} = {resultado}")
                break
        case '*':
            resultado=num1*num2
            print(f"{num1} * {num2} = {resultado}")
            break
        case _:
            print("Digite um número válido")