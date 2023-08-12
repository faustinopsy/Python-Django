# Primeiro, crio uma lista de alunos:
turma = ['Alice', 'Bob', 'Carl', 'Daniele', 'Eduard', 'Felicia']
print('Lista original:')
for aluno in turma:
    print(aluno, end=" ")
print('\n\"Fatiando\" os quatro primeiros de dois em dois:')
for indice in range(0, 4, 2):
    print(turma[indice], end=" ")
print('\nIgnorando os dois primeiros:')
for indice in range(2, len(turma)):
    print(turma[indice], end=" ")
print('\nPegando até o quinto elemento: ')
for indice in range(0, 5):
    print(turma[indice], end=" ")
print('\nRetornando todo mundo de dois em dois a partir do início (índices pares):')
for indice in range(0, len(turma), 2):
    print(turma[indice], end=" ")
print('\nRetornando todo mundo de dois em dois a partir do segundo (índices ímpares):')
for indice in range(1,len(turma), 2):
    print(turma[indice], end=" ")
