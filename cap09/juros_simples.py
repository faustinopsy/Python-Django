def calcula_juros(principal, meses, taxa=0.5):
    """ Cálculo de juros simples """
    resultado = (principal * taxa * meses) / 100.0
    return resultado

print('Calculando os juros de R$ 100,00 a 5% por 3 meses:')
print(f'R$ {calcula_juros(100.0,5,3)}')
