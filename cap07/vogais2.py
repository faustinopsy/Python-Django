vogais = ['a','e','i','o','u','A','E','I','O','U']
outros = []
indice = 0
entrada = input('Digite a palavra a ser filtrada: ')
while indice < len(entrada):
    letra = entrada[indice]
    indice = indice + 1
    if letra not in vogais:
        outros.append(letra)
if len(outros) > 0:
    print(f'A palavra {entrada} possui {len(outros)} caracteres que nao sao vogais!')
else:
    print(f'A palavra {entrada} possui apenas vogais.')
