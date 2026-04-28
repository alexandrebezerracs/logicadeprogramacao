"""
1. solicite dois números e exiba o resultado da divisão do segundo pelo primeiro com duas casas decimais.ok
2. peça a temperatura em fahrenheit e exiba o valor convertido em celsius
3. peça três números e exiba a media aritimética entre eles.ok
4. solicite o nome do usuário e mostre qual o tipo de dados esta armazenado ok
5. crie peça o valor em dolarese exibva o valor correspondente em reais.
6. crie uma lista com 10 números e exiba a lista com o dobro de cada um dos números
7. solicite dois números e verifique se o segundo é menor que o primeiro ok
8. solicite o nome e sobrenome de dois usuários e imprima  o nome do primeiro com o sobrenome do segundo e inversamente ok
9. peça um número e exiba a metade dele ok
10. solicite a altura e a largura de um retangulo e exiba a area ok
11. crie um sistema que receba um numero e exiba o seu antecessor e seu sucessor ok
12. crie um sistema que receba um número e mostre o seu dobro, triplo e a raiz quadrada ok
13. peça um número e exiba o quadrado dele ok 
14. peça tres números e exiba o produto deles ok
15. peça o valor de um produto e exiba o valor após aplicar um desconto de 10% ok
16. solicite um valor principal, a taxa de juros e o tempo e exiba o valor dos juros simples ok
17. receba o valor em metros do usuario e converta o valor em centímetros milímetros e quilometros. exiba os tres valores
18. peça uma quantidade em horas e exiba o valor correspondente em minutos
19. peça a distancia percorrida e o combustivel gasto e exiba o consumo médio do veículo
20. solicite um numero e exiba o valor absoluto dele sem considerar o sinal
"""
import os
import time
#NOTE - 14

n1=int(input("Digite o 1º número: "))
n2=int(input("Digite o 2º número: "))
n3=int(input("Digite o 3º número: "))

prd = n1*n2*n3

print(f"O produto entre os tres valores é {prd}")

time.sleep(5)
os.system ("cls")

# 
#NOTE - 15

p1=float(input("Digite o valor do produto: ")).replace(",", ".")

desconto=p1*0.1

print(f"Valor com desconto: {desconto:.2f}")

#NOTE - 16
time.sleep(5)
os.system("cls")

print(30*'-', "Juros Simples", 30*'-')
cap=int(input("Digite o capital: "))
tax=float(input("Digite a taxa em decimal: "))
temp=int(input("Digite o tempo do investimento em anos: "))

juros=cap*tax*temp

print(f"O montante é {juros}")
time.sleep(5)
os.system("cls")

#NOTE - 20

numero=float(input("Digite qualque número real: "))

print(f"O número absoluto é {numero:.0f}")

time.sleep(5)
os.system("cls")

print(30*'-', "Convertor de temperatura", 30*'-')
tempe=float(input("Digite a temperatura em fahrenheit: "))

print(f"A temperatura em celcios é {tempe-32}")