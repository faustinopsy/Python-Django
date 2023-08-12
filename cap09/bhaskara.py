""" Importação do módulo matemático e leitura das variáveis de entrada do problema"""
import math
a = int(input('Digite o coeficiente a:'))
b = int(input('Digite o coeficiente b:'))
c = int(input('Digite o coeficiente c:'))

def delta(a, b, c):
""" Funçao que calcula o valor do discriminante (delta) """
    resultado = b ** 2 -4 * a * c
    return resultado

def raiz1(a, b, c):
""" Funçao que calcula o valor da primeira raiz da equaçao (x') """
    resultado = (-b + math.sqrt(delta(a, b, c))) / (2 * a)
    return resultado

def raiz2(a, b, c):
""" Funçao que calcula o valor da primeira raiz da equaçao (x'') """
    resultado = (-b - math.sqrt(delta(a, b, c))) / (2 * a)
    return resultado

discriminante = delta(a, b, c)
if discriminante < 0.0:
    print('A equação não tem raízes reais!')
elif discriminante == 0.0:
    raiz = raiz1(a, b, c)
    print(f'A equação possui duas raízes idênticas, de valor {raiz}.')
else:
    raiz1 = raiz1(a, b, c)
    raiz2 = raiz2(a, b, c)
    print(f'A equação possui duas raízes reais, de valores {raiz1} e {raiz2}.')
