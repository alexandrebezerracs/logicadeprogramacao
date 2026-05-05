'''
#NOTE - nova maneira de usar o for
lista=[1,2,3,4,5,6,7,8,9,10]
dobro=[v*2 for v in lista]
print(dobro)
#NOTE - nova maneira de usar o if e else
num1=float(input("Digite o 1º número: "))
num2=float(input("Digite o 2º número: "))

#comparação ternária
result='num1 é maior' if num1>num2 else 'num1 é menor'

print(result)


#NOTE - nova maneira de embaralhar os nomes

nome1=input("Digite o Primeiro nome completo: ")
nome2=input("Digite o Segundo nome completo: ")

#separando o nome do sobrenome
parte1=nome1.split()
parte2=nome2.split()

# primeiro nome e sobrenome
primeironome1=parte1[0]
sobrenome1=parte1[-1]

primeironome2=parte2[0]
sobrenome2=parte2[-1]

novonome1=primeironome1+' '+sobrenome2
novonome2=primeironome2+' '+sobrenome1

print(novonome1)
print(novonome2)
'''