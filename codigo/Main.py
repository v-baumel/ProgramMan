import pygame
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
import Constantes as C
C.screen = screen
import Mapa
import Jogador
import Inimigo

def main():
    
    pygame.display.set_caption("ProgramMan")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Arial', 40)

    map_width = C.MAP_X * C.TILE_SIZE
    map_height = C.MAP_Y * C.TILE_SIZE
    offset_x = (C.X_MAX - map_width) // 2
    offset_y = 0

    mapa = Mapa.Mapa(C.MAPA_1, offset_x, offset_y)

    jogador = Jogador.Jogador(mapa.player_start[0], mapa.player_start[1], mapa)
    mapa.player = jogador
    inimigos = pygame.sprite.Group()
    mapa.ghosts = inimigos
    
    for gx, gy in mapa.ghost_starts:
        inimigo = Inimigo.Inimigo(gx, gy, mapa)
        inimigos.add(inimigo)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        jogador.handle_input()
        jogador.update(1 / C.FPS)
        for inimigo in inimigos: inimigo.update(1 / C.FPS)

        screen.fill(C.BLACK)
        mapa.get_walls().draw(screen)
        mapa.get_pellets().draw(screen)
        mapa.get_upgrade().draw(screen)
        mapa.get_fruit().draw(screen)
        jogador.draw(screen)
        inimigos.draw(screen)

        text_teclas_apertadas = font.render(f"Teclas apertadas: {jogador.tracker.bolinhas_coletadas}", True, C.WHITE)
        x = offset_x + map_width-80
        y = 20
        screen.blit(text_teclas_apertadas, (x, y))
        
        text_monitores_chamados = font.render(f"Monitores chamados: {jogador.tracker.powerups_coletados}", True, C.WHITE)
        y = 80
        screen.blit(text_monitores_chamados, (x, y))

        text_energeticos_consumidos = font.render(f"Energéticos consumidos: {jogador.tracker.fruitinhas}", True, C.WHITE)
        y = 140  
        screen.blit(text_energeticos_consumidos, (x, y))    

        pygame.display.flip()
        clock.tick(C.FPS)

if __name__ == "__main__":
    main() 
