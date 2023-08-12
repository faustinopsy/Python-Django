""" Tratamento de exceções - exemplo de propagação de erro com raise """
try:
    with open('abcxyz.txt', 'r') as arquivo:
        for linha in arquivo:
            print(linha, end='')
            
except ZeroDivisionError:
    print('Não e possivel dividir por zero.')

except ValueError:
    print('Digite um inteiro válido.')

except:
    print('Erro inesperado.')
    raise

else:
    print('O programa executou sem erros.')
