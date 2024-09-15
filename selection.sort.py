# Criando uma lista com 15 números
numeros = [10, 5, 8, 32, 4, 16, 9, 7, 22, 11, 15, 2, 25, 18, 6]

def selection_sort(array):
  
  for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
      if array[min_index] > array[j]:
        min_index = j
 # Troca os elementos
    array[i], array[min_index] = array[min_index], array[i]

selection_sort(numeros)

print("Array ordenado:", numeros)