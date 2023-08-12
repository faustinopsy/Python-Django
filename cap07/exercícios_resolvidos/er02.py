fila = []
quantidade_clientes = 0
while True:
    opcao = ''
    print('\n' * 100)               # Limpa a tela
    print('Menu do Sistema:')
    print('1. Incluir cliente na fila')
    print('2. Listar pessoas na fila')
    print('3. Atender o próximo cliente')
    print('4. Sair do programa')
    opcao = int(input('Sua escolha -> '))
    if opcao == 1:
        quantidade_clientes = quantidade_clientes + 1
        print('\n' * 100)           #         Limpa a tela
        nome = input('Digite o nome do cliente: ')
        rg = input('Digite o RG do cliente: ')
        cliente = {
            'nome': nome,
            'rg': rg
        }
        fila.append(cliente)
    elif opcao == 2:
        if len(fila) >0 :
            print('\n' * 100)           #         Limpa a tela
            for indice in range(0, len(fila)):
                print(f'{indice + 1} - {fila[indice]["rg"]} - {fila[indice]["nome"]}')
            input('Tecle <enter> para retornar ao menu...')
        else:
            print('Fila vazia !')
            input('Tecle <enter> para retornar ao menu...')
    elif opcao == 3:
        if len(fila) >0 :
            print('\n' * 100)           #         Limpa a tela
            cliente = fila.pop(0)
            print(f'Atendendo o cliente: {cliente["nome"]} - RG: {cliente["rg"]}')
            print(f'Restam {len(fila)} clientes na fila.')
            input('Tecle <enter> para retornar ao menu...')
        else:
            print('Fila vazia !')
            input('Tecle <enter> para retornar ao menu...')
    elif opcao == 4:
        break
print("Programa finalizado pelo usuario.")
