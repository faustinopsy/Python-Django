from cadastro_produtos2 import CadastroProdutos
from produto5 import Produto


cadastro = CadastroProdutos()
umProduto = Produto(123, 'Serra Circular', 500.00)
cadastro.cadastrar(umProduto)

outroProduto = Produto(124, 'Plaina', 27.50)
cadastro.cadastrar(outroProduto)
for p in cadastro:
    print(p.descricao)
