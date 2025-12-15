import pygame
import Personagem
import Constantes as C
from animacoes_jogo import AnimationSystem


class Jogador(Personagem.Personagem):
    def __init__(self, x, y, mapa):
        super().__init__(x, y, mapa)
        self.speed = 2
        self.image.fill(C.YELLOW)
        self.anim = AnimationSystem()
        self.facing = "direita"

    def handle_input(self):
        keys = pygame.key.get_pressed()
        nd = (0, 0)
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            nd = (-1, 0)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            nd = (1, 0)
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            nd = (0, -1)
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            nd = (0, 1)
        if nd != (0, 0):
            self.next_direction = nd

    def draw(self, surface):
        self.anim.update()
        size = max(1, int(C.TILE_SIZE // 2 - 2))
        x, y = self.rect.center
        facing = ""
        dx,dy = self.direction
        if dx < 0:
            facing = "esquerda"
        elif dx > 0:
            facing = "direita"
        elif dy < 0:
            facing = "cima"
        elif dy > 0:
            facing = "baixo"
        else:
            facing = "direita"
        self.anim.desenhar_estudante_sem_poder(surface, x, y, facing, size)

    def update(self, dt):
        super().update(dt)
        if self.direction != (0, 0):
            dx, dy = self.direction
            if dx < 0:
                self.facing = "esquerda"
            elif dx > 0:
                self.facing = "direita"
            elif dy < 0:
                self.facing = "cima"
            elif dy > 0:
                self.facing = "baixo"