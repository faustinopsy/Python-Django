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

    def get_codigo(self)->int:
        return self.__codigo

    def set_codigo(self, codigo: int)->None:
        self.__codigo = codigo

    def get_descricao(self)->str:
        return self.__descricao

    def set_descricao(self, descricao: str)->None:
        self.__descricao = descricao

    def get_preco(self)->float:
        return self.__preco

    def set_preco(self, preco: float)->None:
        self.__preco = preco

    def get_quantidade_estoque(self)->float:
        return self.__quantidade_estoque

    def set_quantidade_estoque(self, quantidade_estoque: float)->None:
        self.__quantidade_estoque = _quantidade_estoque

