from collections import OrderedDict
lista_duplicados = ['Alice', 'Bob', 'Carl', 'Bob', 'Alice', 'Carl']
print(f'Conteúdo inicial da lista: {lista_duplicados}')
print('Convertendo a lista em conjunto para eliminar duplicidades...')
s1 = set(lista_duplicados)
print('Convertendo o conjunto em uma lista sem duplicações...')
lista1 = list(s1)
print(f'Conteúdo da lista sem valores duplicados: {lista1}')
