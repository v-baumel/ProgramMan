import pygame
#Se "pygame" estiver sublinhado é pq você não instalou ele

pygame.init()

tela = pygame.display.set_mode((500, 200))
pygame.display.set_caption("Teste Pygame")

fonte = pygame.font.SysFont(None, 48)
texto = fonte.render("Você instalou o pygame!", True, (255, 255, 255))

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill((0, 0, 0))       # Fundo preto
    tela.blit(texto, (20, 80)) # Desenha o texto na tela
    pygame.display.flip()      # Atualiza a tela

pygame.quit()
