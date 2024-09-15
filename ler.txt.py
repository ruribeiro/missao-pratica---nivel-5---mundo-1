# Abre o arquivo txt e armazena seu conteúdo em uma variável
arquivo = open('loremipsum.txt', 'r')
conteudo = arquivo.read()
arquivo.close()

# Imprime todo o conteúdo da variável (e do arquivo txt)
print(conteudo)

# Imprime apenas a primeira linha do arquivo txt
primeira_linha = conteudo.split('\n')[0]
print(primeira_linha)

# Imprime apenas os 3 primeiros caracteres do arquivo txt
primeiros_caracteres = conteudo[:3]
print(primeiros_caracteres)

# Utiliza a instrução "with" para abrir o arquivo txt e imprimir seu conteúdo
with open('loremipsum.txt', 'r') as arquivo:
    conteudo_com_with = arquivo.read()
    print(conteudo_com_with)