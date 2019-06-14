import time

# BUBBLE SORT
def metricas_bubblesort(vetor, ordem):
    inicio = time.time()
    bubblesort(vetor)
    fim = time.time()

    print("Tempo (ms) vetor " + ordem + ": " + str(round(fim-inicio, 6)))

def bubblesort(vetor):
    tamanho = len(vetor)

    for i in range(tamanho):
        for j in range(0, tamanho-i-1):
            if vetor[j] > vetor[j+1] :
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]

# BUBBLE SORT MELHORADO
def metricas_bubblesort_melhorado(vetor, ordem):
    inicio = time.time() 
    bubblesort_melhorado(vetor)
    fim = time.time()

    print("Tempo (ms) vetor " + ordem + ": " + str(round(fim-inicio, 6)))

def bubblesort_melhorado(vetor):
    trocar = True
    passar = len(vetor)-1
    while passar > 0 and trocar:
       trocar = False
       for i in range(passar):
           if vetor[i]>vetor[i+1]:
               trocar = True
               temp = vetor[i]
               vetor[i] = vetor[i+1]
               vetor[i+1] = temp
       passar = passar-1


