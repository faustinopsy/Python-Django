""" TAD Pilha """
from typing import List
elementos = []

def push(elemento)->None:
    """ Adiciona um elemento a pilha """
    elementos.append(elemento)

def pop()->'elemento do topo da pilha':
    """ Retira o elemento do topo da pilha, retornando-o """
    return elementos.pop()

def is_empty()->bool:
    """ Devolve True ou False, dependendo se a pilha estiver vazia ou nao """
    resultado = True
    if elementos == []:
        resultado = True
    else:
        resultado = False 
    return resultado

def get_elementos()->List:
    """ Retorna os elementos da pilha, armazenados em uma lista """
    return elementos

def tamanho()->int:
    """ Retorna o tamanho da pilha """
    return len(elementos)

# Testando os metodos:
print('A pilha esta, inicialmente, vazia: ')
print(f'is_empty: {is_empty()}')
print('Colocando uma string na pilha: ')
push('Abracadabra')
print(f'Conteudo da pilha: {get_elementos()}')
print('Colocando dois numeros na pilha: ')
push(123)
push(3.141596)
print(f'Conteudo da pilha: {get_elementos()}')
print(f'Tamanho atual da pilha: {tamanho()}')
print(f'Removido o elemento {pop()} da pilha.')
print(f'Conteudo da pilha: {get_elementos()}')
print(f'A pilha ainda contem elementos: is_empty() = {is_empty()}')
