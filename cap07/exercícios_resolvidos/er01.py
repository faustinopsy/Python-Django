alunos = []
total_individual = 0.0
continua_loop_alunos = 'S'
continua_cadastro_notas = 'S'
while continua_loop_alunos == 'S':
    registro_aluno = {
        'nome': '',
        'notas': [],
        'media': 0.0
    }
    nome = input('Entre com o nome do aluno: ')
    registro_aluno['nome'] = nome
    indice = 0
    total_individual = 0
    while continua_cadastro_notas == 'S':
        indice = indice + 1
        print('Digite a nota n. %d: ' %indice)
        nota = float(input())
        registro_aluno['notas'].append(nota)
        total_individual = total_individual + nota
        print('Deseja cadastrar outra nota? [S-continua/N-encerrar etapa]')
        continua_cadastro_notas = str.capitalize(input())
    registro_aluno['media'] = total_individual / len(registro_aluno['notas'])
    alunos.append({'aluno': registro_aluno})
    print('Deseja cadastrar as notas de outro aluno? [S-continua/N-proximo aluno]')
    continua_loop_alunos = str.capitalize(input())
    continua_cadastro_notas = 'S'
for registro in alunos:
    if registro['aluno']['media'] >= 7.0:
        print(f'Nome: {registro["aluno"]["nome"]} - Notas: {registro["aluno"]["notas"]} - Média: {registro["aluno"]["media"]} - APROVADO')
    elif registro['aluno']['media'] >= 3.0:
        print(f'Nome: {registro["aluno"]["nome"]} - Notas: {registro["aluno"]["notas"]} - Média: {registro["aluno"]["media"]} - FARÁ PROVA FINAL')
    else:
        print(f'Nome: {registro["aluno"]["nome"]} - Notas: {registro["aluno"]["notas"]} - Média: {registro["aluno"]["media"]} - REPROVADO')
