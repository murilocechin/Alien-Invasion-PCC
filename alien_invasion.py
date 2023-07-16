"""
Dirario: Criando o primeiro arquivo do jogo. 
"""

import sys

import pygame

class AlienInvasion:
    """Classe geral para administrar os aspectos básicos do jogo"""

    def __init__(self):
        """Inicializa o jogo, e criar os game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    
    def run_game(self):
        """Inicializa o main loop do jogo"""

        while True:
            # Monitora os movimentos(Livro em Inglês chama de Eventos) do teclado e do mouse.

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Printa na tela a mais recente drawn screen
            pygame.display.flip()


if __name__ == '__main__':
    # Faz a game instance, e roda o jogo.
    ai = AlienInvasion()
    ai.run_game()
