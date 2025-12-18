import pygame
from Personagem import Personagem
import Constantes as C
import random

directions = ((1,0), (-1,0), (0,1), (0,-1))

class Inimigo(Personagem):
    def __init__(self, x, y, mapa, image_path):
        super().__init__(x,y,mapa)
        self.spawn = (x,y)
        self.speed = 3
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(
            self.image,
            (C.TILE_SIZE-2, C.TILE_SIZE-2)
        )
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self, dt):
        #estratégia de perseguição simples
        #verifica quais direções são possíveis (tenta evitar voltar na direção oposta)
        #escolhe a que minimiza a distância ao jogador, com alguma aleatoriedade 
        def check_dir(d):
            self.rect.x += d[0] * self.speed
            self.rect.y += d[1] * self.speed
            hit_wall = pygame.sprite.spritecollide(self, self.mapa.get_walls(), False)
            self.rect.x -= d[0] * self.speed
            self.rect.y -= d[1] * self.speed
            return not hit_wall 

        player = self.mapa.player
        opposite_dir = (-self.direction[0], -self.direction[1])

        possible_dirs = [d for d in directions if check_dir(d)]

        if not possible_dirs:
            self.direction = (0, 0)
        else:
            choices = possible_dirs
            if opposite_dir in choices and len(choices) > 1:
                choices = [d for d in choices if d != opposite_dir]

            scored = []
            for d in choices:
                nx = self.rect.centerx + d[0] * C.TILE_SIZE
                ny = self.rect.centery + d[1] * C.TILE_SIZE
                dist = (player.rect.centerx - nx) ** 2 + (player.rect.centery - ny) ** 2
                scored.append((dist, d))

            scored.sort(key=lambda x: x[0]) # organizar por distancia

            if len(scored) > 1 and random.random() < 0.444: # 44.4% de chance de escolher um caminho aleatório entre os piores
                self.direction = random.choice([d for _, d in scored[1:]])
            else:
                self.direction = scored[0][1]

        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed
        