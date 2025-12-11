import pygame
import math 

class AnimationSystem: #classe da parte de animações 
    def __init__(self):
        self.animation_frame=0
        self.animation_speed=0.15
        self.blink_timer=0
    
    def update(self):
        self.animation_frame+=self.animation_speed
        self.blink_timer+=1
    
    def desenhar_estudante_sem_poder(self, tela, x, y, direcao, tamanho=30): #estudante normal 
        cor_da_pele=(255, 220, 177)
        cor_da_camisa=(50,100, 200)
        cor_da_calça=(40,40,80)
        cor_do_bone=(200, 50, 50)
        cor_do_chinelo=(100,100,100)

        boca_aberta=abs(math.sin(self.animation_frame))>0.5
        
        if direcao=="direita":
            pygame.draw.circle(tela, cor_da_camisa, (int(x), int(y)), tamanho) #corpo 
            pygame.draw.circle(tela, cor_da_pele, (int(x + tamanho//3), int(y - tamanho//4)), tamanho//2) #cabeca 
            pygame.draw.polygon(tela, cor_do_bone, [
                (x + tamanho//3 - tamanho//3, y - tamanho//4 - tamanho//3),
                (x + tamanho//3 + tamanho//2, y - tamanho//4 - tamanho//3),
                (x + tamanho//3 + tamanho//3, y - tamanho//4)
            ])
            pygame.draw.circle(tela, (0, 0, 0), (int(x + tamanho//3 + tamanho//6), int(y - tamanho//4)), tamanho//10) #olho

            #agr animação da boca se abrindo 
            if boca_aberta:
                pygame.draw.circle(tela, (0,0,0), (int(x + tamanho//3 + tamanho//4), int(y - tamanho//4 + tamanho//6)), tamanho//8)
            #perna
            pygame.draw.rect(tela, cor_da_calça, (x - tamanho//4, y + tamanho//2, tamanho//3, tamanho//2))
            pygame.draw.rect(tela, cor_da_calça, (x + tamanho//8, y + tamanho//2, tamanho//3, tamanho//2))
            #chinelo 
            pygame.draw.ellipse(tela, cor_do_chinelo, (x - tamanho//4, y + tamanho, tamanho//2, tamanho//4))
            pygame.draw.ellipse(tela, cor_do_chinelo, (x + tamanho//8, y + tamanho, tamanho//2, tamanho//4))

        elif direcao=="esquerda":
            pygame.draw.circle(tela, cor_da_camisa, (int(x), int(y)), tamanho)
            pygame.draw.circle(tela, cor_da_pele, (int(x - tamanho//3), int(y - tamanho//4)), tamanho//2)
            pygame.draw.polygon(tela, cor_do_bone, [
                (x - tamanho//3 + tamanho//3, y - tamanho//4 - tamanho//3),
                (x - tamanho//3 - tamanho//2, y - tamanho//4 - tamanho//3),
                (x - tamanho//3 - tamanho//3, y - tamanho//4)
            ])
            pygame.draw.circle(tela, (0, 0, 0), (int(x - tamanho//3 - tamanho//6), int(y - tamanho//4)), tamanho//10)
            if boca_aberta: 
                pygame.draw.circle(tela, (0, 0, 0), (int(x - tamanho//3 - tamanho//4), int(y - tamanho//4 + tamanho//6)), tamanho//8)
            pygame.draw.rect(tela, cor_da_calça, (x - tamanho//4, y + tamanho//2, tamanho//3, tamanho//2))
            pygame.draw.rect(tela, cor_da_calça, (x + tamanho//8, y + tamanho//2, tamanho//3, tamanho//2))
            pygame.draw.ellipse(tela, cor_do_chinelo, (x - tamanho//4, y + tamanho, tamanho//2, tamanho//4))
            pygame.draw.ellipse(tela, cor_do_chinelo, (x + tamanho//8, y + tamanho, tamanho//2, tamanho//4))
        
        elif direcao=="cima":
            pygame.draw.circle(tela, cor_da_camisa, (int(x), int(y)), tamanho) #a unica coisa que muda aqui é que ele vira de costas
            pygame.draw.circle(tela, cor_da_pele, (int(x), int(y - tamanho//2)), tamanho//2)
            pygame.draw.circle(tela, cor_do_bone, (int(x), int(y - tamanho//2)), tamanho//2 + 2)
            pygame.draw.circle(tela, cor_do_bone, (int(x), int(y - tamanho//2 - tamanho//6)), tamanho//3) #bone agora tem visao de cima 
            pygame.draw.rect(tela, cor_da_calça, (x - tamanho//3, y + tamanho//3, tamanho//4, tamanho//2))
            pygame.draw.rect(tela, cor_da_calça, (x + tamanho//8, y + tamanho//3, tamanho//4, tamanho//2))
        
        elif direcao=="baixo":
            pygame.draw.circle(tela, cor_da_camisa, (int(x), int(y)), tamanho)
            pygame.draw.circle(tela, cor_da_pele, (int(x), int(y - tamanho//3)), tamanho//2)
            pygame.draw.ellipse(tela, cor_do_bone, (x - tamanho//2, y - tamanho//2 - tamanho//3, tamanho, tamanho//3))
            pygame.draw.circle(tela, (0, 0, 0), (int(x - tamanho//6), int(y - tamanho//3)), tamanho//10)
            pygame.draw.circle(tela, (0, 0, 0), (int(x + tamanho//6), int(y - tamanho//3)), tamanho//10)
            if boca_aberta:
                pygame.draw.arc(tela, (0, 0, 0), (x - tamanho//6, y - tamanho//6, tamanho//3, tamanho//4), 0, math.pi, 2)
            pygame.draw.rect(tela, cor_da_calça, (x - tamanho//3, y + tamanho//3, tamanho//4, tamanho//2))
            pygame.draw.rect(tela, cor_da_calça, (x + tamanho//8, y + tamanho//3, tamanho//4, tamanho//2))
            pygame.draw.ellipse(tela, cor_do_chinelo, (x - tamanho//3, y + tamanho - tamanho//4, tamanho//2, tamanho//3))
            pygame.draw.ellipse(tela, cor_do_chinelo, (x + tamanho//8, y + tamanho - tamanho//4, tamanho//2, tamanho//3))
    
    def desenhar_estudante_com_power_up(self, tela, x, y, direcao, tamanho=30): #ele vai botar uma bermuda, bone pra tras e tenis 
        cor_pele = (255, 220, 177)
        cor_camisa = (50, 100, 200)
        cor_bermuda = (100, 100, 150)  
        cor_bone = (200, 50, 50)
        cor_tenis = (255, 255, 255) #tenis branco 

        boca_aberta = abs(math.sin(self.quadro_animacao)) > 0.5

        if direcao=="direita":
            pygame.draw.circle(tela, cor_camisa, (int(x), int(y)), tamanho)
            pygame.draw.circle(tela, cor_pele, (int(x + tamanho//3), int(y - tamanho//4)), tamanho//2)
            pygame.draw.polygon(tela, cor_bone, [
                (x + tamanho//3 - tamanho//2, y - tamanho//4 - tamanho//3),
                (x + tamanho//3 + tamanho//4, y - tamanho//4 - tamanho//3),
                (x + tamanho//3 - tamanho//4, y - tamanho//4)
            ]) #agr o bone vai ficar pra tras 
            pygame.draw.circle(tela, (0, 0, 0), (int(x + tamanho//3 + tamanho//6), int(y - tamanho//4)), tamanho//10)
            if boca_aberta:
                pygame.draw.circle(tela, (0, 0, 0), (int(x + tamanho//3 + tamanho//4), int(y - tamanho//4 + tamanho//6)), tamanho//8)
            pygame.draw.rect(tela, cor_bermuda, (x - tamanho//4, y + tamanho//2, tamanho//3, tamanho//3))
            pygame.draw.rect(tela, cor_bermuda, (x + tamanho//8, y + tamanho//2, tamanho//3, tamanho//3)) #bermuda
            pygame.draw.ellipse(tela, cor_tenis, (x - tamanho//4, y + tamanho - tamanho//6, tamanho//2, tamanho//3))
            pygame.draw.ellipse(tela, cor_tenis, (x + tamanho//8, y + tamanho - tamanho//6, tamanho//2, tamanho//3)) #tenis
            
        elif direcao=="esquerda":
            pygame.draw.circle(tela, cor_camisa, (int(x), int(y)), tamanho)
            pygame.draw.circle(tela, cor_pele, (int(x - tamanho//3), int(y - tamanho//4)), tamanho//2)
            pygame.draw.polygon(tela, cor_bone, [
                (x - tamanho//3 + tamanho//2, y - tamanho//4 - tamanho//3),
                (x - tamanho//3 - tamanho//4, y - tamanho//4 - tamanho//3),
                (x - tamanho//3 + tamanho//4, y - tamanho//4)
            ])
            pygame.draw.circle(tela, (0, 0, 0), (int(x - tamanho//3 - tamanho//6), int(y - tamanho//4)), tamanho//10)
            if boca_aberta:
                pygame.draw.circle(tela, (0, 0, 0), (int(x - tamanho//3 - tamanho//4), int(y - tamanho//4 + tamanho//6)), tamanho//8)
            pygame.draw.rect(tela, cor_bermuda, (x - tamanho//4, y + tamanho//2, tamanho//3, tamanho//3))
            pygame.draw.rect(tela, cor_bermuda, (x + tamanho//8, y + tamanho//2, tamanho//3, tamanho//3))
            pygame.draw.ellipse(tela, cor_tenis, (x - tamanho//4, y + tamanho - tamanho//6, tamanho//2, tamanho//3))
            pygame.draw.ellipse(tela, cor_tenis, (x + tamanho//8, y + tamanho - tamanho//6, tamanho//2, tamanho//3))

        elif direcao=="cima":
            pygame.draw.circle(tela, cor_camisa, (int(x), int(y)), tamanho)
            pygame.draw.circle(tela, cor_pele, (int(x), int(y - tamanho//2)), tamanho//2)
            pygame.draw.circle(tela, cor_bone, (int(x), int(y - tamanho//2)), tamanho//2 + 2)
            pygame.draw.rect(tela, cor_bermuda, (x - tamanho//3, y + tamanho//3, tamanho//4, tamanho//3))
            pygame.draw.rect(tela, cor_bermuda, (x + tamanho//8, y + tamanho//3, tamanho//4, tamanho//3))
        
        elif direcao=="baixo":
            pygame.draw.circle(tela, cor_camisa, (int(x), int(y)), tamanho)
            pygame.draw.circle(tela, cor_pele, (int(x), int(y - tamanho//3)), tamanho//2)
            pygame.draw.ellipse(tela, cor_bone, (x - tamanho//2, y - tamanho//2 - tamanho//3, tamanho, tamanho//3)) #aqui o bone fica com a aba pra tras 
            pygame.draw.circle(tela, (0, 0, 0), (int(x - tamanho//6), int(y - tamanho//3)), tamanho//10)
            pygame.draw.circle(tela, (0, 0, 0), (int(x + tamanho//6), int(y - tamanho//3)), tamanho//10)
            if boca_aberta:
                pygame.draw.arc(tela, (0, 0, 0), (x - tamanho//6, y - tamanho//6, tamanho//3, tamanho//4), 0, math.pi, 2)
            pygame.draw.rect(tela, cor_bermuda, (x - tamanho//3, y + tamanho//3, tamanho//4, tamanho//3))
            pygame.draw.rect(tela, cor_bermuda, (x + tamanho//8, y + tamanho//3, tamanho//4, tamanho//3))
            pygame.draw.ellipse(tela, cor_tenis, (x - tamanho//3, y + tamanho - tamanho//4, tamanho//2, tamanho//3))
            pygame.draw.ellipse(tela, cor_tenis, (x + tamanho//8, y + tamanho - tamanho//4, tamanho//2, tamanho//3))
    
    def desenhar_linguagem(self, tela, x, y, direcao, tipo_linguagem, tamanho=25):
        cores = {
            'python': (52, 102, 153),  #azul do python 
            'c': (85, 85, 170),  #azul meio roxo do C
            'java': (240, 80, 40),  #laranja do java 
            'assembly': (100, 100, 100)  #cinza do assembly 
        }
        cor_base=cores.get(tipo_linguagem, (255, 0,0))

        pygame.draw.circle(tela, cor_base, (int(x), int(y - tamanho//4)), tamanho) #corpo da linguagem meio arredondado
        deslocamento_onda=abs(math.sin(self.quadro_animacao*2))*3
        for i in range(5):
            onda_x = x - tamanho + (i * tamanho//2)
            onda_y = y + tamanho//2 + (deslocamento_onda if i % 2 == 0 else -deslocamento_onda)
            pygame.draw.circle(tela, cor_base, (int(onda_x), int(onda_y)), tamanho//3)
        
        cor_olho = (255, 255, 255)
        cor_pupila = (0, 0, 255) #eles mudam baseado na direção que o fantasma ta indo 

        if direcao=="direita": 
            deslocamento_olho_x = tamanho//6
        elif direcao=="esquerda":
            deslocamento_olho_x = -tamanho//6
        elif direcao=="cima":
            deslocamento_olho_x = 0
        else: #olhando pra baixo 
            deslocamento_olho_x = 0
        
        pygame.draw.circle(tela, cor_olho, (int(x - tamanho//4), int(y - tamanho//3)), tamanho//4)
        pygame.draw.circle(tela, cor_olho, (int(x + tamanho//4), int(y - tamanho//3)), tamanho//4) #olhos brancos 

        pygame.draw.circle(tela, cor_pupila, 
                         (int(x - tamanho//4 + deslocamento_olho_x), int(y - tamanho//3)), tamanho//8)
        pygame.draw.circle(tela, cor_pupila, 
                         (int(x + tamanho//4 + deslocamento_olho_x), int(y - tamanho//3)), tamanho//8) #pupila olhando pra onde o fantasma ta indo 
        
        #simbolos das linguagens
        cor_simbolo = (255, 255, 255)
        fonte = pygame.font.Font(None, tamanho//2)

        simbolos = {
            'python': '🐍',
            'c': 'C',
            'java': '☕',
            'assembly': 'A'
        }

        texto = fonte.render(simbolos.get(tipo_linguagem, '?'), True, cor_simbolo)
        retangulo_texto = texto.get_rect(center=(int(x), int(y + tamanho//4)))
        tela.blit(texto, retangulo_texto)
    
    def desenhar_fantasma_computador(self, tela, x, y, piscar=False, tamanho=25): #quando o personagem entrar em power up, as linguagens vao virar computadores 
        if piscar and (self.temporizador_piscar // 15) % 2 == 0:
            return #ai ele nao desenha, e da o efeito de ficar piscando
        cor_computador = (150, 150, 255)
        cor_tela = (100, 200, 255)
        pygame.draw.rect(tela, cor_computador, (x - tamanho, y - tamanho, tamanho*2, tamanho*1.5)) #corpo do computador 
        pygame.draw.rect(tela, cor_tela, (x - tamanho//1.5, y - tamanho//1.5, tamanho*1.3, tamanho)) #tela 
        pygame.draw.rect(tela, (100, 100, 100), (x - tamanho, y + tamanho//2, tamanho*2, tamanho//3)) #teclado 

        for i in range(3): #detalhes do computador 
            pygame.draw.line(tela, (80, 80, 80), 
                           (x - tamanho + 5, y + tamanho//2 + 5 + i*3),
                           (x + tamanho - 5, y + tamanho//2 + 5 + i*3), 1)

    def desenhar_bolinha(self, tela, x, y, tamanho=5):
        pygame.draw.circle(tela, (255, 255, 100), (int(x), int(y)), tamanho)
        pygame.draw.circle(tela, (255, 255, 200), (int(x - tamanho//3), int(y - tamanho//3)), tamanho//3) #dar um brilho