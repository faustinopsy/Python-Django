""" Exceção lançada quando se tenta realizar uma saída do estoque para a qual
    não há quantidade suficiente do produto disponível """
class EstoqueInsuficienteException(BaseException):
    def __init__(self, mensagem): 
        self.mensagem = mensagem 
 
    def __str__(self): 
        return self.mensagem
