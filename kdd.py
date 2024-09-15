import time

#variável do tipo lista
palavras = list()

# Leia o conteúdo do arquivo "texto.txt" linha-a-linha
with open('texto.txt', 'r') as arquivo:
    for linha in arquivo:
        # Separe cada linha lida em palavras
        palavras.extend(linha.split())

# Função para ordenação Bubble Sort
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Função para ordenação Selection Sort
def selection_sort(lista):
    for i in range(len(lista)):
        min_idx = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

# Medir o tempo de execução do Bubble Sort
inicio = time.time()
palavras_bubble = bubble_sort(palavras.copy())
fim = time.time()
print("Bubble Sort:", palavras_bubble)
print("Tempo de execução do Bubble Sort:", fim - inicio, "segundos")

# Medir o tempo de execução do Selection Sort
inicio = time.time()
palavras_selection = selection_sort(palavras.copy())
fim = time.time()
print("Selection Sort:", palavras_selection)
print("Tempo de execução do Selection Sort:", fim - inicio, "segundos")

# Medir o tempo de execução do método sort nativo do Python
inicio = time.time()
palavras_sort = sorted(palavras)
fim = time.time()
print("Sort nativo do Python:", palavras_sort)
print("Tempo de execução do método sort nativo do Python:", fim - inicio, "segundos") 