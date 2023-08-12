""" Classe que representa um produto """


class Produto:

    def __init__(self, codigo: int, descricao:str, preco: float, quantidade_estoque: float)->None:
        self.codigo = codigo
        self.descricao = descricao
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque
        
    def entrada_estoque(self, quantidade: float)->None:
        self.quantidade_estoque += quantidade

    def saida_estoque(self, quantidade: float)->None:
        self.quantidade_estoque -= quantidade

    def visualizar_quantidade_em_estoque(self)->None:
        print(f'A quantidade em estoque e {self.quantidade_estoque}')
