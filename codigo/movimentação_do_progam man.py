
import pygame

def move(self, key):
    # ve onde o jogador apertou , não necessariamente va
    if key == "up":
        self.progam_man_next_direction = [0, -self.scale/16]

    elif key == "left":
        self.progam_man_next_direction = [-self.scale/16, 0]

    elif key == "down":
        self.progam_man_next_direction = [0, self.scale/16]

    elif key == "right":
        self.progam_man_next_direction = [self.scale/16, 0]




def turning_corner(self, position, direction, next_direction):
    
    # tenta ir na nova direção
    test_pos = [position[0] + next_direction[0], position[1] + next_direction[1]]

    # testa colisão
    test_pos = self.collider(test_pos, [0,0])

    # se nao colidiu, troca a direção
    if test_pos == [position[0] + next_direction[0], position[1] + next_direction[1]]:
        # virou a esquina
        return next_direction, next_direction

    # senão, continua na direção atual
    return direction, next_direction




def collider(self, position, direction):
    # Tenta mover
    new_x = position[0] + direction[0]
    new_y = position[1] + direction[1]

    # Verifica colisão com paredes
    for y in range(len(self.map)):
        for x in range(len(self.map[0])):
            if self.map[y][x] == "#":
                
                # área sólida da parede
                x_wall = x * self.scale
                y_wall = y * self.scale
                wall_size = self.scale

                # posição do Program Man
                if (new_x + self.scale*0.5 > x_wall and
                    new_x < x_wall + wall_size and
                    new_y + self.scale*0.5 > y_wall and
                    new_y < y_wall + wall_size):

                    # bateu: não mexe
                    return position

    # não bateu: mexe
    return [new_x, new_y]
