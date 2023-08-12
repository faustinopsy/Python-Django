""" Exemplo de uso de herança múltipla em Python"""
class Pessoa:
    """ Classe ancestral - representa uma pessoa """

    def __init__(self, nome: str, idade: int) -> None:  
        self.__nome = nome  
        self.__idade = idade  

    def __str__(self)->str:
        resultado = '\nNome: ' + self.nome
        resultado += '\nIdade: ' + str(self.idade)
        return resultado
    
    @property
    def nome(self)->str:  
        return self.__nome

    @nome.setter
    def nome(self, nome:str)->None:
        self.__nome = nome
    
    @property
    def idade(self)->int:
        return self.__idade

    @idade.setter
    def idade(self, idade:int)->None:
        self.__idade = idade
  
class Estudante:
    """ Classe que representa o papel de estudante, desempenhado por uma pessoa """
    def __init__(self, matricula: str)->None:  
        self.__matricula = matricula  

    def __str__(self)->str:
        resultado = '\nMatricula: ' + self.matricula
        return resultado
    
    @property
    def matricula(self)->str:  
        return self.__matricula
  
  
class Residente(Pessoa, Estudante):
    """ Um residente e, ao mesmo tempo, pessoa e estudante: """
    def __init__(self, nome: str, idade: int, matricula: str)->None:  
        Pessoa.__init__(self, nome, idade)
        Estudante.__init__(self, matricula)  

    def __str__(self)->str:
        resultado = Pessoa.__str__(self)
        resultado += Estudante.__str__(self)
        return resultado

