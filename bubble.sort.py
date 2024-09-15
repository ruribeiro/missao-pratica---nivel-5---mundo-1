def bubble_sort(array):
  
  for i in range(len(array)):
    for j in range(0, len(array) - i - 1):
      if array[j] > array[j + 1]:
        # Troca os elementos de lugar
        temp = array[j]
        array[j] = array[j + 1]
        array[j + 1] = temp

# Criando uma lista com 15 números
numeros = [10, 5, 8, 32, 4, 16, 9, 7, 22, 11, 15, 2, 25, 18, 6]

# Aplicando o Bubble Sort
bubble_sort(numeros)

print("Array ordenado:", numeros)