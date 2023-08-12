resultado_exercicio = float(input('Entre com o valor do resultado do exercicio contabil anterior: '))
if (resultado_exercicio >= 0):
    print(f'Houve lucro de R$ %.2f'%resultado_exercicio)
else:
    resultado_exercicio = abs(resultado_exercicio)
    print(f'Houve prejuizo de R$ %.2f'%resultado_exercicio)
