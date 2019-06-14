import time

#SELECTION SORT
def metricas_selectionSort(vetor, ordem):
    inicio = time.time()
    selectionsort(vetor)
    fim = time.time()

    print("Tempo (ms) vetor " + ordem + ": " + str(round(fim-inicio, 6)))

def selectionsort(vetor):
    for i in range(len(vetor)):
        indice = i
        for j in range(i+1, len(vetor)):
            if vetor[indice] > vetor[j]:
                indice = j
         
        vetor[i], vetor[indice] = vetor[indice], vetor[i]