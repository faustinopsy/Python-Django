""" Exemplo de variável global """

x = "123"    # Definição fora do corpo da função – variável global

def testar()->None:
    x = x + "456"
    print(f'Valor de x dentro da funçao testar(): {x}')

testar()
print(f'Valor de x fora da funçao testar(): {x}')
