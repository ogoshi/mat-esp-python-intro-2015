# Aula de MatEsp - Python
import matplotlib.pyplot as plt
lista = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]
n = len(lista)
print ("Lista original: " , lista)
Cont = 0
# Cont se refere ha uma variavel universal usada por nos para fazer a contagem de elementos nos graficos bubble-it.

Numcont = 0
# Numcont se refere a outra variavel universal usada por nos para fazer a contagem de elementos nos graficos bubble-troca.

for i in range(0, n-1, 1):
    
# para cada interacao em i o for interno faz todas as possiveis interacaos com j.

    for j in range(i+1, n, 1):
# para cada elemento da lista[i] com o elemento da lista[j] a condicao e testada, se for verdadeira ele executa os comandos abaixo.

        if lista[i] > lista[j]:
            temp = lista[i]
            lista[i] = lista[j]
            lista[j] = temp
# nesta linha usamos uma variavel "temp" para trocarmos os valores da lista[i] para lista[j] caso ela satisfaca a condicao "if".

            x = range(0, 20, 1)
            y = lista
            plt.figure()
            plt.plot(x, y, 'ok')
            plt.title('Interacao {}'.format(Numcont))
            plt.xlabel('Indice')
            plt.ylabel('Valor')
            plt.savefig("fig/bubble-troca-{}.png".format(Numcont) )
            plt.close()
            Numcont += 1
        x = range(0, 20, 1)
        y = lista
        plt.figure()
        plt.plot(x, y, 'ok')
        plt.plot(i, lista[i], 'or')
        plt.plot(j, lista[j], 'ob')
        plt.title('Interacao {}'.format(Cont))
        plt.xlabel('Indice')
        plt.ylabel('Valor')
        plt.savefig("fig/bubble-it-{}.png".format(Cont) )
        plt.close()
        Cont += 1
# neste grupo de comandos obtivemos um grafico diferente para cada variacao de j que causa mudanca no grafico.

print ("Lista em ordem crescente: ",lista)
CMV = lista[15:20]
CMV.reverse()
print  ("Cinco maiores valores: ", CMV)
print ("Cinco menores valores:" , lista[0:5])
x = range(0, 20, 1)
y = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]
plt.figure()
plt.plot(x, y, 'ok')
plt.title('Estado Inicial')
plt.xlabel('Indice')
plt.ylabel('Valor')
plt.savefig("fig/bubble-inicio.png")
plt.close()
# nesta linha de comando obtivemos o grafico que mostra a lista antes de qualquer alteracao do comando.

x = range(0, 20, 1)
y = lista
plt.figure()
plt.plot(x, y, 'ok')
plt.title('Estado Final')
plt.xlabel('Indice')
plt.ylabel('Valor')
plt.savefig("fig/bubble-fim.png")
plt.close()
# nesta linha obtivemos o grafico que mostra a lista apos todas as alteracoes feitas pelo codigo programado.
