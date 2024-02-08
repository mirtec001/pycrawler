from settings import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.Surface([2,2])
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 100
        self.dx = 0
        self.dy = 0
        self.direction = direction

    def update(self, walls, dt):

        if self.direction == "left":
            self.dx -= self.speed * dt
        if self.direction == "right":
            self.dx += self.speed * dt
        if self.direction == "up":
             self.dy -= self.speed * dt
        if self.direction == "down":
             self.dy += self.speed * dt


        self.rect.x += self.dx
        self.rect.y += self.dy
        
        hits = pygame.sprite.spritecollide(self, walls, False)
        if hits:
                self.kill()
    

    def draw(self, window):
         window.blit(self.image, self.rect)
