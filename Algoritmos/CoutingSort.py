import time

class CoutingSort:
    def counting_sort(vetor,tempo):
        vetor.ordenado = False
        m = max(vetor.lista) + 1
        count = [0] * m
        for a in vetor.lista:
            time.sleep(tempo)
            count[a] += 1
        i = 0
        for a in range(m):
            for c in range(count[a]):
                time.sleep(tempo)
                vetor.lista[i] = a
                i += 1
        vetor.ordenado = True
        return vetor.lista