""" Comparação entre passagem de argumentos por referência e por valor """
def quadrado_por_valor(x):
    """Eleva x ao quadrado,  usando passagem por valor"""
    print(f'Recebido o valor {x}')
    x = x * x
    print(f'Devolvido o valor {x}')
    return x

def quadrado_por_ref(lista, x):
    """ Recebe uma lista e um valor x """
    """ Eleva x ao quadrado, e armazena-o na lista,
        usando passagem por referência"""
    print(f'Recebido o valor {x}')
    x = x * x
    lista.append(x)
    print(f'Devolvido o valor {x}')
    return

dummy = 4
print(f'dummy vale {dummy}')
print('Elevando dummy ao quadrado:')
print('por valor:')
print(quadrado_por_valor(dummy))
print(f'Apos a execuçao de quadrado_por_valor(dummy), dummy agora vale {dummy}')
print('por referência:')
l = []
print(quadrado_por_ref(l, dummy))
print(f'Apos a execuçao de quadrado_por_ref(dummy), dummy agora vale {l[0]}')
