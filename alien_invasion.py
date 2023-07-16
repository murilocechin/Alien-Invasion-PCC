"""
Dirario: Criando o primeiro arquivo do jogo. 
"""

import sys

import pygame

from settings import Settings

class AlienInvasion:
    """Classe geral para administrar os aspectos básicos do jogo"""

    def __init__(self):
        """Inicializa o jogo, e criar as configurações de jogo"""
        pygame.init()
        self.settings = Settings()

    
        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_hight
        ))
        pygame.display.set_caption("Alien Invasion")

        # Set the background color.
        self.bg_color = (230, 230, 230)

    
    def run_game(self):
        """Inicializa o main loop do jogo"""

        while True:
            # Monitora os movimentos(Livro em Inglês chama de Eventos) do teclado e do mouse.

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Redesenhando a tela a cada passo do loop.
            self.screen.fill(self.settings.bg_color)
            # Printa na tela a mais recente drawn screen
            pygame.display.flip()


if __name__ == '__main__':
    # Faz a game instance, e roda o jogo.
    ai = AlienInvasion()
    ai.run_game()


