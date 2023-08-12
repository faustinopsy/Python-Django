""" Gravando configuraçoes em um arquivo com o Pickle """
import pickle

def salvar_configuracao(nome_proprietario: str, numero_serie: str, endereco_mac: str)->None:
    arquivo = open('config.dat','w+b')
    registro = {
        'nome_proprietario' : nome_proprietario,
        'numero_serie' : numero_serie,
        'endereco_mac' : endereco_mac,
    }
    pickle.dump(registro, arquivo)
    arquivo.close()


salvar_configuracao('Francisco', '1234-5', '19:04:73:8c:4d:a8')

