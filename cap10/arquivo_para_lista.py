""" btendo dados de um arquivo texto e armazenando-os em uma lista  """
arquivo = open('contatos.txt', 'a+')
lista = arquivo.readlines()
print(f'A lista contem: {lista}')
arquivo.close()
