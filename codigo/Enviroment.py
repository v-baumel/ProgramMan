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
        self.image = pygame.image.load("imagens/tecla.png").convert_alpha()
        self.image = pygame.transform.scale(
            self.image,
            (C.TILE_SIZE // 2, C.TILE_SIZE // 2)
        )
        self.rect = self.image.get_rect()
        self.rect.center = (
            x + C.TILE_SIZE // 2,
            y + C.TILE_SIZE // 2
        )

        
class Power_up(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("imagens/monitor.png").convert_alpha()
        self.image = pygame.transform.scale(
            self.image,
            (C.TILE_SIZE, C.TILE_SIZE)
        )
        self.rect = self.image.get_rect()
        self.rect.center = (
            x + C.TILE_SIZE // 2,
            y + C.TILE_SIZE // 2
        )

class Fruit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("imagens/energetico.png").convert_alpha()
        self.image = pygame.transform.scale(
            self.image,
            (C.TILE_SIZE // 1.5, C.TILE_SIZE // 1.5)
        )
        self.rect = self.image.get_rect()
        self.rect.center = (
            x + C.TILE_SIZE // 2,
            y + C.TILE_SIZE // 2
        )