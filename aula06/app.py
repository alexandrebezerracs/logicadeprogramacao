'''
[] - lista - valores/indices/Lista adiciona sempre no final
{} - dicionário - objeto/jason
() - Tupla
'''
lista=['Gomes','Enzo Valentim','Beatriz Alcântara','Thiago Monteverde','Clarice Lispector','Ricardo Veras','Marina Drummond',
       'Gustavo Lins','Heloísa Faissol','Bruno Piva','Letícia Dornelles','Caio Mesquita','Alessandra Negrini','Otávio Mesquita',
       'Priscila Fantin','Murilo Benício','Sabrina Sato','Hugo Gloss','Tati Quebra-Barraco','Wagner Moura','Gisele Bündchen']

#print(lista)
# imprimi um valor especifico
print(lista[0])
# imprimi o último índice
print(lista[-1])
# imprimi um intervalo
print(lista[0:5])
# ordenar a lista
# lista.sort()
# adicionar na lista
lista.append("Karython")
# inserindo em posição específica
lista.insert(2, "João Fialho")
# inserindo vários valores
lista.extend(['Ana','Bezerra da Silva','Davi Bezerra', 'Nicollas Sanches'])

numero=[]
#adicionando valores de forma dinâmica
for i in range(10):
    numero.append(i*2)
print(numero)


#for i in range(len(lista)):
#    print(f'{i+1}º valor da lista: {lista[i]}')

# removendo itens da lista
print(f'lista antes de remover: {lista}')
# pop - remove pelo índice
lista.pop(0)
#removendo o último
lista.pop()
# removendo peço valor
lista.remove('Enzo Valentim')
print(f'lista depois de remover: {lista}')

listanumeros=[n for n in range(11)]
# removendo um intervalo de valores
print(f'lista antes de remover: {listanumeros}')
del listanumeros[2:5]

print(f'lista depois de remover: {listanumeros}')


listanomes=['Gomes','Enzo Valentim','Beatriz Alcântara','Thiago Monteverde','Clarice Lispector','Ricardo Veras','Marina Drummond',
       'Gustavo Lins','Heloísa Faissol','Bruno Piva','Letícia Dornelles','Caio Mesquita','Alessandra Negrini','Otávio Mesquita',
       'Priscila Fantin','Murilo Benício','Sabrina Sato','Hugo Gloss','Tati Quebra-Barraco','Wagner Moura','Gisele Bündchen']
# alterando valor de lista
listanomes[1]='Lucas'
print('\n',listanomes)

numeros=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(numeros)):
    if numeros[i]>5:
        numeros[i]=numeros[i]*2
print(numeros)

# list comprieision
numeros=[n*2 if n>5 else n for n in numeros]
print(numeros)