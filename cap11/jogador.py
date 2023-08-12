""" Classe que demonstra o uso variáveis estáticas """
class Jogador:

    numero_jogadores=0

    def __init__(self, nome):
        self.nome = nome
        Jogador.numero_jogadores += 1

    def sair(self):
        Jogador.numero_jogadores -= 1
        print(f'O jogador {self.nome} se desconectou. Restam {numero_jogadores} jogadores.')

    def imprimir_quantidade_jogadores(self):
        print(f'Neste momento, ha {Jogador.numero_jogadores} jogadores conectados.')
