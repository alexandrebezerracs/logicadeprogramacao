"""
1. solicite dois números e exiba o resultado da divisão do segundo pelo primeiro com duas casas decimais.ok
2. peça a temperatura em fahrenheit e exiba o valor convertido em celsius
3. peça três números e exiba a media aritimética entre eles.ok
4. solicite o nome do usuário e mostre qual o tipo de dados esta armazenado ok
5. crie peçe o valor m dolares e exiba o valor correspondente em reais.
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
#NOTE - 1

numm1=float(input("Digite o primeiro número: "))
numm2=float(input("Digite o segundo número: "))
res=numm1/numm2
print(f"o resultado da divisão entre os dois números é {res:.2f}")


time.sleep(5)
os.system ("cls")
#NOTE - 2
print(30*'-', "Convertor de temperatura", 30*'-')
tempe=float(input("Digite a temperatura em fahrenheit: "))
celsus=tempe-32/1.8
print(f"A temperatura em celcios é {celsus:.2f}")


time.sleep(5)
os.system("cls")


#NOTE - 3

nm1 = float(input("Digite o Primeiro número: "))
nm2 = float(input("Digite o Segundo número: "))
nm3 = float(input("Digite o Terceiro número: "))

media = (nm1+nm2+nm3)

print(f"A média aritmética é {media}")

time.sleep(5)
os.system("cls")
#NOTE - 4

nomedousuario=input("Digite o seu nome: ")
print("olá",nomedousuario)
print("O tipo de dado amarzenado é string")



#NOTE - 5
dolra = float(input("Digite o valor em dolar: "))
real = dolra*4.98
print(f"O valor em reais é {real:.2f}")

time.sleep(5)
os.system("cls")
#NOTE - 6

lista=[1,2,3,4,5,6,7,8,9,10]
dobro=[v*2 for v in lista]
print(dobro)

#NOTE - 7

nummm1=int(input("Digite um número: "))
nummm2=int(input("Digite outro número: "))

if nummm1>nummm2:
    print("O segundo é menor que o primeiro")
else:
    print("O segundo é maior que o primeiro")

time.sleep(5)
os.system("cls")
#NOTE - 8

nome1=input("Digite o nome da 1ª pessoa")
nome2=input("Digite o nome da 2ª pessoa")
snome1=input("Digite o sobrenome da 1ª pessoa")
snome2=input("Digite o sobrenome da 2ª pessoa")

print(nome1,snome2)
print("\n",nome2,snome1)

time.sleep(5)
os.system("cls")
#NOTE - 9

nuum=int(input("digite um número: "))
print(f"A metade do número é {nuum/2}")

time.sleep(5)
os.system("cls")
#NOTE - 10

nn1=int(input("Digite a altura do retangulo: "))
nn2=int(input("Digite a largura do retangulo: "))
area=nn1*nn2
print(f"A área é {area}")

time.sleep(5)
os.system("cls")
#NOTE - 11

nnn1=int(input("Digite um número: "))
print(f"{nnn1-1}, {nnn1}, {nnn1+1}")

time.sleep(5)
os.system("cls")
#NOTE - 12

nj1=int(input("Digite um número: "))
print(f'{nj1*2}, {nj1*3}, {nj1**1/2}')
      
time.sleep(5)
os.system("cls")
#NOTE - 13

nk1=int(input("Digite um número: "))
print(f"{nk1**2}")


time.sleep(5)
os.system("cls")
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

time.sleep(5)
os.system("cls")
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


time.sleep(5)
os.system("cls")
#NOTE - 17

metros=float("Digite o valor em metros: ")
cent=metros*100
mili=metros*1000
kil=metros/1000
print(f"O valor em centimetros é {cent}")
print(f"O valor em milimetros é {mili}")
print(f"O valor em kilometros é {kil}")

time.sleep(5)
os.system("cls")
#NOTE - 18

h=int(input("Digite as horas: "))
print(h*60)

time.sleep(5)
os.system("cls")
#NOTE - 19

dit=float(input("Digite a distancia percorrida em km: "))
comb=float(input("Digite o combustivel gasto em litros: "))
media=dit/comb
print(f"A media de comsumo é {media}L/km")


time.sleep(5)
os.system("cls")
#NOTE - 20

numero=float(input("Digite qualque número real: "))

print(f"O número absoluto é {numero:.0f}")

time.sleep(5)
os.system("cls")

