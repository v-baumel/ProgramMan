import pygame
import Personagem
import Mapa
import Constantes as C
from sistema_de_vidas import SistemaVidas
from animacoes_jogo import AnimationSystem


class Jogador(Personagem.Personagem):
    def __init__(self, x, y, mapa):
        super().__init__(x, y, mapa)
        self.speed = 2
        self.image.fill(C.YELLOW)
        self.anim = AnimationSystem()
        self.facing = "baixo"
        self.tracker = SistemaVidas()
        
    def handle_input(self):
        keys = pygame.key.get_pressed()
        nd = (0, 0)
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            nd = (-1, 0)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            nd = (1, 0)
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            nd = (0, -1)
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            nd = (0, 1)
        if nd != (0, 0):
            self.next_direction = nd

    def objects_colision(self):
        pellets = self.mapa.get_pellets()
        power_up = self.mapa.get_upgrade()
        fruits = self.mapa.get_fruit()
        
        pellet_hits = pygame.sprite.spritecollide(self,pellets,False)
        if pellet_hits :
            for pellet in pellet_hits:
                pellet.kill()
                self.tracker.coletar_bolinha()
        
        power_hit = pygame.sprite.spritecollide(self,power_up,False)
        if power_hit:
            for pp in power_hit:
                pp.kill()
                #self.tracker.ativar_power_up()
                self.tracker.coletar_power_up()
        
        fruits_hit = pygame.sprite.spritecollide(self,fruits,False)
        if fruits_hit:
            for fruits_hited in fruits_hit:
                fruits_hited.kill()
                self.tracker.colect_fruits()

    def draw(self, surface):
        self.anim.update()
        size = max(1, int(C.TILE_SIZE // 2 - 2))
        x, y = self.rect.center
        facing = ""
        dx,dy = self.direction
        if dx < 0:
            facing = "esquerda"
        elif dx > 0:
            facing = "direita"
        elif dy < 0:
            facing = "cima"
        elif dy > 0:
            facing = "baixo"
        else:
            facing = "direita"
        self.anim.desenhar_estudante_sem_poder(surface, x, y, facing, size)

    def update(self, dt):
        super().update(dt)
        if self.direction != (0, 0):
            dx, dy = self.direction
            if dx < 0:
                self.facing = "esquerda"
            elif dx > 0:
                self.facing = "direita"
            elif dy < 0:
                self.facing = "cima"
            elif dy > 0:
                self.facing = "baixo"

        self.objects_colision()