import time


class BubbleSort:
    def bubble_sort(vetor, tempo):
        elementos = len(vetor.lista) - 1
        vetor.ordenado = False
        ordenado = False
        j = 0
        while not ordenado:
            ordenado = True
            for i in range(elementos):
                if vetor.lista[i] > vetor.lista[i + 1]:
                    vetor.lista[i], vetor.lista[i + 1] = vetor.lista[i + 1], vetor.lista[i]
                    ordenado = False
                time.sleep(tempo)
        vetor.ordenado = True

        return vetor.lista
