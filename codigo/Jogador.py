import pygame
import Personagem
import Mapa
import Constantes as C
from sistema_de_vidas import SistemaVidas
from animacoes_jogo import AnimationSystem


class Jogador(Personagem.Personagem):
    def __init__(self, x, y, mapa):
        super().__init__(x, y, mapa)

        self.animations = {
            "cima": [pygame.image.load(p).convert_alpha() for p in C.upAnim],
            "baixo": [pygame.image.load(p).convert_alpha() for p in C.downAnim],
            "esquerda": [pygame.image.load(p).convert_alpha() for p in C.leftAnim],
            "direita": [pygame.image.load(p).convert_alpha() for p in C.rightAnim],
        }

        for key in self.animations:
            self.animations[key] = [
                pygame.transform.scale(img, (C.TILE_SIZE-2, C.TILE_SIZE-2))
                for img in self.animations[key]
            ]

        self.frame_index = 0
        self.frame_counter = 0
        self.frame_delay = 8  # troca a cada 8 frames (~7.5 animações/s)

        self.image = self.animations["baixo"][0]
        self.rect = self.image.get_rect(topleft=(x, y))

        self.speed = 3
        self.anim = AnimationSystem()
        self.facing = "baixo"
        self.tracker = SistemaVidas()
        self.alive = True
        
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
        enemies_hit = pygame.sprite.spritecollide(self, self.mapa.ghosts, False)
        if enemies_hit:
            for enemy in enemies_hit:
                if self.tracker.powerup_ativo:
                    enemy.rect.topleft = enemy.spawn
                    self.tracker.fantasmas_comidos += 1
                else:
                    self.alive = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)


    def update(self, dt):
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
        
        walls = self.mapa.get_walls()
        old_pos = self.rect.topleft

        self.rect.x += self.next_direction[0] * self.speed #* dt
        self.rect.y += self.next_direction[1] * self.speed #* dt

        wall_hits = pygame.sprite.spritecollide(self, walls, False)
        if not wall_hits:
            self.direction = self.next_direction
        else:
            self.rect.topleft = old_pos
            self.rect.x += self.direction[0] * self.speed
            self.rect.y += self.direction[1] * self.speed

            hit_list = pygame.sprite.spritecollide(self, walls, False)
            if hit_list:
                self.rect.topleft = old_pos
        
        
        if self.direction != (0, 0):
            self.frame_counter += 1
            if self.frame_counter >= self.frame_delay:
                self.frame_counter = 0
                self.frame_index = (self.frame_index + 1) % 2
        else:
            self.frame_index = 0

        self.image = self.animations[self.facing][self.frame_index]


        self.objects_colision()