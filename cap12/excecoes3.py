""" Tratamento de exceções """
try:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    resultado = n1/n2

except ZeroDivisionError:
    print('Nao e possivel dividir por zero.')

except ValueError:
    print('Digite um inteiro valido.')

except:
    print('Entrada invalida.')

else:
    print(f'A entrada executou sem erros. A divisao de {n1} por {n2} resulta em {resultado}.')

finally:
    print('O programa terminou!')
