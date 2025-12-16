import pygame
import Constantes as C
from Enviroment import Wall
from Enviroment import Pellet
from Enviroment import Power_up
class Mapa:
    def __init__(self, level_data):
        self.tile_size = C.TILE_SIZE
        self.walls = pygame.sprite.Group()
        self.pellets = pygame.sprite.Group()
        self.upgrade= pygame.sprite.Group()
        self.player_start = None
        self.ghost_starts = []
        # Tamanho: 31 linhas x 28 colunas (tamanho original do arcade)
        #  Legenda:0
        # # = Parede
        # . = Caminho com pellet normal
        # O = Power-up (pellet maior)
        # X = Espaço vazio (sem pellet - área dos fantasmas)
        # T = Túnel (teleporte entre bordas)
        # P = Posição inicial do Pac-Man
        # L = Posicão inicial de Inimigo
        
        for row_index, row in enumerate(level_data):
            for col_index, tile in enumerate(row):
                x = col_index * self.tile_size
                y = row_index * self.tile_size

                
                if tile == "#":
                    wall = Wall(x, y)
                    self.walls.add(wall)
                elif tile == ".":
                    pellet = Pellet(x, y)
                    self.pellets.add(pellet)
                elif tile == "O":
                    upgrade = Power_up(x, y)
                    self.upgrade.add(upgrade)
                elif tile == "P":
                    self.player_start = (x, y)
                elif tile == "F":
                    self.ghost_starts.append((x, y))
    def get_upgrade(self):
        return self.upgrade

    def get_walls(self):
        return self.walls
    
    def get_pellets(self):
        return self.pellets
    
