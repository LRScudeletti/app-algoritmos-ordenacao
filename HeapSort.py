import time

# HEAP SORT
def metricas_heapsort(vetor, ordem):
    inicio = time.time()
    heapsort(vetor)
    fim = time.time()

    print("Tempo (ms) vetor " + ordem + ": " + str(round(fim-inicio, 6)))
 
def heapsort(vetor):
    tamanho = len(vetor)

    for i in range(tamanho, -1, -1):
        heapify(vetor, tamanho, i)
 
    for i in range(tamanho-1, 0, -1):
        vetor[i], vetor[0] = vetor[0], vetor[i]   
        heapify(vetor, i, 0)

def heapify(vetor, tamanho, i):
    maior = i  
    l = 2 * i + 1     
    r = 2 * i + 2     
 
    if l < tamanho and vetor[i] < vetor[l]:
        maior = l
 
    if r < tamanho and vetor[maior] < vetor[r]:
        maior = r
 
    if maior != i:
        vetor[i],vetor[maior] = vetor[maior],vetor[i]
        heapify(vetor, tamanho, maior)