import time


def insertion_sort(vetor,tempo):
    vetor.ordenado = False
    for i in range(1, len(vetor.lista)):
        key = vetor.lista[i]
        j = i - 1
        while j >= 0 and key < vetor.lista[j]:
            vetor.lista[j + 1] = vetor.lista[j]
            j -= 1
        vetor.lista[j + 1] = key
        time.sleep(tempo)
    vetor.ordenado = True
    return vetor.lista