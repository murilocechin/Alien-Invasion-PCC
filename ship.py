"""
Classe da nave
"""
import pygame


class Ship:
    """Classe que administra a nave"""

    def __init__(self, ai_game):
        """Inicializa a nave e configura a posição de começo"""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Carrega a imagem da nave e pega suas reações
        self.image = pygame.image.load('images/ship.bpm')
        self.rect = self.image.get_rect()

        # Começa cada nave nova na parte baixa da tela
        self.rect.midbottom = self.screen_rect.midbottom

    
    def blitme(self):
        """Desenha a nave na sua posição atual"""
        self.screen.blit(self.image, self.rect)