"""
Calculos e manipulação de variáveis
"""

nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")
peso = input("Digite seu peso: ")
altura = input("Digite a sua altura: ")

#tratamento de exceção
try:
    idade = int(idade)
    peso = float(peso)
    altura = float(altura)
except ValueError as e:  # noqa: F841
    print("Idade deve ser um número válido")
    idade = 0

imc = peso / (altura**2)
print("Seu imc é:", imc)