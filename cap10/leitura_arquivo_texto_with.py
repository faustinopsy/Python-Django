""" Leitura de dados em arquivo de texto, linha por linha """
""" Conteúdo original – listagem 10.1:
arquivo = open('contatos.txt', 'r+')
print('O conteúdo de contatos.txt é:')
while True:
    linha = arquivo.readline()
    if (linha != ""):
        print(linha, end='')   # readline() acrescenta um \n ao final,
    else:                      # por isso, end='' remove o \n de print()
        break
arquivo.close()
============ com a função with() ======================
"""
with open('contatos.txt', 'r+') as arquivo:
    for linha in arquivo:
        print(linha, end='')
