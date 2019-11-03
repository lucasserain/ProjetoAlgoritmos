
class GnomeSort:

    def gnome_sort(vetor, tempo):
        index = 0
        while index < len(vetor.lista):
            if index == 0:
                index = index + 1
            if vetor.lista[index] >= vetor.lista[index - 1]:
                index = index + 1
            else:
                vetor.lista[index], vetor.lista[index - 1] = vetor.lista[index - 1], vetor.lista[index]
                index = index - 1
        vetor.ordenado = True
        return vetor.lista