""" Tratando exceções """

try:
    with open('abcxyz.txt', 'r') as arquivo:
        for linha in arquivo:
            print(linha, end='')
except IOError:
    print('Arquivo abcxyz.txt nao encontrado.')
