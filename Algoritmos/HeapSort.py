import time



class HeapSort:
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    def heap_sort(vetor, tempo):
        vetor.ordenado = False
        n = len(vetor.lista)
        for i in range(n, -1, -1):
            self.heapify(vetor.lista, n, i)
            time.sleep(tempo)
        for i in range(n - 1, 0, -1):
            vetor.lista[i], vetor.lista[0] = vetor.lista[0], vetor.lista[i]
            heapify(vetor.lista, i, 0)
            time.sleep(tempo)
        vetor.ordenado = True
        return vetor.lista