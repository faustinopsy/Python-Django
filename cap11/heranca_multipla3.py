""" Exemplo de uso de herança múltipla em Python com uma propriedade 'nome' definida na classe ancestral
    e na classe filha """

		
class Pessoa:  
    def __init__(self):  
        super().__init__()  
        self.nome = 'João'  
        self.idade = 25  
  
    def getNome(self):  
        return self.nome  
  
  
class Aluno:  
    def __init__(self):  
        super().__init__()  
        self.name = 'José'  
        self.matricula = '555'  
  
    def getNome(self):  
        return self.nome  
  
  
class Residente(Pessoa, Aluno):  
    def __init__(self):  
        super().__init__()  
  
    def getNome(self):  
        return self.nome  
  
residente1 = Residente()  
print(residente1.getNome())  
