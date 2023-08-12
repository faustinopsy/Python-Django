""" Exemplo de classe abstrata """
from abc import ABC, abstractmethod

class CriadorAbstratoDePeca(ABC):
    """ Classe abstrata que define as etapas para criar uma peça juridica """

    def executar(self):
        self.adicionar_reus()
        self.adicionar_testemunhas()
        self.adicionar_vitimas()

    @abstractmethod
    def adicionar_reus(self):
        pass
    
    @abstractmethod
    def adicionar_testemunhas(self):
        pass

    @abstractmethod
    def adicionar_vitimas(self):
        pass
