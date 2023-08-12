""" Classe que implementa um cadastro de produtos """
""" PROPOSITALMENTE, esta classe esta mal projetada """
from produto5 import Produto

class CadastroProdutos:

    def __init__(self):
        self.__repositorio_produtos = []

    def __getitem__(self, indice)->Produto:
        return self.__repositorio_produtos[indice]
        
    @property
    def repositorio_produtos(self)->'Coleção que armazena os produtos':
        return self.__repositorio_produtos

    def _existe(self, produto: Produto)->bool:
        resultado = False
        if produto in self.__repositorio_produtos:
            resultado = True
        return resultado
        
    def cadastrar(self, produto: Produto)->None:
        if not self._existe(produto):
            self.repositorio_produtos.append(produto)
        else:
            print('Produto ja cadastrado!')

    def alterar(self, produto: Produto)->None:
        pass

    def excluir(self, produto: Produto)->None:
        pass

    def consultar(self, produto: Produto)->None:
        pass

    def entradaEstoque(self, produto: Produto)->None:
        pass

    def saidaEstoque(self, produto: Produto)->None:
        pass

    def retornarProdutosEstoqueZerado(self, produto: Produto)->None:
        pass

