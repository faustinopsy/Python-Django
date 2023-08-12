""" Exemplo de módulo personalizado """
import math

def area_triangulo(base: float, altura: float) -> float:
    """ Calcula a área de um triângulo, dados sua base e altura """
    resultado = (base * altura) / 2
    return resultado

def area_circulo(raio: float) -> float:
    """ Calcula a área de um círculo, dado seu raio """
    resultado = math.pi * (raio ** 2)
    return resultado
