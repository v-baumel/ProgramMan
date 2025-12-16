import pygame
import Constantes as C
TILE_SIZE = C.TILE_SIZE
print(TILE_SIZE)

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = C.WALL_IMAGE
        self.rect = self.image.get_rect(topleft=(x, y))


class Pellet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([TILE_SIZE//3, TILE_SIZE//3])
        self.image.fill(C.BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (x + TILE_SIZE // 2, y + TILE_SIZE // 2)
