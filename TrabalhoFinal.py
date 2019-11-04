from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
import time
import numpy as np
from tkinter.messagebox import showinfo

VALORES = []
teste = None
tempoDeExecucao = 0

# Classe para criação de Threads
class minhaThread(threading.Thread):
    def __init__(self, threadID, vetor, algoritmo, tempo):
        threading.Thread.__init__(self)
        self.threadID = threadID # Id da thread criada
        self.vetor = vetor # lista desordenada
        self.algoritmo = algoritmo # Algoritmo que deve ser utilizado para ordenação
        self.tempo = tempo # Tempo de atraso - utilizado por conta da parte gráfica
        self.kill = threading.Event() # Método usado para matar a thread ao fim da execução
    def run(self):
        inicio = time.time()
        # Aqui, selecionamos o algoritmo que terá a HONRA de ordernar nosso vetor
        if self.algoritmo == 'BubbleSort':
            bubble_sort(self.vetor,self.tempo,inicio)
        elif self.algoritmo == 'InsertionSort':
            insertion_sort(self.vetor,self.tempo,inicio)
        elif self.algoritmo == 'SelectionSort':
            selection_sort(self.vetor,self.tempo,inicio)
        elif self.algoritmo == 'MergeSort':
            self.vetor.ordenado = merge_sort(self.vetor,0,len(self.vetor.lista)-1,self.tempo,inicio) 
        elif self.algoritmo == 'QuickSort':
            start = 0
            end = len(self.vetor.lista) - 1  
            quick_sort(self.vetor, start , end, self.tempo,inicio)
        elif self.algoritmo == 'HeapSort':
            heap_sort(self.vetor,self.tempo,inicio)
        elif self.algoritmo == 'CountingSort':
            counting_sort(self.vetor,self.tempo,inicio)
        elif self.algoritmo == 'RadixSort':
            radix_sort(self.vetor,self.tempo,inicio)
        elif self.algoritmo == 'GnomeSort':
            gnome_sort(self.vetor,self.tempo,inicio)
        elif self.algoritmo == 'PancakeSort':
            pancake_sort(self.vetor,self.tempo,inicio)    
        # Aqui calculamos o tempo final gasto pelo algoritmo    
        fim = time.time() 
        self.vetor.tempoAni = fim - inicio
        # Para calcularmos o tempo de execução, retiramos o tempo levado pelos time.sleep
        self.vetor.tempoExe = self.vetor.tempoAni - (self.vetor.qnt_sleep * self.tempo)
        # Indicamos que o algoritmo terminou no prompt de comando.
        print(self.algoritmo, "chegou ao fim.")
        self.vetor.ordenado = True
        # Chama função que "mata" a thread
        self.stop()
        
    def stop(self):
        # Mata a thread
        print("Thread encerrada.")
        self.kill.set()
        
''' ----------------------> BUBBLE SORT <---------------------  '''
def bubble_sort(vetor,tempo,inicio):
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
            fim = time.time() 
            vetor.tempoAni = fim - inicio
            vetor.tempoExe = vetor.tempoAni - (vetor.qnt_sleep * tempo)
    return vetor.lista   

''' ----------------------> INSERTION SORT <---------------------  '''
def insertion_sort(vetor,tempo,inicio):
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
        fim = time.time() 
        vetor.tempoAni = fim - inicio
        vetor.tempoExe = vetor.tempoAni - (vetor.qnt_sleep * tempo)
    return vetor.lista 

''' ----------------------> SELECTION SORT <---------------------  '''
def selection_sort(vetor,tempo,inicio):
    vetor.ordenado = False
    for i in range(len(vetor.lista)):
        min_idx = i
        for j in range(i + 1, len(vetor.lista)):
            if vetor.lista[min_idx] > vetor.lista[j]:
                min_idx = j
        vetor.lista[i], vetor.lista[min_idx] = vetor.lista[min_idx], vetor.lista[i]  
        time.sleep(tempo)
        vetor.qnt_sleep+= 1 
        fim = time.time() 
        vetor.tempoAni = fim - inicio
        vetor.tempoExe = vetor.tempoAni - (vetor.qnt_sleep * tempo)
    return vetor.lista

''' ----------------------> MERGE SORT <---------------------  '''
def merge(arr, l, m, r, tempo,inicio): 
    time.sleep(tempo)
    arr.qnt_sleep+= 1 
    fim = time.time() 
    arr.tempoAni = fim - inicio
    arr.tempoExe = arr.tempoAni - (arr.qnt_sleep * tempo)
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

def merge_sort(arr,l,r,tempo,inicio): 
    if l < r: 
        m = (l+(r-1))//2
        merge_sort(arr, l, m, tempo,inicio) 
        merge_sort(arr, m+1, r, tempo,inicio) 
        merge(arr, l, m, r, tempo,inicio)     
    return True

''' ----------------------> QUICK SORT <---------------------  '''

def partition(vetor, start, end, tempo,inicio):
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
    fim = time.time() 
    vetor.tempoAni = fim - inicio
    vetor.tempoExe = vetor.tempoAni - (vetor.qnt_sleep * tempo)
    vetor.lista[top] = pivot
    return top

def quick_sort(vetor, start, end, tempo,inicio):
    vetor.ordenado = False
    if start < end:
        split = partition(vetor, start, end, tempo, inicio)
        quick_sort(vetor, start, split - 1, tempo, inicio)
        quick_sort(vetor, split + 1, end, tempo, inicio)
    else:
        return vetor.lista
    
''' ----------------------> HEAP SORT <---------------------  '''
def heapify(arr, n, i,inicio):
    largest = i  
    l = 2 * i + 1
    r = 2 * i + 2  
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  
        heapify(arr, n, largest, inicio)
        
def heap_sort(vetor,tempo,inicio):
    vetor.ordenado = False
    n = len(vetor.lista)
    for i in range(n, -1, -1):
        heapify(vetor.lista, n, i,inicio)
        time.sleep(tempo/2)
        vetor.qnt_sleep+= 0.5 
        fim = time.time() 
        vetor.tempoAni = fim - inicio
        vetor.tempoExe = vetor.tempoAni - (vetor.qnt_sleep * tempo)
    for i in range(n - 1, 0, -1):
        vetor.lista[i], vetor.lista[0] = vetor.lista[0], vetor.lista[i]  
        heapify(vetor.lista, i, 0, inicio)
        time.sleep(tempo/2)
        vetor.qnt_sleep+= 0.5 
        fim = time.time() 
        vetor.tempoAni = fim - inicio
        vetor.tempoExe = vetor.tempoAni - (vetor.qnt_sleep * tempo)
    return vetor.lista

''' ----------------------> COUNTING SORT <---------------------  '''
def counting_sort(vetor,tempo,inicio):
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
        fim = time.time() 
        vetor.tempoAni = fim - inicio
        vetor.tempoExe = vetor.tempoAni - (vetor.qnt_sleep * tempo)
    return vetor.lista    

''' ----------------------> RADIX SORT <---------------------  '''
def counting_sort_r(vetor, n, exp, tempo,inicio):
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
        fim = time.time() 
        vetor.tempoAni = fim - inicio
        vetor.tempoExe = vetor.tempoAni - (vetor.qnt_sleep * tempo)
    return vetor.lista

def radix_sort(vetor,tempo,inicio):
    vetor.ordenado = False
    m = max(vetor.lista)
    n = len(vetor.lista)
    exp = 1
    while m >= exp :
        counting_sort_r(vetor, n, exp, tempo,inicio)
        exp *= 10  
    return vetor.lista
    
''' ----------------------> GNOME SORT <---------------------  '''
def gnome_sort(vetor, tempo,inicio):
    index = 0
    while index < len(vetor.lista):
        if index == 0:
            index = index + 1
        if vetor.lista[index] >= vetor.lista[index - 1]:
            index = index + 1
        else:
            vetor.lista[index], vetor.lista[index - 1] = vetor.lista[index - 1], vetor.lista[index]
            index = index - 1 
            time.sleep(tempo)
            vetor.qnt_sleep+= 1 
            fim = time.time() 
            vetor.tempoAni = fim - inicio
            vetor.tempoExe = vetor.tempoAni - (vetor.qnt_sleep * tempo)
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
  
def pancake_sort(vetor, tempo,inicio): 
    n = len(vetor.lista)
    curr_size = n 
    while curr_size > 1: 
        time.sleep(tempo)
        vetor.qnt_sleep+= 1 
        fim = time.time() 
        vetor.tempoAni = fim - inicio
        vetor.tempoExe = vetor.tempoAni - (vetor.qnt_sleep * tempo)
        mi = findMax(vetor.lista, curr_size, tempo) 
        if mi != curr_size-1: 
            flip(vetor.lista, mi, tempo) 
            flip(vetor.lista, curr_size-1, tempo) 
        curr_size -= 1
    return vetor.lista    

# Classe vetor, utilizada por todos os algoritmos
class vetor:
    def __init__(self, lista):
        self.lista = lista # Lista com os elementos não ordenados
        self.ordenado = False # Flag indicando se o algoritmo terminou de ordenar
        self.qnt_sleep = 0 # Quantidade de vezes que o algoritmo passou por um time.sleep
        self.tempoExe = 0 # Tempo total de execução do algoritmo, desconsiderando o tempo de pausa
        self.tempoAni = 0 # O Tempo total gasto pela animação, considerando o tempo de pausa

    def __str__(self):
        return self.nome
   
# Listbox das opções de algoritmos existentes
class App:
    def __init__(self, janela):
        self.janela = janela
        self.listbox = Listbox(self.janela, selectmode=MULTIPLE, width=13, justify=CENTER)
        self.listbox.pack()
        self.listbox.place(x=215, y=150)
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

# -----------------> TELA DE SIMULAÇÃO DOS ALGORITMOS
def tela_simulacao():
    # Recebe os parametros da tela principal
    global janela
    teste.passaParam()
    
    # Tratamento de possiveis erros de entrada do usuário
    if len(VALORES) != 2:
        showinfo("Erro no número de Algoritmos Selecionados!", "Escolha 2 Algoritmos para comparação.")
        return
    if int(varN.get()) <= 1:
        showinfo("Erro no tamanho do vetor inserido!", "Você escolheu um valor de n menor ou igual a 1 (vetor ordenado).")
        return
    
    # Fecha Tela Principal
    janela.destroy()
    
    # Configura nova Tela
    janela = Tk()
    janela.configure(background='black')
    janela.attributes('-fullscreen',True)
    janela.title("ANÁLISE E COMPLEXIDADE DE ALGORITMOS")
    janela.geometry("600x600+250+50")
    
    # Recebe as Entradas do usuário
    n = int(varN.get())  # Entrada do usuário - número de elementos
    tempo = tempoDeExecucao # Entrada do usuário - tempo de atraso para exibição da animação
    AlgoritmoA = VALORES[0]  # Algoritmo usada para comparação
    AlgoritmoB = VALORES[1]  # #Algoritmo usada para comparação
    
    # Cria vetor inicial - fixamos em 10.000 para não haver vetores com valores estratosféricos
    lista = np.random.randint(10000, size=n)
    algoritmosUsados = 2  # Permitiria (no futuro) a comparação de mais de um algoritmo
    
    # Cria uma cópia da lista para cada algoritmo simulado
    i = 0
    Vetores = []
    Figuras = []
    while (i < algoritmosUsados):
        listaProv = lista.copy()
        Vetores.append(vetor(listaProv))
        Figuras.append(Figure(dpi=80, facecolor='#105F10', linewidth=1.0))
        Figuras[i].add_subplot(111).plot(Vetores[i].lista)
        i = i + 1
        
    # Labels de Tempo - Parte Visual
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
    
    # Adiciona os gráficos de cada algoritmo na tela - Parte Visual
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

    # Exibe tempo de execução e animação - Parte Visual
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
    
    # Botão de retorno do Menu Principal
    menu_bt = Button(janela, text='Voltar/Menu Principal', command=tchauQuerida)
    menu_bt.pack()
    
    # Laço que permanece True enquanto houver vetores desordenados
    start = False
    while (Vetores[0].ordenado == False or Vetores[1].ordenado == False):
        # Atualiza o tempo de execução na tela
        labelTempoA_.configure(text=Vetores[0].tempoAni)
        labelTempoA__.configure(text=Vetores[0].tempoExe)
        labelTempoB_.configure(text=Vetores[1].tempoAni)
        labelTempoB__.configure(text=Vetores[1].tempoExe)
        
        # Atualiza o gráfico na tela
        Figuras[0].clear()
        Figuras[0].add_subplot(111).plot(Vetores[0].lista)
        canvas.draw()
        Figuras[0].canvas.flush_events()
        Figuras[1].clear()
        Figuras[1].add_subplot(111).plot(Vetores[1].lista)
        canvasB.draw()
        Figuras[1].canvas.flush_events()
        
        # Cria cada algoritmo em uma thread para rodar simultanêamente
        if start == False:
            start = True
            thread = minhaThread(0, Vetores[0], AlgoritmoA, tempo)
            thread.start()
            threadb = minhaThread(0, Vetores[1], AlgoritmoB, tempo)
            threadb.start()
            
    # Atualiza o gráfico com o resultado final
    time.sleep(1)        
    Figuras[0].clear()
    Figuras[0].add_subplot(111).plot(Vetores[0].lista)
    canvas.draw()
    Figuras[0].canvas.flush_events()
    Figuras[1].clear()
    Figuras[1].add_subplot(111).plot(Vetores[1].lista)
    canvasB.draw()
    Figuras[1].canvas.flush_events()            
    
    # Atualiza o tempo com o resultado final
    labelTempoA_.configure(text=Vetores[0].tempoAni)
    labelTempoA__.configure(text=Vetores[0].tempoExe)
    labelTempoB_.configure(text=Vetores[1].tempoAni)
    labelTempoB__.configure(text=Vetores[1].tempoExe)
    
    # Indica na tela qual "venceu"
    if Vetores[0].tempoExe < Vetores[1].tempoExe:
        vencedor = VALORES[0] + ' teve um menor tempo de execução!'
    elif Vetores[0].tempoExe > Vetores[1].tempoExe:
        vencedor = VALORES[1] + ' teve um menor tempo de execução!'
    elif Vetores[0].tempoExe == Vetores[1].tempoExe:
        vencedor = 'Empate técnico em tempo de execução!'
    labelVencedor = Label(janela, text=vencedor)
    labelVencedor.pack()
    labelVencedor.place(x=50, y=600)
        
    # Indica no prompt que o processamento foi finalizado
    print("Processamento finalizado")

# -----------------> FUNÇÃO PRINCIPAL
def menu():
    # Cria a Janela Principal
    global janela
    janela = Tk()
    label = Label(janela, text='ANÁLISE E COMPLEXIDADE DE ALGORITMOS')
    label.pack()
    
    # Label de número elementos
    labelIn = Label(janela, text='Insira o número de elementos')
    labelIn.place(x=170, y=50)
    
    # Input de elementos
    global varN
    varN = StringVar()
    inputN = Entry(janela, textvariable=varN, width=13, justify=CENTER)
    inputN.pack()
    varN.set(1000)
    inputN.place(x=215,y=85)
    
    # Input de Algoritmos Utilizados
    label.place(x=132, y=5)
    label2 = Label(janela, text='Selecione dois algoritmos')
    label2.place(x=185, y=120)
    
    # Input de Velocidade
    label3 = Label(janela, text='Selecione a velocidade da animação')
    label3.place(x=160, y=325)
    global teste 
    teste = App(janela)
    
    # Seleção de Velocidade 
    def radCall():
        global tempoDeExecucao
        radSel = radVar.get()
        if radSel == 1:
            print("selecionei 1")
            tempoDeExecucao = 0
        elif radSel == 2:
            tempoDeExecucao = 0.2
        elif radSel == 3:
            tempoDeExecucao = 1
    radVar = IntVar()
    rad1 = Radiobutton(janela, text='Tempo Real', variable=radVar, value=1, command=radCall)
    rad2 = Radiobutton(janela, text='Atraso Curto', variable=radVar, value=2, command=radCall)
    rad3 = Radiobutton(janela, text='Atraso Longo', variable=radVar, value=3, command=radCall)
    rad1.place(x=130, y=355)
    rad2.place(x=220, y=355)
    rad3.place(x=310, y=355)
    rad1.select()
    
    # Botão de simulação
    menu_bt_simular = Button(janela, text='Simular', command=tela_simulacao)
    menu_bt_simular.place(x=230, y=390)
    
    # Configuração da Janela
    janela.geometry("500x435+250+50")
    janela.title("ANÁLISE E COMPLEXIDADE DE ALGORITMOS")
    janela.configure(background='black')
    janela.mainloop()

# -----------------> FUNÇÃO QUE VOLTA PARA A TELA PRINCIPAL
def tchauQuerida():
    janela.destroy()
    menu()
    
if __name__ == '__main__':
    menu()
