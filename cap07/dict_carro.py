print("Criando um dicionario para armazenar os dados de um carro...")
carro = {
    'marca' : 'Hyundai',
    'modelo' : 'HB20',
    'ano': 2015,
    'motorizacao': 1.6,
    'cambio': 'automático',
    'acessorios':[],
}
print("Dicionario criado!", carro)
carro['ano']=2018
carro['modelo']='HB20 R-Spec'
print("Troquei de carro - comprei um mais novo!", carro)
print("Colocando acessorios no carro:")
carro['acessorios'] = ['alarme']
print("Instalei um alarme novo:", carro)
carro['acessorios'].append('som')
print("Coloquei um novo som:", carro)
carro['acessorios'][1] = 'som diferente'
print("Troquei o modelo do som:", carro)
