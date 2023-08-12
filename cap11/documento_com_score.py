""" Classe que representa um documento com o conceito de score """
import datetime

class Documento:

    def __init__(self, numero:str, data_criacao:datetime, resumo:str)->None:
        self.__numero = numero
        self.__data_criacao = data_criacao
        self.__resumo = resumo
        self.__score = 0

    def __str__(self)->str:
        resultado = '\nDocumento n.:' + self.__numero + '\n'
        resultado += 'Data de criaçao:' + datetime.strftime(self.__data_criacao,'%d/%m/%Y') + '\n'
        resultado += 'Resumo:' + self.__resumo + '\n'
        resultado += 'Score:' + self.__score + '\n'
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

    @property
    def score(self)->int:
        return self.__score


""" Classe que representa um oficio circular """
import datetime
import time   # Necessario para usar strftime()
from documento import Documento

class OficioCircular(Documento):

    def __init__(self, numero:str, data_criacao:datetime, resumo:str, texto: str, data_limite: datetime, destinatarios:'lista de destinatarios')->None:
        super().__init__(numero, data_criacao, resumo)
        self.__texto = texto
        self.__data_limite = data_limite
        self.__destinatarios = destinatarios

    def __str__(self)->str:
        resultado = super().__str__()
        resultado += 'Texto: ' + self.texto + '\n'
        resultado += 'Data limite para envio: ' + self.data_limite.strftime('%d/%m/%Y') + '\n'
        resultado += 'Destinatarios: \n'
        resultado += ', '.join(self.destinatarios) + '\n'
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
    def data_limite(self)->datetime:
        return self.__data_limite

    @data_limite.setter
    def data_limite(self, data_limite: datetime)->None:
        if (data_limite==None):
            print('Erro: Uma data limite para envio deve ser fornecida.')
        else:
            self.__data_limite = data_limite

    @property
    def destinatarios(self)->'lista de destinatarios':
        return self.__destinatarios

    @destinatarios.setter
    def destinatarios(self, destinatarios: 'Lista de destinatarios')->None:
        self.__destinatarios = destinatarios

    def is_vencido(self)->bool:
        resultado = self.__is_vencido(self)
        return resultado

    def __is_vencido(self)->bool:
        hoje = datetime.date.today()
        resultado = False
        if(self.__data_limite < hoje):
            resultado = True
        return resultado

    def __enviar_copia(self)->None:
        pass

    @property
    def score(self)->int:
        resultado = len(self.destinatarios) + len(self.texto)
        return resultado


""" Classe que representa uma CI """
import datetime
from documento import Documento
from datetime import datetime

class CI(Documento):

    def __init__(self, numero:str, resumo:str, texto: str, destinatarios:'lista de destinatarios')->None:
        data_criacao = datetime.now()
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

    @property
    def score(self)->int:
        resultado = len(super().resumo) + 2
        return resultado
