import modulo as ma
import time

def main():
    while True:
        print(30*'-',"calculadora",30*'-')
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Limpar terminal")
        print("0. Sair da calculadora")
        

        opcao=input("Digite a opção: ")
        match opcao:
            case '1':
                print(30*"-", "soma", 30*'-')
                num1=int(input("Digite um número para a soma: "))
                num2=int(input("Digite outro número para a soma: "))
                result=ma.soma(num1,num2)
                print(result)
            case '2':
                print(30*"-", "Subtração", 30*'-')
                num1=int(input("Digite um número para a subtração: "))
                num2=int(input("Digite outro número para a subtração: "))
                result=ma.sub(num1,num2)
                print(result)
            case '3':
                print(30*"-", "Multiplicação", 30*'-')
                num1=int(input("Digite um número para a multiplicação: "))
                num2=int(input("Digite outro número para a multiplicação: "))
                result=ma.mult(num1,num2)
                print(result)
            case '4':
                print(30*"-", "Divisão", 30*'-')
                num1=float(input("Digite um número para a divisão: "))
                num2=float(input("Digite outro número para a divisão: "))
                result=ma.div(num1,num2)
                print(result)
            case '5':
                ma.limpa_terminal()
            case '0':
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
            case _:
                print("Opção inválida!❌")