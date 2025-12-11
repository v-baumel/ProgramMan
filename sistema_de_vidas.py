import pygame 
import time

class SistemaVidas:

    def __init__(self):
        self.vidas = 3
        self.bolinhas_coletadas = 0
        self.fantasmas_comidos = 0
        self.powerup_ativo = False
        self.tempo_inicio_powerup = 0
        self.duracao_powerup = 20 #power up vai durar 20 seg
        self.game_over = False
        self.invulneravel = False
        self.temporizador_invulneravel = 0
        self.duracao_invulneravel = 90  #1,5 seg sem levar dano dps de perder vida 
    
    def coletar_bolinha(self):
        self.bolinhas_coletadas += 1

        if self.bolinhas_coletadas % 25 == 0:
            self.vidas += 1
            return "vida_extra"
        
        return "bolinha"

    def checar_ativacao_power_up(self):
        if self.vidas >= 8 and not self.powerup_ativo:
            self.ativar_powerup()
            return True
        return False
    
    def ativar_power_up(self):
        self.powerup_ativo = True
        self.tempo_inicio_powerup = time.time()
        self.fantasmas_comidos = 0
    
    def atualizar_power_up(self):
        if not self.powerup_ativo:
            return None
        tempo_decorrido = time.time() - self.tempo_inicio_powerup
        tempo_restante = self.duracao_powerup - tempo_decorrido #atualizar o status 
    
        if tempo_restante <= 0:
            self.desativar_powerup()
            return "powerup_fim" #acabou o tempo
        
        #ficar piscando nos ulitmos 5 segundos
        if tempo_restante <= 5:
            return "powerup_terminando"
        
        return "powerup_ativo"
    
    def desativar_powerup(self):
        self.powerup_ativo = False
        self.tempo_inicio_powerup = 0
    
    def comer_fantasmas(self): #come os fantasminhas no powerup
        if self.powerup_ativo:
            self.fantasmas_comidos += 1
            self.vidas += 1
            return True
        return False
    
    def perder_vida(self): #perde uma vida qnd é comido por um fantasma
        if self.invulneravel:
            return False
        
        self.vidas -= 1
        self.invulneravel = True
        self.temporizador_invulneravel = 0
        
        # Desativa power-up ao perder vida
        if self.powerup_ativo:
            self.desativar_powerup()
        
        if self.vidas <= 0:
            self.game_over = True
            return "game_over"
        
        return "vida_perdida"

    def atualizar_invulnerabilidade(self):
        if self.invulneravel:
            self.temporizador_invulneravel += 1
            if self.temporizador_invulneravel >= self.duracao_invulneravel:
                self.invulneravel = False
                self.temporizador_invulneravel = 0
    
    def mostrar_tempo_faltando_de_powerup(self):
        if not self.powerup_ativo:
            return 0
        return max(0, self.duracao_powerup - (time.time() - self.tempo_inicio_powerup))
    
    def tempo_de_piscar(self):
        return self.powerup_ativo and self.obter_tempo_restante_powerup() <= 5
    
    def desenhar_hud(self,tela, largura, altura): #desenha tipo um menu com vidas, bolinhas, powerup 
        fonte_grande=pygame.font.Font(None, 36)
        fonte_pequena = pygame.font.Font(None, 24)

        texto_vidas = fonte_grande.render(f"Vidas: {self.vidas}", True, (255, 255, 255))
        tela.blit(texto_vidas, (10, 10))

        cor_coracao = (255, 50, 50)
        for i in range(min(self.vidas, 10)):  #no maximo 10 corações 
            x = 20 + i * 25
            y = 50
            #coração simples 
            pygame.draw.circle(tela, cor_coracao, (x, y), 8)
            pygame.draw.circle(tela, cor_coracao, (x + 12, y), 8)
            pygame.draw.polygon(tela, cor_coracao, [
                (x - 8, y + 2),
                (x + 6, y + 16),
                (x + 20, y + 2)
            ])
        
        #bolinhas comidas
        texto_bolinhas = fonte_pequena.render(f"Bolinhas: {self.bolinhas_coletadas}", True, (255, 255, 100))
        tela.blit(texto_bolinhas, (10, 80))
        
        #vida extra depois 
        proxima_vida = 25 - (self.bolinhas_coletadas % 25)
        texto_proxima = fonte_pequena.render(f"Próxima vida em: {proxima_vida}", True, (150, 255, 150))
        tela.blit(texto_proxima, (10, 105))
        
        #status do powerup 
        if self.powerup_ativo:
            tempo_restante = self.obter_tempo_restante_powerup()
            cor_powerup = (255, 100, 0) if tempo_restante <= 5 else (255, 255, 0)
            texto_powerup = fonte_grande.render(f"POWER-UP: {int(tempo_restante)}s", True, cor_powerup)
            retangulo_texto = texto_powerup.get_rect(center=(largura // 2, 30))
            tela.blit(texto_powerup, retangulo_texto)
            
            #quantidade de fantasmas comidos no powerup 
            texto_fantasmas = fonte_pequena.render(f"Fantasmas comidos: {self.fantasmas_comidos}", True, (150, 255, 255))
            tela.blit(texto_fantasmas, (largura // 2 - 80, 60))
        else:
            #aviso de 8 vidas para power up 
            if self.vidas < 8:
                texto_necessario = fonte_pequena.render(f"Power-up em {8 - self.vidas} vidas", True, (200, 200, 200))
                tela.blit(texto_necessario, (largura - 200, 10))
    
        #game over 
        if self.game_over:
            fonte_game_over = pygame.font.Font(None, 72)
            texto_game_over = fonte_game_over.render("GAME OVER", True, (255, 0, 0))
            retangulo_texto = texto_game_over.get_rect(center=(largura // 2, altura // 2))
            
            #relatório final 
            fonte_estatisticas = pygame.font.Font(None, 32)
            texto_estatisticas = fonte_estatisticas.render(f"Bolinhas coletadas: {self.bolinhas_coletadas}", True, (255, 255, 255))
            retangulo_estatisticas = texto_estatisticas.get_rect(center=(largura // 2, altura // 2 + 60))
            tela.blit(texto_estatisticas, retangulo_estatisticas)
        
        #indica quando ele ta invuneravel 
        if self.invulneravel and not self.game_over:
            #texto fica piscando 
            if (self.temporizador_invulneravel // 10) % 2 == 0:
                texto_invuln = fonte_pequena.render("INVENCÍVEL", True, (100, 255, 255))
                tela.blit(texto_invuln, (10, 135))