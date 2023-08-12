""" Leitura de dados em arquivo de texto """
arquivo = open('contatos.txt', 'r')
conteudo = arquivo.read()
print(f'O conteudo de contatos.txt e: \n{conteudo}')
arquivo.close()

