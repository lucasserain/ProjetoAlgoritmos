from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
import time
import numpy as np
from tkinter.messagebox import showinfo

VALORES = []
teste = None

class minhaThread(threading.Thread):
    def __init__(self, threadID, vetor, algoritmo, tempo):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.vetor = vetor
        self.algoritmo = algoritmo
        self.tempo = tempo
        self.kill = threading.Event()
    def run(self):
        inicio = time.time()
        if self.algoritmo == 'BubbleSort':
            bubble_sort(self.vetor,self.tempo)
        elif self.algoritmo == 'InsertionSort':
            insertion_sort(self.vetor,self.tempo)
        elif self.algoritmo == 'SelectionSort':
            selection_sort(self.vetor,self.tempo)
        elif self.algoritmo == 'MergeSort':
            self.vetor.ordenado = merge_sort(self.vetor,0,len(self.vetor.lista)-1,self.tempo) 
        elif self.algoritmo == 'QuickSort':
            start = 0
            end = len(self.vetor.lista) - 1  
            quick_sort(self.vetor, start , end, self.tempo)
        elif self.algoritmo == 'HeapSort':
            heap_sort(self.vetor,self.tempo)
        elif self.algoritmo == 'CountingSort':
            counting_sort(self.vetor,self.tempo)
        elif self.algoritmo == 'RadixSort':
            radix_sort(self.vetor,self.tempo)
        elif self.algoritmo == 'GnomeSort':
            gnome_sort(self.vetor,self.tempo)
        elif self.algoritmo == 'PancakeSort':
            pancake_sort(self.vetor,self.tempo)     
        fim = time.time() 
        self.vetor.tempoAni = fim - inicio
        self.vetor.tempoExe = self.vetor.tempoAni - (self.vetor.qnt_sleep * self.tempo)
        print(self.algoritmo, "chegou ao fim.")
        self.vetor.ordenado = True
        self.stop()
        
    def stop(self):
        # Mata a thread
        print("Thread encerrada.")
        self.kill.set()
        
''' ----------------------> BUBBLE SORT <---------------------  '''
def bubble_sort(vetor,tempo):
    elementos = len(vetor.lista)-1
    vetor.ordenado = False
    ordenado = False
    j = 0
    while not ordenado:
        ordenado = True    
        for i in range(elementos):
            if vetor.lista[i] > vetor.lista[i+1]:
                vetor.lista[i], vetor.lista[i+1] = vetor.lista[i+1],vetor.lista[i]
                ordenado = False
            time.sleep(tempo/2)
            vetor.qnt_sleep+= 0.5
    return vetor.lista   

''' ----------------------> INSERTION SORT <---------------------  '''
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
        vetor.qnt_sleep+= 1 
    return vetor.lista 

''' ----------------------> SELECTION SORT <---------------------  '''
def selection_sort(vetor,tempo):
    vetor.ordenado = False
    for i in range(len(vetor.lista)):
        min_idx = i
        for j in range(i + 1, len(vetor.lista)):
            if vetor.lista[min_idx] > vetor.lista[j]:
                min_idx = j
        vetor.lista[i], vetor.lista[min_idx] = vetor.lista[min_idx], vetor.lista[i]  
        time.sleep(tempo)
        vetor.qnt_sleep+= 1 
    return vetor.lista

''' ----------------------> MERGE SORT <---------------------  '''
def merge(arr, l, m, r, tempo): 
    time.sleep(tempo)
    arr.qnt_sleep+= 1 
    n1 = m - l + 1
    n2 = r- m 
    L = [0] * (n1) 
    R = [0] * (n2) 
    for i in range(0 , n1): 
        L[i] = arr.lista[l + i] 
    for j in range(0 , n2): 
        R[j] = arr.lista[m + 1 + j] 
    i = 0  
    j = 0 
    k = l 
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr.lista[k] = L[i] 
            i += 1
        else: 
            arr.lista[k] = R[j] 
            j += 1
        k += 1
    while i < n1: 
        arr.lista[k] = L[i] 
        i += 1
        k += 1
    while j < n2: 
        arr.lista[k] = R[j] 
        j += 1
        k += 1

def merge_sort(arr,l,r,tempo): 
    if l < r: 
        m = (l+(r-1))//2
        merge_sort(arr, l, m, tempo) 
        merge_sort(arr, m+1, r, tempo) 
        merge(arr, l, m, r, tempo)     
    return True

''' ----------------------> QUICK SORT <---------------------  '''

def partition(vetor, start, end, tempo):
    pivot = vetor.lista[np.random.randint(start, end)]
    bottom = start - 1
    top = end
    done = 0
    while not done:
        while not done:
            bottom = bottom + 1
            if bottom == top:
                done = 1
                break
            if vetor.lista[bottom] > pivot:
                vetor.lista[top] = vetor.lista[bottom]
                break
        while not done:
            top = top - 1
            if top == bottom:
                done = 1
                break
            if vetor.lista[top] < pivot:
                vetor.lista[bottom] = vetor.lista[top]
                break
    time.sleep(tempo)
    vetor.qnt_sleep+= 1 
    vetor.lista[top] = pivot
    return top

def quick_sort(vetor, start, end, tempo):
    vetor.ordenado = False
    if start < end:
        split = partition(vetor, start, end, tempo)
        quick_sort(vetor, start, split - 1, tempo)
        quick_sort(vetor, split + 1, end, tempo)
    else:
        return vetor.lista
    
''' ----------------------> HEAP SORT <---------------------  '''
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
        
def heap_sort(vetor,tempo):
    vetor.ordenado = False
    n = len(vetor.lista)
    for i in range(n, -1, -1):
        heapify(vetor.lista, n, i)
        time.sleep(tempo/2)
        vetor.qnt_sleep+= 0.5 
    for i in range(n - 1, 0, -1):
        vetor.lista[i], vetor.lista[0] = vetor.lista[0], vetor.lista[i]  
        heapify(vetor.lista, i, 0)
        time.sleep(tempo/2)
        vetor.qnt_sleep+= 0.5 
    return vetor.lista

''' ----------------------> COUNTING SORT <---------------------  '''
def counting_sort(vetor,tempo):
    vetor.ordenado = False
    m = max(vetor.lista) + 1
    count = [0] * m
    for a in vetor.lista:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            vetor.lista[i] = a
            i += 1
        time.sleep(tempo)  
        vetor.qnt_sleep+= 1 
    return vetor.lista    

''' ----------------------> RADIX SORT <---------------------  '''
def counting_sort_r(vetor, n, exp, tempo):
    vAux = [0] * 10
    v_Ord = [0] * (n)
    for i in range(n):
        vAux[(int)((vetor.lista[i] / exp) % 10)] += 1
    for i in range(1, 10):
        vAux[i] += vAux[i - 1]
    for i in range(n - 1, -1, -1):
        v_Ord[vAux[(int)((vetor.lista[i] / exp) % 10)] - 1] = vetor.lista[i]
        vAux[(int)((vetor.lista[i] / exp) % 10)] -= 1
    for i in range(n):
        vetor.lista[i] = v_Ord[i]
        time.sleep(tempo)
        vetor.qnt_sleep+= 1 
    return vetor.lista

def radix_sort(vetor,tempo):
    vetor.ordenado = False
    m = max(vetor.lista)
    n = len(vetor.lista)
    exp = 1
    while m >= exp :
        counting_sort_r(vetor, n, exp, tempo)
        exp *= 10  
    return vetor.lista
    
''' ----------------------> GNOME SORT <---------------------  '''
def gnome_sort(vetor, tempo):
    index = 0
    while index < len(vetor.lista):
        time.sleep(tempo)
        vetor.qnt_sleep+= 1 
        if index == 0:
            index = index + 1
        if vetor.lista[index] >= vetor.lista[index - 1]:
            index = index + 1
        else:
            vetor.lista[index], vetor.lista[index - 1] = vetor.lista[index - 1], vetor.lista[index]
            index = index - 1  
    return vetor.lista

''' ----------------------> PANCAKE SORT <---------------------  '''
def flip(arr, i, tempo): 
    start = 0
    while start < i: 
        temp = arr[start] 
        arr[start] = arr[i] 
        arr[i] = temp 
        start += 1
        i -= 1

def findMax(arr, n, tempo): 
    mi = 0
    for i in range(0,n): 
        if arr[i] > arr[mi]: 
            mi = i 
    return mi 
  
def pancake_sort(vetor, tempo): 
    n = len(vetor.lista)
    curr_size = n 
    while curr_size > 1: 
        time.sleep(tempo)
        vetor.qnt_sleep+= 1 
        mi = findMax(vetor.lista, curr_size, tempo) 
        if mi != curr_size-1: 
            flip(vetor.lista, mi, tempo) 
            flip(vetor.lista, curr_size-1, tempo) 
        curr_size -= 1
    return vetor.lista    

''' ----------------------> CLASSE VETOR <---------------------  '''    
class vetor:
    def __init__(self, lista):
        self.lista = lista
        self.ordenado = False
        self.qnt_sleep = 0
        self.tempoExe = 0
        self.tempoAni = 0

    def __str__(self):
        return self.nome
   
''' ----------------------> MAIN <---------------------  '''
# Listbox das opções de algoritmos
class App:
    def __init__(self, janela):
        self.janela = janela
        self.listbox = Listbox(self.janela, selectmode=MULTIPLE, width=15)
        self.listbox.pack()
        self.listbox.place(x=250, y=120)
        self.listbox.bind("<<ListboxSelect>>", self.callback)
        self.listbox.insert(END, "BubbleSort")
        self.listbox.insert(END, "InsertionSort")
        self.listbox.insert(END, "SelectionSort")
        self.listbox.insert(END, "MergeSort")
        self.listbox.insert(END, "QuickSort")
        self.listbox.insert(END, "HeapSort")
        self.listbox.insert(END, "CountingSort")
        self.listbox.insert(END, "RadixSort")
        self.listbox.insert(END, "GnomeSort")
        self.listbox.insert(END, "PancakeSort")
        self.selection = self.listbox.curselection()

    def callback(self, a):
        if len(self.listbox.curselection()) > 2:
            for i in self.listbox.curselection():
                if i not in self.selection:
                    self.listbox.selection_clear(i)
        self.selection = self.listbox.curselection()

    def passaParam(self):
        global VALORES
        VALORES = [self.listbox.get(idx) for idx in self.listbox.curselection()]
        print(VALORES)
        
# x - tela de simulação dos algoritmos
def tela_simulacao():
    global janela
    teste.passaParam()
    teste2.passaParamm()
    if len(VALORES) != 2:
        showinfo("Erro no número de Algoritmos Selecionados!", "Escolha 2 Algoritmos para comparação.")
        return
    if int(varN.get()) <= 1:
        showinfo("Erro no tamanho do vetor inserido!", "Você escolheu um valor de n menor ou igual a 1 (vetor ordenado).")
        return
    janela.destroy()
    janela = Tk()
    janela.configure(background='black')
    janela.attributes('-fullscreen',True)
    janela.title("ANÁLISE E COMPLEXIDADE DE ALGORITMOS")
    janela.geometry("600x600+250+50")
    
    # 2 - Recebe as Entradas do usuário
    n = int(varN.get())  # Entrada do usuário - número de elementos
    tempo = TEMPO_ENTRADA  # Entrada do usuário - tempo de atraso para exibição da animação
    AlgoritmoA = VALORES[0]  # Algoritmo usada para comparação
    AlgoritmoB = VALORES[1]  # #Algoritmo usada para comparação
    
    # 3 - Cria lista de elementos inicial
    lista = np.random.randint(10000, size=n)
    algoritmosUsados = 2  # Indica quantos algoritmos foram implementados

    # 4 - Cria uma cópia da lista para cada algoritmo utilizado
    i = 0
    Vetores = []
    Figuras = []
    while (i < algoritmosUsados):
        listaProv = lista.copy()
        Vetores.append(vetor(listaProv))
        Figuras.append(Figure(dpi=80, facecolor='#105F10', linewidth=1.0))
        Figuras[i].add_subplot(111).plot(Vetores[i].lista)
        i = i + 1
        
    # Labels de Tempo
    labelTempoA = Label(janela, text='Tempo de Animação (seg): ')
    labelTempoA.pack()
    labelTempoA.place(x=50, y=100)
    
    labelTempoA2 = Label(janela, text='Tempo de Execução (seg): ')
    labelTempoA2.pack()
    labelTempoA2.place(x=50, y=200)
    
    labelTempoB = Label(janela, text='Tempo de Animação (seg): ')
    labelTempoB.pack()
    labelTempoB.place(x=50, y=400)
    
    labelTempoB2 = Label(janela, text='Tempo de Execução (seg): ')
    labelTempoB2.pack()
    labelTempoB2.place(x=50, y=500)
    
    # 5 - Cria Canvas para os algoritmos
    labelA = Label(janela, text=VALORES[0])
    labelA.pack()
    canvas = FigureCanvasTkAgg(Figuras[0], master=janela)
    canvas.draw()
    canvas.get_tk_widget().pack()
    
    labelB= Label(janela, text=VALORES[1])
    labelB.pack()
    canvasB = FigureCanvasTkAgg(Figuras[1], master=janela)
    canvasB.draw()
    canvasB.get_tk_widget().pack()

    
    
    menu_bt = Button(janela, text='Voltar/Menu Principal', command=tchauQuerida)
    menu_bt.pack()
    # Enquanto o vetor estiver desordenado, atualiza
    start = False
    while (Vetores[0].ordenado == False or Vetores[1].ordenado == False):
        
        Figuras[0].clear()
        Figuras[0].add_subplot(111).plot(Vetores[0].lista)
        canvas.draw()
        Figuras[0].canvas.flush_events()

        Figuras[1].clear()
        Figuras[1].add_subplot(111).plot(Vetores[1].lista)
        canvasB.draw()
        Figuras[1].canvas.flush_events()
        # Chama thread's para rodar simultanêamente
        if start == False:
            time.sleep(1)
            start = True
            thread = minhaThread(0, Vetores[0], AlgoritmoA, tempo)
            thread.start()
            threadb = minhaThread(0, Vetores[1], AlgoritmoB, tempo)
            threadb.start()
            
    # Exibe tempo de execução e animação
    labelTempoA_ = Label(janela, text=Vetores[0].tempoAni)
    labelTempoA_.pack()
    labelTempoA_.place(x=50, y=150)
    
    labelTempoA__ = Label(janela, text=Vetores[0].tempoExe)
    labelTempoA__.pack()
    labelTempoA__.place(x=50, y=250)
    
    labelTempoB_ = Label(janela, text=Vetores[1].tempoAni)
    labelTempoB_.pack()
    labelTempoB_.place(x=50, y=450)
    
    labelTempoB__ = Label(janela, text=Vetores[1].tempoExe)
    labelTempoB__.pack()
    labelTempoB__.place(x=50, y=550)
    
    # Atualiza uma última vez
    time.sleep(1)        
    Figuras[0].clear()
    Figuras[0].add_subplot(111).plot(Vetores[0].lista)
    canvas.draw()
    Figuras[0].canvas.flush_events()

    Figuras[1].clear()
    Figuras[1].add_subplot(111).plot(Vetores[1].lista)
    canvasB.draw()
    Figuras[1].canvas.flush_events()            
    
    
    # Indica que o processamento foi finalizado
    print("Processamento finalizado")

# 1 - Cria tela
def menu():
    # Janela Principal
    global janela
    janela = Tk()
    label = Label(janela, text='ANÁLISE E COMPLEXIDADE DE ALGORITMOS')
    label.pack()
    label.place(x=130, y=80)
    label2 = Label(janela, text='Selecione dois algoritmos e a velocidade desejada para iniciar a simulação')
    label2.place(x=130, y=80)
    # Botão de simulação
    menu_bt_simular = Button(janela, text='Simular', command=tela_simulacao)
    menu_bt_simular.place(x=270, y=300)
    # Label de numero elementos
    labelIn = Label(janela, text='Insira o número de elementos:')
    labelIn.place(x=150, y=50)
    # Input de elementos
    global varN
    varN = StringVar()
    inputN = Entry(janela, textvariable=varN, width=5)
    inputN.pack()
    varN.set(50)
    inputN.place(x=320,y=50)
    global teste 
    teste = App(janela)
    v = IntVar()
    '''
    Radiobutton(janela, text="Rápido", padx = 20, variable=v,value=1).pack(anchor=W)
    Radiobutton(janela, text="Atraso Médio", padx = 20, variable=v,value=2).pack(anchor=W)
    Radiobutton(janela, text="Tempo Real", padx = 20, variable=v,value=3).pack(anchor=W)
    '''
    janela.geometry("500x500+250+50")
    janela.title("ANÁLISE E COMPLEXIDADE DE ALGORITMOS")
    janela.configure(background='black')
    janela.mainloop()

def tchauQuerida():
    janela.destroy()
    menu()


if __name__ == '__main__':
    menu()
