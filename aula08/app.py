'''
#NOTE - funções
'''

import os
#função com parâmetro e retorno
# def funcaosegundograu(a,b,c):
#     print("Hello word!")
#     return a,b,c
#chamando a função e armazenando o valor em uma variável
# x=funcaosegundograu(1,2,3)
# print(x)

# def soma(a,b):
#     resultado=a+b
#     return resultado

# num1=float(input("Digite um número qualquer: "))
# num2=float(input("Digite um número qualquer: "))

# result=soma(num1,num2)
# print(result)

# def mostrar_msg():
#     print("Olá mundo das funções!")

# mostrar_msg()

# def mostrar_saudações(nome):
#     print(f"Olá {nome}, seja bem vindo(a)!")

# mostrar_saudações("Alexandre")

# # função recursiva
# def fatorial(n):
#     #n!
#     return 1 if n == 0 else n*fatorial(n-1)
# p=fatorial(2)
# print(p)

#função lambda
somar= lambda x, y: x+y
limpar = lambda: os.system("cls" if os.name =="nt" else "clear")

#algoritmo principal
if __name__=="__main__":
    try:
        x = int(input("Informe o valor de x: "))
        y = int(input("Informe o valor de y: "))
        result=somar(x,y)

        limpar()
        print(f"O resultado da soma é {result}.")
    except Exception as e:
        print(f"Não foi possível somar. {e}.")