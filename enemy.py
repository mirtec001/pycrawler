from settings import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([CELL, CELL])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
    
    def update(self):
        pass


    def draw(self, window):
        window.blit(self.image, self.rect)
