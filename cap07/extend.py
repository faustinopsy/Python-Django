turma = []
lista_alunos = ['Adriano','Bruno','Carlos']
lista_alunas = ['Daniele', 'Elisa','Fernanda']
print('Turma vazia: ', turma)
print('Lista dos alunos: ', lista_alunos)
print('Lista das alunas: ', lista_alunas)
print('Juntando todo mundo... primeiro as damas!')
turma.extend(lista_alunas)
print(turma)
print('Agora os cavalheiros:')
turma.extend(lista_alunos)
print(turma)
