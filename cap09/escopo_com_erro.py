def func(a: int, b: int)->None:
    print(f'Foram recebidos os parâmetros a={a} e b={b}.')
    z = 5

func(1,2)
print(f'O valor de z é {z}')    # Erro aqui: NameError: name 'z' is not defined 
