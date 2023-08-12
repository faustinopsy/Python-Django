impares = [1,3,5,7,9]

def sao_impares(lista):
    resultado = True
    for num in lista:
        if (num % 2) == 0:
            resultado = False
    return resultado

print(sao_impares(impares))
    
