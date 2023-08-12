""" Agenda de contatos """
contatos = []

def limpar_tela()->None:
    print('\n' * 100)   # limpa a tela

    
def menu()->'Opçao selecionada':
    limpar_tela()
    print('Agenda de contatos - selecione uma opçao:')
    print('[1] Incluir')
    print('[2] Editar')
    print('[3] Excluir')
    print('[4] Localizar por nome')
    print('[5] Listar telefones')
    print('[6] Sair')
    opcao = input('Sua escolha ->')
    return int(opcao)


def cria_contato()->dict:
    """ Obtem os dados de um contato e devolve um dicionario
        populado com eles """
    limpar_tela()
    nome = input('Digite o nome do contato: ')
    fone = input('Digite o fone do contato: ')
    contato = {
        'nome': nome,
        'fone': fone
    }
    return contato


def buscar_indice_por_nome(nome)->int:
    """ Busca um contato pelo nome e devolve seu indice; se nao existir, retorna -1 """
    resultado = -1
    indice = 0
    while (indice < len(contatos)) and (resultado == -1):
        if(contatos[indice]['nome']==nome):
            resultado = indice
        else:
            indice = indice + 1
    return resultado


def incluir()->None:
    """ Inclui um novo contato na agenda """
    contato = cria_contato()
    contatos.append(contato)
    input('Registro incluido. Tecle <enter>...')


def editar()->None:
    """ Altera o telefone de um contato, se existir algum com o numero fornecido """
    contato = cria_contato()
    posicao = buscar_indice_por_nome(contato['nome'])
    if(posicao != -1):
        contatos[posicao] = contato
        input('Registro alterado. Tecle <enter>...')
    else:
        limpar_tela()
        input('Contato nao encontrado. Tecle <enter>...')


def excluir()->None:
    nome = input('Informe o nome do contato a excluir: ')
    posicao = buscar_indice_por_nome(nome)
    limpar_tela()
    if(posicao != -1):
        print(f'Removido o item {contatos[posicao]} da agenda.')
        input('Tecle <enter>...')
        contatos.pop(posicao)
    else:
        input('Contato nao encontrado. Tecle <enter>...')


def buscar_por_nome()->None:
    nome = input('Informe o nome do contato: ')
    posicao = buscar_indice_por_nome(nome)
    limpar_tela()
    if(posicao != -1):
        limpar_tela()
        print('Contato encontrado: ')
        print(f'Nome: {contatos[posicao]["nome"]} - Telefone: {contatos[posicao]["fone"]}')
        input('Tecle <enter>...')
        contatos.pop(posicao)
    else:
        input('Contato nao encontrado. Tecle <enter>...')


def localizar_por_nome(nome)->dict:
    posicao = buscar_indice_por_nome(registro['nome'])
    limpar_tela()
    if(posicao != -1):
        print(f'Nome: {contatos[posicao]["nome"]}')
        print(f'Fone: {contatos[posicao]["fone"]}')
        input('Tecle <enter>...')
    else:
        input('Contato nao encontrado. Tecle <enter>...')

    
def listar_contatos()->None:
    if len(contatos) == 0:
        print('Nao ha contatos cadastrados.')
        input('Tecle <enter>...')
    else:
        for contato in contatos:
            print(f'Contato: nome - {contato["nome"]} - fone: {contato["fone"]}')
        input('Tecle <enter> para retornar ao menu...')


opcao = 0
while(opcao != 6):
    opcao = menu()
    if (opcao <1) or (opcao > 6):
        input("Opçao invalida. Tecle enter...")
    elif opcao == 1:
        incluir()
    elif opcao == 2:
        editar()
    elif opcao == 3:
        excluir()
    elif opcao == 4:
        buscar_por_nome()
    elif opcao == 5:
        listar_contatos()
    else:
        break
print('Sessao encerrada pelo usuario.')
        
