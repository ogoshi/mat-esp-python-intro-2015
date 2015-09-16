# Aula de MatEsp - Python
# definição de funçao. 
def codigo_sort(lista):
      """ aqui a funçao 'len' pega o numero de elementos da lista
 e guarda na variável 'n' """
      n = len(lista)
      # aqui o comando for varre a lista para todos os elementos. 	
      for i in range(0, n-1, 1):
	     # para cada interação em i o 'for' interno faz todas as possiveis interações com j.
            for j in range(i+1, n, 1):
		  # para cada elemento da lista[i] com o elemento da lista[j] a condição é testada, se for verdadeira ele executa os comandos abaixo.
                  if lista[i] > lista[j]:
                        temp = lista[i]
                        lista[i] = lista[j]
                        lista[j] = temp
      # o comando printa, ele escreve a ultima interação da lista, ou seja, a lista organizada.
      print lista
