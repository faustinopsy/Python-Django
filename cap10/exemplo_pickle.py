""" Gravando e recuperando um dicionario com o Pickle """
import pickle

usuarios = {
    '1234-5' : 'Alice',
    '1235-6' : 'Bob',
    '1236-7' : 'Charlie',
}

print(f'A coleçao {usuarios} sera salva num arquivo.')
arquivo = open('dados.dat','w+b')
pickle.dump(usuarios, arquivo)
arquivo.close()
print('Lendo os dados do arquivo:')
arquivo = open('dados.dat','rb')
usuarios = pickle.load(arquivo)
arquivo.close()
print(f'Usuarios: {usuarios}')
print(f'Nome do usuario de chave 1234-5: {usuarios["1234-5"]}')
