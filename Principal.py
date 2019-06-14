import BubbleSort
import HeapSort
import InsertionSort
import MergeSort
import QuickSort
import SelectionSort
import ShellSort

import random

import sys
sys.setrecursionlimit(1000000)

# PRINCIPAL
tamanho = int(input ("\nDigite o tamanho do vetor: "))
vetorOriginal = random.sample(range(1, tamanho + 1), tamanho)

while True:
    print ("\nEscolha o tipo de ordenação:")
    tipo = input("1 - BubbleSort Original\n2 - BubbleSort Melhorado\n3 - HeapSort\n4 - InsertionSort\n5 - MergeSort\n6 - QuickSort Pivô Central\n7 - QuickSort Pivô Primeiro\n8 - SelectionSort\n9 - ShellSort\n")

    vetor = vetorOriginal[:]

    print("")

    if tipo=="1":
        print(vetor)
        BubbleSort.metricas_bubblesort(vetor, "aleatório")
        BubbleSort.metricas_bubblesort(sorted(vetor, key=int), "crescente")
        BubbleSort.metricas_bubblesort(sorted(vetor, key=int, reverse=True), "decrescente")
        print(vetor)
    elif tipo=="2":
        print(vetor)
        BubbleSort.metricas_bubblesort_melhorado(vetor, "aleatório")
        BubbleSort.metricas_bubblesort_melhorado(sorted(vetor, key=int), "crescente")
        BubbleSort.metricas_bubblesort_melhorado(sorted(vetor, key=int, reverse=True), "decrescente")
        print(vetor)
    elif tipo=="3":
        print(vetor)
        HeapSort.metricas_heapsort(vetor, "aleatório")
        HeapSort.metricas_heapsort(sorted(vetor, key=int), "crescente")
        HeapSort.metricas_heapsort(sorted(vetor, key=int, reverse=True), "decrescente")
        print(vetor)
    elif tipo == "4":
        print(vetor)
        InsertionSort.metricas_insertionsort(vetor, "aleatório")
        InsertionSort.metricas_insertionsort(sorted(vetor, key=int), "crescente")
        InsertionSort.metricas_insertionsort(sorted(vetor, key=int, reverse=True), "decrescente")
        print(vetor)
    elif tipo == "5":
        print(vetor)
        MergeSort.metricas_mergesort(vetor, "aleatório")
        MergeSort.metricas_mergesort(sorted(vetor, key=int), "crescente")
        MergeSort.metricas_mergesort(sorted(vetor, key=int, reverse=True), "decrescente")
        print(vetor)
    elif tipo == "6":
        print(vetor)
        QuickSort.metricas_quicksort_central(vetor, 0, len(vetor)-1, "aleatório")
        QuickSort.metricas_quicksort_central(sorted(vetor, key=int), 0, len(vetor)-1, "crescente")
        QuickSort.metricas_quicksort_central(sorted(vetor, key=int, reverse=True), 0, len(vetor)-1, "decrescente")
        print(vetor)
    elif tipo == "7":
        print(vetor)
        QuickSort.metricas_quicksort_primeiro(vetor, 0, len(vetor)-1, "aleatório")
        QuickSort.metricas_quicksort_primeiro(sorted(vetor, key=int), 0, len(vetor)-1, "crescente")
        QuickSort.metricas_quicksort_primeiro(sorted(vetor, key=int, reverse=True), 0, len(vetor)-1, "decrescente")
        print(vetor)
    elif tipo == "8":
        print(vetor)
        SelectionSort.metricas_selectionSort(vetor, "aleatório")
        SelectionSort.metricas_selectionSort(sorted(vetor, key=int), "crescente")
        SelectionSort.metricas_selectionSort(sorted(vetor, key=int, reverse=True), "decrescente")
        print(vetor)
    elif tipo == "9":
        print(vetor)
        ShellSort.metricas_shellsort(vetor, "aleatório")
        ShellSort.metricas_shellsort(sorted(vetor, key=int), "crescente")
        ShellSort.metricas_shellsort(sorted(vetor, key=int, reverse=True), "decrescente")
        print(vetor)
    else:
        print("Valor inválido")

    if input("\nDeseja ordernar o mesmo vetor com outra método? (1 - Sim ou 2 - Não): ") != '1':
        break