notas = [ ]
notas.append(7)
notas.append(9)
notas.append(4)
print('Lista original: ', notas)
notas.remove(4)
print('Lista após remover a nota 4:', notas)
soma = 0
for nota in notas:
	soma += nota
	media = soma / len(notas)
print("Soma das notas:", soma, "Média:", media)

