import pygame
import Personagem
import Constants as C

class Jogador(Personagem.Personagem):
    def __init__(self, x, y, mapa):
        super().__init__(x, y, mapa)
        self.image.fill(C.YELLOW) 

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.next_direction = (-1, 0)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.next_direction = (1, 0)
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.next_direction = (0, -1)
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.next_direction = (0, 1)