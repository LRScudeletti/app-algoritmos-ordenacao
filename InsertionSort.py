import time

# INSERTION SORT
def metricas_insertionsort(vetor, ordem):
    inicio = time.time()
    insertionsort(vetor)
    fim = time.time()

    print("Tempo (ms) vetor " + ordem + ": " + str(round(fim-inicio, 6)))

def insertionsort(vetor):
    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i-1
        while j >=0 and chave < vetor[j]:
                vetor[j+1] = vetor[j]
                j -= 1
        vetor[j+1] = chave