""" Classe que demonstra o uso variáveis estáticas """
class Player:
    
    numero_jogadores=0

    def adicionar_jogador(self):
        numero_jogadores += 1
        print(f'Neste momento, ha {numero_jogadores} jogadores conectados.')

    def sair(self):
        numero_jogadores -= 1
        print(f'Voce se desconectou. Restam {numero_jogadores} jogadores.')
