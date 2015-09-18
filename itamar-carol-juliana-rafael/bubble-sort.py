# Aula de MatEsp - Python
lista = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]
n = len(lista)
# aqui o comando for varre a lista para todos os elementos.
print "Lista original: " + str(lista)
for i in range(0, n-1, 1):
	# para cada interação em i o 'for' interno faz todas as possiveis interações com j.
	for j in range(i+1, n, 1):
		# para cada elemento da lista[i] com o elemento da lista[j] a condição é testada, se for verdadeira ele executa os comandos abaixo.
		if lista[i] > lista[j]:
			temp = lista[i]
			lista[i] = lista[j]
			lista[j] = temp
# o comando printa, ele escreve a ultima interação da lista, ou seja, a lista organizada.
print "Lista em ordem crescente: " + str(lista)
