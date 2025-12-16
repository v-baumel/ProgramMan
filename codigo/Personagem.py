import pygame
import Constantes as C
import Mapa 
from sistema_de_vidas import SistemaVidas
#superclasse para os fantasmas e o jogador
class Personagem(pygame.sprite.Sprite):
    def __init__(self, x, y, mapa:Mapa):
        super().__init__()
        TILE_SIZE =  C.TILE_SIZE
        self.image = pygame.Surface([TILE_SIZE-2, TILE_SIZE-2])
        self.image.fill(C.RED)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x-1, y-1)
        self.speed = 1
        self.direction = (0, 1) # (dx, dy)
        self.next_direction = (0, 1)
        self.score = 0
        self.mapa = mapa

    def update(self, dt):
        walls = self.mapa.get_walls()
        
        old_pos = self.rect.topleft

        self.rect.x += self.next_direction[0] * self.speed #* dt
        self.rect.y += self.next_direction[1] * self.speed #* dt

        wall_hits = pygame.sprite.spritecollide(self, walls, False)
        if not wall_hits:
            self.direction = self.next_direction
        else:
            self.rect.topleft = old_pos
            self.rect.x += self.direction[0] * self.speed
            self.rect.y += self.direction[1] * self.speed

            hit_list = pygame.sprite.spritecollide(self, walls, False)
            if hit_list:
                self.rect.topleft = old_pos

        


