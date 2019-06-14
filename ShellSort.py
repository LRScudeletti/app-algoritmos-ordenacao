import time

#SHELL SORT
def metricas_shellsort(vetor, ordem):
    inicio = time.time()
    shellsort(vetor)
    fim = time.time()

    print("Tempo (ms) vetor " + ordem + ": " + str(round(fim-inicio, 6)))

def shellsort(vetor):
    tamanho = len(vetor)
    diferenca = tamanho/2

    while diferenca > 0:
        for i in range(int(diferenca), tamanho):
            temp = vetor[i]
            j = i
            while  j >= int(diferenca) and vetor[j-int(diferenca)] > temp:
                vetor[j] = vetor[j-int(diferenca)]
                j -= int(diferenca)
            vetor[j] = temp
        diferenca /= 2