import time

# MERGE SORT
def metricas_mergesort(vetor, ordem):
    inicio = time.time()
    mergesort(vetor)
    fim = time.time()

    print("Tempo (ms) vetor " + ordem + ": " + str(round(fim-inicio, 6)))

def mergesort(vetor):
    if len(vetor)>1:
        meio = len(vetor)//2
        esquerda = vetor[:meio]
        direita = vetor[meio:]

        mergesort(esquerda)
        mergesort(direita)

        i, j, k = 0, 0, 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                vetor[k]=esquerda[i]
                i=i+1
            else:
                vetor[k]=direita[j]
                j=j+1
            k=k+1

        while i < len(esquerda):
            vetor[k]=esquerda[i]
            i=i+1
            k=k+1

        while j < len(direita):
            vetor[k]=direita[j]
            j=j+1
            k=k+1