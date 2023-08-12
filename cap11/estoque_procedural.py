""" Criação de produtos de maneira procedural """

def cria_produto(codigo: int, descricao: str, preco:float, quantidade_estoque:float)->None:
    produto = {
        'codigo': codigo,
        'descricao':descricao,
        'preco': preco,
        'quantidade_estoque': quantidade_estoque
        }
    return produto

def entrada_estoque(produto: dict, quantidade: float)->None:
    produto['quantidade_estoque'] += quantidade

def saida_estoque(produto: dict, quantidade: float)->None:
    produto['quantidade_estoque'] -= quantidade

def visualizar_quantidade_em_estoque(produto: dict)->None:
    print(f'A quantidade em estoque e {produto["quantidade_estoque"]}')
