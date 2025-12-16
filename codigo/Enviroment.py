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
        radius = C.TILE_SIZE // 4
        size = radius * 2
        self.image = pygame.Surface((C.TILE_SIZE, C.TILE_SIZE), pygame.SRCALPHA)
        center = self.image.get_rect().center
        pygame.draw.circle(
            self.image,
            C.DARK_GREEN,
            center,
            radius
        )
        self.rect = self.image.get_rect()
        self.rect.center = (x + TILE_SIZE // 2, y + TILE_SIZE // 2)

        


class Power_up(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        radius = C.TILE_SIZE // 4
        size = radius * 2
        self.image = pygame.Surface((C.TILE_SIZE, C.TILE_SIZE), pygame.SRCALPHA)
        center = self.image.get_rect().center
        pygame.draw.circle(
            self.image,
            C.BLUE,
            center,
            radius
        )
        self.rect = self.image.get_rect()
        self.rect.center = (x + TILE_SIZE // 2, y + TILE_SIZE // 2)

class Fruit(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        radius = C.TILE_SIZE//4
        self.image = pygame.Surface((C.TILE_SIZE,C.TILE_SIZE),pygame.SRCALPHA)
        center = self.image.get_rect().center
        pygame.draw.circle(self.image,C.RED,center,radius)
        self.rect = self.image.get_rect()
        self.rect.center = (x+TILE_SIZE // 2, y + TILE_SIZE // 2)