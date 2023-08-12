# Primeiro, crio uma lista de alunos:
turma = ['Alice', 'Bob', 'Carl', 'Daniele', 'Eduard', 'Felicia']
print('Lista original:')
for aluno in turma:
    print(aluno, end=" ")
print('\n\"Fatiando\" os quatro primeiros de dois em dois, na ordem inversa:')
for indice in range(3, 0, -2):
    print(turma[indice], end=" ")
print('\nIgnorando os dois primeiros, na ordem inversa:')
for indice in range(len(turma)-1, 1, -1):
    print(turma[indice], end=" ")
print('\nPegando os cinco ultimos elementos, na ordem inversa:: ')
for indice in range(5, 0, -1):
    print(turma[indice], end=" ")
print('\nRetornando todo mundo de dois em dois a partir do fim (índices pares):')
for indice in range(len(turma)-2, -1, -2):
    print(turma[indice], end=" ")
print('\nRetornando todo mundo de dois em dois a partir do fim (índices ímpares):')
for indice in range(len(turma)-1, -1, -2):
    print(turma[indice], end=" ")
