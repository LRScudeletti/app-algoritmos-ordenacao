import time

def metricas_quicksort_central(vetor, inicial, fim, ordem):
    inicio = time.time()
    quicksort_central(vetor, inicial, fim)
    fim = time.time()

    print("Tempo (ms) vetor " + ordem + ": " + str(round(fim-inicio, 6)))

def metricas_quicksort_primeiro(vetor, inicial, fim, ordem):
    inicio = time.time()
    quicksort_central(vetor, inicial, fim)
    fim = time.time()

    print("Tempo (ms) vetor " + ordem + ": " + str(round(fim-inicio, 6)))

# QUICK SORT PIVÔ ELEMENTO CENTRAL
def quicksort_central(vetor, esquerda, direita):
    i = esquerda
    j = direita
    pivo = vetor[esquerda + (direita - esquerda) // 2]
    while i <= j:
        while vetor[i] < pivo: i += 1
        while vetor[j] > pivo: j -= 1
        if i <= j: 
            vetor[i], vetor[j] = vetor[j], vetor[i]
            i += 1
            j -= 1
    if esquerda < j: 
        quicksort_central(vetor, esquerda, j)
    if i < direita: 
        quicksort_central(vetor, i, direita)
    return vetor

# QUICK SORT PIVÔ PRIMEIRO ELEMENTO
def quicksort_primeiro(vetor, esquerda, direita):
    i = esquerda
    j = direita
    pivo = vetor[esquerda]
    while i <= j:
        while vetor[i] < pivo: i += 1
        while vetor[j] > pivo: j -= 1
        if i <= j: 
            vetor[i], vetor[j] = vetor[j], vetor[i]
            i += 1
            j -= 1
    if esquerda < j: 
        quicksort_primeiro(vetor, esquerda, j)
    if i < direita: 
        quicksort_primeiro(vetor, i, direita)
    return vetor