""" Classe que representa um documento """
import datetime

class Documento:

    def __init__(self, numero:str, data_criacao:datetime, resumo:str)->None:
        self.__numero = numero
        self.__data_criacao = data_criacao
        self.__resumo = resumo

    def __str__(self)->str:
        resultado = '\nDocumento n.:' + self.__numero + '\n'
        resultado += 'Data de criaçao:' + datetime.datetime.strftime(self.__data_criacao,'%d/%m/%Y') + '\n'
        resultado += 'Resumo:' + self.__resumo + '\n'
        return resultado

    @property
    def numero(self)->str:
        return self.__numero

    @property
    def data_criacao(self)->datetime:
        return self.__data_criacao

    @property
    def resumo(self)->str:
        return self.__resumo

    @resumo.setter
    def resumo(self, resumo: str)->None:
        if (resumo=='') or (resumo == None):
            print('Erro: Um resumo deve ser fornecido.')
        else:
            self.__resumo = resumo

