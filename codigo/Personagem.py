import pygame
import Constantes as C
import Mapa 
#superclasse para os fantasmas e o jogador
class Personagem(pygame.sprite.Sprite):
    def __init__(self, x, y, mapa:Mapa):
        super().__init__()
        TILE_SIZE =  C.TILE_SIZE
        self.image = pygame.Surface([TILE_SIZE-2, TILE_SIZE-2])
        #self.image.fill(C.RED)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x-1, y-1)
        self.speed = 2
        self.direction = (0, 1) # (dx, dy)
        self.next_direction = (0, 1)
        self.score = 0
        self.mapa = mapa

    def update(self, dt): pass


