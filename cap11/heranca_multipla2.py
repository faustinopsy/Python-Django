""" Exemplo de uso de herança múltipla em Python com uma propriedade 'nome' definida na classe ancestral
    e na classe filha """
class Pessoa:
    def __init__(self):  
        self.nome = 'João'  
        self.idade = 25  

    def nome(self):  
        return self.nome  
  
  
class Aluno:  
    def __init__(self):  
        self.nome = 'José'  
        self.matricula = '555'  
  
    def nome(self):  
        return self.nome  
  
  
class Residente(Pessoa, Aluno):  
    def __init__(self):  
        Pessoa.__init__(self)  
        Aluno.__init__(self)  

    def getNome(self):  
        return self.nome
