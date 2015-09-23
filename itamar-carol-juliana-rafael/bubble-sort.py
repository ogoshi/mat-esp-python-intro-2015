# Aula de MatEsp - Python
lista = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]



        n = len(lista)
        print ("Lista original: " , lista)
        
        for i in range(0, n-1, 1):
            # para cada interacao em i o for interno faz todas as possiveis interacaos com j.
            for j in range(i+1, n, 1):
            # para cada elemento da lista[i] com o elemento da lista[j] a condicao e testada, se for verdadeira ele executa os comandos abaixo.
		if lista[i] > lista[j]:
			temp = lista[i]
			lista[i] = lista[j]
			lista[j] = temp
        print ("Lista em ordem crescente: ",lista)
        print ("Cinco menores valores:" , lista[0:5])
        a = lista[15:20]
        a.reverse()
        print  ("Cinco maiores valores: ", a)
        
