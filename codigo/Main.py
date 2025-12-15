import pygame
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
import Constantes as C
import Mapa
import Jogador

def main():
    
    pygame.display.set_caption("ProgramMan")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Arial', 24)

    mapa = Mapa.Mapa(C.MAPA_1)

    map_width = C.MAP_X * C.TILE_SIZE
    map_height = C.MAP_Y * C.TILE_SIZE
    offset_x = (C.X_MAX - map_width) // 2
    offset_y = 0

    for wall in mapa.get_walls():
        wall.rect.x += offset_x
        wall.rect.y += offset_y
    for pellet in mapa.get_pellets():
        pellet.rect.x += offset_x
        pellet.rect.y += offset_y

    jogador = Jogador.Jogador(mapa.player_start[0] + offset_x, mapa.player_start[1] + offset_y, mapa)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        jogador.handle_input()
        jogador.update(1 / C.FPS)

        screen.fill(C.BLACK)
        mapa.get_walls().draw(screen)
        mapa.get_pellets().draw(screen)
        jogador.draw(screen)

        pygame.display.flip()
        clock.tick(C.FPS)

if __name__ == "__main__":
    main() 