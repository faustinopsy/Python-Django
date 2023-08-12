vogais = ['a','e','i','o','u','A','E','I','O','U']
outros = []
entrada = input('Digite a palavra a ser filtrada: ')
for letra in entrada:
    if letra not in vogais:
        outros.append(letra)
if len(outros) > 0:
    print(f'A palavra {entrada} possui {len(outros)} caracteres que nao sao vogais!')
else:
    print(f'A palavra {entrada} possui apenas vogais.')
