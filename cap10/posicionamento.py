"""
    Poisicionando-se em um arquivo texto com o uso de seek() e tell()
"""
import os

arquivo = 'teste_seek.txt'
handler = open(arquivo, 'w')
handler.write("Testando o uso do metodo seek().\nEsta e a segunda linha do arquivo\nE esta, a terceira.")
handler.close()

handler = open(arquivo, 'r')
print(f'Apos abrir o arquivo para leitura, a posiçao inicial do manipulador e {handler.tell()}.')
linha = handler.readline()
print(f'Linha 1: {linha}')
print(f'Apos ler a primeira linha, o manipulador esta na posiçao {handler.tell()}.')
print('Voltando o manipulador 24 bytes a partir da posiçao atual e lendo uma linha a partir dai:')
handler.seek(handler.tell()-24, os.SEEK_SET)
linha = handler.readline()
print(f'Linha lida: {linha}')
print('Posicionando o manipulador 33 bytes a partir do inicio do arquivo e lendo uma linha:')
handler.seek(33, os.SEEK_SET)
linha = handler.readline()
print(f'Linha lida: {linha}')
