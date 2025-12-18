import pygame
import math
import random
pygame.init()

def tela_inicio(screen):
    """Tela de início - Programador vs Programação"""
    import Constantes as C
    
    clock = pygame.time.Clock()
    font_titulo = pygame.font.SysFont('Courier New', 100, bold=True)
    font_subtitulo = pygame.font.SysFont('Courier New', 30)
    font_botao = pygame.font.SysFont('Courier New', 45, bold=True)
    font_code = pygame.font.SysFont('Courier New', 16)
    
    # Cores minimalistas
    CODE_GREEN = (0, 255, 100)
    BUG_RED = (255, 70, 70)
    DARK_BG = (25, 25, 35)
    LIGHT_TEXT = (200, 200, 210)
    
    # Apenas alguns bugs caindo (reduzido de 15 para 6)
    code_lines = [
        "NullPointerException",
        "StackOverflow",
        "Memory Leak",
        "404 Not Found",
    ]
    
    falling_bugs = []
    for i in range(6):
        falling_bugs.append({
            'x': (C.X_MAX // 7) * (i + 1),
            'y': random.randint(-C.Y_MAX, -100),
            'speed': 2,
            'text': code_lines[i % len(code_lines)],
        })
    
    botao_rect = pygame.Rect(C.X_MAX // 2 - 250, C.Y_MAX // 2 + 180, 500, 90)
    time = 0
    
    while True:
        time += 0.05
        mouse_pos = pygame.mouse.get_pos()
        mouse_hover = botao_rect.collidepoint(mouse_pos)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    return True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_hover:
                    return True
        
        # Background limpo
        screen.fill(DARK_BG)
        
        # Bugs caindo de forma organizada
        for bug in falling_bugs:
            bug['y'] += bug['speed']
            if bug['y'] > C.Y_MAX + 50:
                bug['y'] = -50
            
            alpha = int(150 * (1 - abs(bug['y'] - C.Y_MAX/2) / (C.Y_MAX/2)))
            if alpha > 0:
                text = font_code.render(bug['text'], True, BUG_RED)
                text.set_alpha(alpha)
                screen.blit(text, (bug['x'] - text.get_width()//2, bug['y']))
        
        # Título principal limpo
        titulo = "PROGRAMMAN"
        text_titulo = font_titulo.render(titulo, True, CODE_GREEN)
        x_center = C.X_MAX // 2 - text_titulo.get_width() // 2
        screen.blit(text_titulo, (x_center, 150))
        
        # Subtítulo único e direto
        subtitulo = "Fuja dos bugs. Colete teclas. Sobreviva."
        text_sub = font_subtitulo.render(subtitulo, True, LIGHT_TEXT)
        screen.blit(text_sub, (C.X_MAX // 2 - text_sub.get_width() // 2, 280))
        
        # Botão minimalista
        if mouse_hover:
            pygame.draw.rect(screen, CODE_GREEN, botao_rect, border_radius=8)
            cor_texto = DARK_BG
        else:
            pygame.draw.rect(screen, DARK_BG, botao_rect, border_radius=8)
            pygame.draw.rect(screen, CODE_GREEN, botao_rect, 3, border_radius=8)
            cor_texto = CODE_GREEN
        
        text_botao = font_botao.render("JOGAR", True, cor_texto)
        screen.blit(text_botao, (
            botao_rect.centerx - text_botao.get_width() // 2,
            botao_rect.centery - text_botao.get_height() // 2
        ))
        
        # Instruções simples no rodapé
        font_pequeno = pygame.font.SysFont('Courier New', 20)
        instrucoes = "SETAS para mover  •  ESPAÇO para começar"
        
        text_inst = font_pequeno.render(instrucoes, True, LIGHT_TEXT)
        screen.blit(text_inst, (C.X_MAX // 2 - text_inst.get_width() // 2, C.Y_MAX - 100))
        
        pygame.display.flip()
        clock.tick(60)


def tela_game_over(screen, stats, venceu=False):
    """Tela de game over limpa e elegante"""
    import Constantes as C
    
    clock = pygame.time.Clock()
    font_titulo = pygame.font.SysFont('Courier New', 110, bold=True)
    font_stats = pygame.font.SysFont('Courier New', 36)
    font_botao = pygame.font.SysFont('Courier New', 40, bold=True)
    font_info = pygame.font.SysFont('Courier New', 24)
    
    CODE_GREEN = (0, 255, 100)
    BUG_RED = (255, 70, 70)
    DARK_BG = (25, 25, 35)
    LIGHT_TEXT = (200, 200, 210)
    
    # Botões maiores e mais espaçados
    botao_reiniciar = pygame.Rect(C.X_MAX // 2 - 500, C.Y_MAX - 180, 450, 85)
    botao_sair = pygame.Rect(C.X_MAX // 2 + 50, C.Y_MAX - 180, 450, 85)
    
    # Apenas 3 partículas flutuantes suaves
    particles = []
    for _ in range(3):
        particles.append({
            'x': random.randint(100, C.X_MAX - 100),
            'y': random.randint(100, C.Y_MAX - 100),
            'size': random.randint(100, 200),
            'speed': random.uniform(0.3, 0.8)
        })
    
    time = 0
    fade_alpha = 0
    can_interact = False
    wait_time = 90  # 1.5 segundos
    frames_waited = 0
    
    while True:
        time += 0.02
        frames_waited += 1
        
        if frames_waited >= wait_time:
            can_interact = True
        
        if fade_alpha < 255:
            fade_alpha += 4
        
        mouse_pos = pygame.mouse.get_pos()
        hover_reiniciar = botao_reiniciar.collidepoint(mouse_pos) and can_interact
        hover_sair = botao_sair.collidepoint(mouse_pos) and can_interact
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN and can_interact:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE or event.key == pygame.K_r:
                    return True
            elif event.type == pygame.MOUSEBUTTONDOWN and can_interact:
                if hover_reiniciar:
                    return True
                elif hover_sair:
                    return False
        
        screen.fill(DARK_BG)
        
        # Círculos sutis no fundo
        for p in particles:
            p['x'] = (p['x'] + p['speed']) % C.X_MAX
            alpha = int(20 + abs(math.sin(time + p['x'] * 0.01)) * 15)
            color = (40, 40, 50, alpha)
            s = pygame.Surface((p['size']*2, p['size']*2), pygame.SRCALPHA)
            pygame.draw.circle(s, color, (p['size'], p['size']), p['size'])
            screen.blit(s, (p['x'] - p['size'], p['y'] - p['size']))
        
        # Título com fade in
        if venceu:
            titulo = "SUCESSO!"
            cor_titulo = CODE_GREEN
        else:
            titulo = "GAME OVER"
            cor_titulo = BUG_RED
        
        text_titulo = font_titulo.render(titulo, True, cor_titulo)
        text_titulo.set_alpha(fade_alpha)
        
        x_title = C.X_MAX // 2 - text_titulo.get_width() // 2
        screen.blit(text_titulo, (x_title, 120))
        
        # Subtítulo simples
        if fade_alpha >= 200:
            if venceu:
                subtitulo = "Você conseguiu escapar... desta vez."
            else:
                subtitulo = "Os bugs venceram."
            
            text_sub = font_info.render(subtitulo, True, LIGHT_TEXT)
            screen.blit(text_sub, (C.X_MAX // 2 - text_sub.get_width() // 2, 260))
        
        # Box de estatísticas minimalista
        if fade_alpha >= 220:
            box_rect = pygame.Rect(C.X_MAX // 2 - 350, 340, 700, 260)
            
            pygame.draw.rect(screen, (35, 35, 45), box_rect, border_radius=12)
            pygame.draw.rect(screen, CODE_GREEN if venceu else BUG_RED, box_rect, 2, border_radius=12)
            
            # Estatísticas limpas
            y_stat = 390
            stats_list = [
                ("Teclas coletadas", stats.get('teclas', 0)),
                ("Monitores chamados", stats.get('monitores', 0)),
                ("Energéticos tomados", stats.get('energeticos', 0))
            ]
            
            for label, valor in stats_list:
                text_label = font_stats.render(f"{label}:", True, LIGHT_TEXT)
                screen.blit(text_label, (C.X_MAX // 2 - 300, y_stat))
                
                text_valor = font_stats.render(f"{valor}", True, CODE_GREEN if venceu else BUG_RED)
                screen.blit(text_valor, (C.X_MAX // 2 + 200, y_stat))
                y_stat += 70
        
        # Botões (só aparecem quando pode interagir)
        if can_interact:
            for botao, texto, hover in [(botao_reiniciar, "JOGAR NOVAMENTE", hover_reiniciar),
                                         (botao_sair, "SAIR", hover_sair)]:
                
                if hover:
                    pygame.draw.rect(screen, CODE_GREEN, botao, border_radius=8)
                    cor_texto = DARK_BG
                else:
                    pygame.draw.rect(screen, (35, 35, 45), botao, border_radius=8)
                    pygame.draw.rect(screen, CODE_GREEN, botao, 3, border_radius=8)
                    cor_texto = CODE_GREEN
                
                text_botao = font_botao.render(texto, True, cor_texto)
                screen.blit(text_botao, (
                    botao.centerx - text_botao.get_width() // 2,
                    botao.centery - text_botao.get_height() // 2
                ))
            
            # Instrução de atalho
            text_atalho = font_info.render("Pressione R ou ESPAÇO para jogar novamente", True, LIGHT_TEXT)
            text_atalho.set_alpha(int(abs(math.sin(time * 2)) * 100 + 155))
            screen.blit(text_atalho, (C.X_MAX // 2 - text_atalho.get_width() // 2, C.Y_MAX - 80))
        else:
            # Contagem regressiva sutil
            dots = "." * ((frames_waited // 15) % 4)
            text_wait = font_info.render(f"Carregando{dots}", True, LIGHT_TEXT)
            screen.blit(text_wait, (C.X_MAX // 2 - text_wait.get_width() // 2, C.Y_MAX - 250))
        
        pygame.display.flip()
        clock.tick(60)


def main():
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    import Constantes as C
    C.screen = screen
    import Mapa
    import Jogador
    import Inimigo
    
    pygame.display.set_caption("ProgramMan")
    
    # Mostra tela de início
    if not tela_inicio(screen):
        pygame.quit()
        return
    
    # Loop principal do jogo
    jogar_novamente = True
    while jogar_novamente:
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

        game_over = False
        venceu = False
        sair_jogo = False  # Nova flag para controlar saída
        
        while not game_over and not sair_jogo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sair_jogo = True  # Marca para sair sem mostrar game over

            jogador.handle_input()
            jogador.update(1 / C.FPS)
            for inimigo in inimigos: 
                inimigo.update(1 / C.FPS)

            screen.fill(C.BLACK)
            mapa.get_walls().draw(screen)
            mapa.get_pellets().draw(screen)
            mapa.get_upgrade().draw(screen)
            mapa.get_fruit().draw(screen)
            jogador.draw(screen)
            inimigos.draw(screen)

            text_teclas = font.render(f"Teclas apertadas: {jogador.tracker.bolinhas_coletadas}", True, C.WHITE)
            x = offset_x + map_width - 80
            screen.blit(text_teclas, (x, 20))
            
            text_monitores = font.render(f"Monitores chamados: {jogador.tracker.powerups_coletados}", True, C.WHITE)
            screen.blit(text_monitores, (x, 80))

            text_energeticos = font.render(f"Energéticos consumidos: {jogador.tracker.fruitinhas}", True, C.WHITE)
            screen.blit(text_energeticos, (x, 140))

            # CORREÇÃO: Verifica colisão com inimigos de forma mais robusta
            try:
                jogador_rect = jogador.rect if hasattr(jogador, 'rect') else None
                jogador_powered = getattr(jogador, 'powered', False)
                
                if jogador_rect:
                    for inimigo in inimigos:
                        inimigo_rect = inimigo.rect if hasattr(inimigo, 'rect') else None
                        if inimigo_rect and jogador_rect.colliderect(inimigo_rect):
                            # Se o jogador NÃO está powered, game over
                            if not jogador_powered:
                                print("COLISÃO DETECTADA! Game Over!")  # Debug
                                game_over = True
                                venceu = False
                                break
            except Exception as e:
                print(f"Erro na detecção de colisão: {e}")
            
            # Verifica vitória
            if len(mapa.get_pellets()) == 0:
                print("VITÓRIA! Todas as teclas coletadas!")  # Debug
                venceu = True
                game_over = True

            pygame.display.flip()
            clock.tick(C.FPS)
        
        # Mostra tela de game over apenas se não for ESC
        if game_over and not sair_jogo:
            stats = {
                'teclas': jogador.tracker.bolinhas_coletadas,
                'monitores': jogador.tracker.powerups_coletados,
                'energeticos': jogador.tracker.fruitinhas
            }
            jogar_novamente = tela_game_over(screen, stats, venceu)
        else:
            # Se apertou ESC, sai do loop
            jogar_novamente = False
    
    pygame.quit()

if __name__ == "__main__":
    main()