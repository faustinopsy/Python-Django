import random
nomes = ['Alice', 'Bob', 'Carl', 'Daniele', 'Edgard']
for n in range(5):
    random.shuffle(nomes)
    print(f'Na passagem de número {n + 1} a lista estava assim: {nomes}')
