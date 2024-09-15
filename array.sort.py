import random

# Array de números 
numeros = [random.randint(1, 100) for _ in range(15)]

# Ordenando em ordem crescente
numeros.sort()
print("Números em ordem crescente:", numeros)

# Ordenando em ordem decrescente
numeros.sort(reverse=True)
print("Números em ordem decrescente:", numeros)

# Array 
pessoas = ["rafael", "ribeiro", "Pedro", "josiane", "claudio"]

# Ordenando em ordem alfabética (crescente)
pessoas.sort()
print("Pessoas em ordem alfabética:", pessoas)

# Ordenando em ordem alfabética inversa (decrescente)
pessoas.sort(reverse=True)
print("Pessoas em ordem alfabética inversa:", pessoas)

#Array de strings representando dados pessoais
pessoas2 = [
    {"nome": "João", "dataNascimento": "01/01/1990", "cpf": "12345678901", "rg": "12345678"},
    {"nome": "Maria", "dataNascimento": "15/03/1985", "cpf": "98765432109", "rg": "87654321"},
    
]

# Ordenando por nome (ordem alfabética)
pessoas2.sort(key=lambda x: x["nome"])
print("Pessoas ordenadas por nome:", pessoas)

# Ordenando por data de nascimento (assumindo formato DD/MM/AAAA)
# Note que essa ordenação pode não ser precisa para todos os formatos de data
pessoas2.sort(key=lambda x: x["dataNascimento"])
print("Pessoas ordenadas por data de nascimento:", pessoas)