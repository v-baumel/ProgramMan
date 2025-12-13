import pygame
import Constants as C
from Enviroment import Wall
from Enviroment import Pellet

class Mapa:
    def __init__(self, level_data):
        self.tile_size = C.TILE_SIZE
        self.walls = pygame.sprite.Group()
        self.pellets = pygame.sprite.Group()
        self.player_start = None
        self.ghost_starts = []
        
        # 1 = Wall, 2 = Pellet, 0 = Empty, 3 = Pacman Start, 4 = Ghost Start
        for row_index, row in enumerate(level_data):
            for col_index, tile in enumerate(row):
                x = col_index * self.tile_size
                y = row_index * self.tile_size
                
                if tile == 1:
                    wall = Wall(x, y)
                    self.walls.add(wall)
                elif tile == 2:
                    pellet = Pellet(x, y)
                    self.pellets.add(pellet)
                elif tile == 3:
                    # Store the starting position (x, y)
                    self.player_start = (x, y)
                elif tile == 4:
                    # Store the starting position (x, y) for ghosts
                    self.ghost_starts.append((x, y))

    def get_walls(self):
        """Returns the sprite group containing all Wall objects."""
        return self.walls
    
    def get_pellets(self):
        """Returns the sprite group containing all Pellet objects."""
        return self.pellets
    