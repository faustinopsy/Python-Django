""" Leitura de dados em arquivo de texto, linha por linha """
arquivo = open('contatos.txt', 'r+')
print('O conteúdo de contatos.txt é:')
while True:
    linha = arquivo.readline()
    if (linha != ""):
        print(linha, end='')    # readline() acrescenta um \n ao final,
    else:                       # por isso, end='' remove o \n de print()
        break
arquivo.close()
