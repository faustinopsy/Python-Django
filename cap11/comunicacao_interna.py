""" Classe que representa uma CI """
import datetime
from documento import Documento

class CI(Documento):

    def __init__(self, numero:str, resumo:str, texto: str, destinatarios:'lista de destinatarios')->None:
        data_criacao = datetime.datetime.now()
        super().__init__(numero, data_criacao, resumo)
        self.__texto = texto
        self.__destinatarios = destinatarios

    def __str__(self)->str:
        resultado = super().__str__()
        resultado += 'Texto: ' + self.__texto + '\n'
        resultado += 'Destinatarios: \n'
        resultado += ', '.join(self.__destinatarios)
        return resultado
        
    @property
    def texto(self)->str:
        return self.__texto

    @texto.setter
    def texto(self, texto: str)->None:
        if (texto=='') or (texto == None):
            print('Erro: Um texto deve ser fornecido.')
        else:
            self.__texto = texto

    @property
    def destinatarios(self)->'lista de destinatarios':
        return self.__destinatarios

    @destinatarios.setter
    def destinatarios(self, destinatarios: 'Lista de destinatarios')->None:
        self.__destinatarios = destinatarios

