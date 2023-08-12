""" Usando uma variavel local e outra global com o mesmo nome """

x = 10

def teste()->None:
    x = 20
    print(f'Acessada a variavel local x: {x}')

teste()
print(f'Acessada a variavel global x: {x}')
