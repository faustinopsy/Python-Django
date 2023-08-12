""" Classe que representa um produto """


class Produto:

    def __init__(self, codigo: int, descricao:str, preco: float, quantidade_estoque: float)->None:
        self.__codigo = codigo
        self.__descricao = descricao
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque
        
    def entrada_estoque(self, quantidade: float)->None:
        self.__quantidade_estoque += quantidade

    def saida_estoque(self, quantidade: float)->None:
        self.__quantidade_estoque -= quantidade

    def visualizar_quantidade_em_estoque(self)->None:
        print(f'A quantidade em estoque é {self.__quantidade_estoque}')
