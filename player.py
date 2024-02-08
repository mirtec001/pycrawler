from settings import *
from bullet import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = pygame.Surface([CELL, CELL])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 0
        self.vel_y = 0
        self.dx = 0
        self.dy = 0
        self.speed = 100

    def update(self, walls, dt):
        self.vel_x = 0
        self.vel_y = 0

        keys = pygame.key.get_pressed()
        
        # Y movement
        if (keys[pygame.K_w]):
            self.vel_y = -(self.speed * dt)
        if (keys[pygame.K_s]):
            self.vel_y = self.speed * dt

        # X movement            
        if (keys[pygame.K_a]):
            self.vel_x = -(self.speed * dt)
        if (keys[pygame.K_d]):
            self.vel_x = self.speed * dt
        

        self.rect.x += self.vel_x
        self.check_collision('x', walls)
        self.rect.y += self.vel_y
        self.check_collision('y', walls)

    def check_collision(self, dir, walls):
        # check the x axis
        if dir == 'x':
            hits = pygame.sprite.spritecollide(self, walls, False)
            if hits:
                if self.vel_x < 0:
                    self.rect.left = hits[0].rect.right
                    self.vel_x = 0
                if self.vel_x > 0:
                    self.rect.right = hits[0].rect.left
                    self.vel_x = 0
        
        # now we need another check for the y axis
        else:
            hits = pygame.sprite.spritecollide(self, walls, False)
            if hits:
                if self.vel_y < 0:
                    self.rect.top = hits[0].rect.bottom
                    self.vel_y = 0
                if self.vel_y > 0:
                    self.rect.bottom = hits[0].rect.top
                    self.vel_y = 0

    def draw(self, window):
        window.blit(self.image, self.rect)