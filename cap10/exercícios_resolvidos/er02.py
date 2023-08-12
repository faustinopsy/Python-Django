""" Lendo configuraçoes a partir de um arquivo com o Pickle """
import pickle

def ler_configuracao()->None:
    arquivo = open('config.dat','rb')
    conteudo = pickle.load(arquivo)
    arquivo.close()
    print(f'Conteudo do arquivo: {conteudo}')


ler_configuracao()
