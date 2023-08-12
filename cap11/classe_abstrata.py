""" Exemplo de classe abstrata """
from abc import ABC

class CriadorAbstratoDePeca(ABC):
    """ Classe abstrata que define as etapas para criar uma peça juridica """

    def executar(self):
        self.adicionar_reus()
        self.adicionar_testemunhas()
        self.adicionar_vitimas()

    def adicionar_reus(self):
        pass
    
    def adicionar_testemunhas(self):
        pass

    def adicionar_vitimas(self):
        pass
