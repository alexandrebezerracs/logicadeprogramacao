'''
Manipulação de arquivos: percorrer os meus diretórios, encontrar o arquivo pasar o comando de abertura de arquivo, passar o camando de ação.

arquivo = open("arquivo.txt", "modo")
arquivo.write('Texto')
arquivo.close()

modos de ação:
    - "r" : leitura do arquivo
    - "w" : escrita(sobrescreve o conteúdo antigo)
    - "a" : adiciona conteúdo
    - "x" : criar um arquivo
    - "b" : arquivos binários
    - "t" : texto
'''
#criando e escrevendo arquivo
import os

arquivo=open("primeiroarquivo.txt", 'w')
arquivo.write('Olá mundo! meu primeiro arquivo')
arquivo.close()

# lendo o arquivo
arquivo=open("primeiroarquivo.txt", "r")
conteudo=arquivo.read()

print(conteudo)
arquivo.close()

# aplicando boa prática
with open("primeiroarquivo.txt", 'r') as arquivo:
    conteudo=arquivo.read()
    print(conteudo)

# arquivo com múltiplas escrotas
with open("alunos.txt", "w") as arquivo:
    arquivo.write("Ana\n")
    arquivo.write("Bruna\n")
    arquivo.write("Bernado\n")
    arquivo.write("joão\n")
    arquivo.write("Gomes\n")
    arquivo.write("karynthon\n")
    
# lendo a linha a linha
with open("alunos.txt") as arquivo:
    for linha in arquivo:
        print(linha)

# Usando uma lista para escrever no arquivo
frutas=["pera", "abacaxi", "melancia", 'manga', 'caju']

with open('frutas.txt', "w") as arquivo:
    for i in frutas:
        arquivo.write(i+"\n")

#converter o arquivo em uma lista
with open("frutas.txt", 'r') as arquivo:
    linhas=arquivo.readlines()
    
print(type(linhas))
print(linhas)

# saída : ['pera\n', 'abacaxi\n', 'melancia\n', 'manga\n', 'caju\n']

# limpar a quebra linha
with open("frutas.txt", 'r') as arquivo:
    for linha in arquivo:
        print(linha.strip())
'''
saída: pera
abacaxi
melancia
manga
caju
'''
# exemplo para cadastro

os.system("cls")

while True:
    nome=input("Digite o seu nome: ").title()

    with open('cadastro.txt', 'a') as arquivo:
        arquivo.write(nome +'\n')


    sair=input("Deseja sair do sistema? s/n: ").lower()

    if sair =="s":
        break