def escrever_em_arquivo(nome_arquivo, lista_de_frases):
  
  with open(nome_arquivo, 'w') as arquivo:
    for frase in lista_de_frases:
      arquivo.write(frase + '\n')

# Criando a lista de frases
lista_frases = ["hoje foi um bom dia.", "quase perdi o prazo do trabalho.", "inefavel e um coisa que nao pode ser explicada."]

# Chamando a função para escrever no arquivo
escrever_em_arquivo("texto.txt", lista_frases)