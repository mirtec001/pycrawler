from settings import *
from player import *
from wall import *
from bullet import *


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Dungeon")
        self.running = True
        self.player = Player(64, 64)
        self.walls = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.bullet_interval = 30
        self.font = pygame.font.Font("freesansbold.ttf", 32)

    def run(self):

        gamemap = self.read_map()
        # read in our map
        for x in range(len(gamemap)):
            for y in range(len(gamemap[x])):
                if (gamemap[x][y] == "1"):
                    self.walls.add(Wall(y * CELL, x * CELL))
        bullet_cooldown = 0
        while(self.running):
            self.text = self.font.render(str(len(self.bullets)), True, WHITE)
            self.text_rect = self.text.get_rect()
            self.text_rect.x = 2
            self.text_rect.y = 1
            
            dt = self.clock.tick(FPS) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            


            keys = pygame.key.get_pressed()


            if keys[pygame.K_j] and bullet_cooldown == 0:
                self.bullets.add(Bullet(self.player.rect.x + 2, self.player.rect.y + 2, "left"))
                bullet_cooldown = self.bullet_interval

            if keys[pygame.K_l] and bullet_cooldown == 0:
                self.bullets.add(Bullet(self.player.rect.x + 2, self.player.rect.y + 2, "right"))
                bullet_cooldown = self.bullet_interval

            if keys[pygame.K_i] and bullet_cooldown == 0:
                self.bullets.add(Bullet(self.player.rect.x + 2, self.player.rect.y + 2, "up"))
                bullet_cooldown = self.bullet_interval

            if keys[pygame.K_k] and bullet_cooldown == 0:
                self.bullets.add(Bullet(self.player.rect.x + 2, self.player.rect.y + 2, "down"))
                bullet_cooldown = self.bullet_interval
            
            bullet_cooldown -= 1
            if bullet_cooldown <= 0:
                bullet_cooldown = 0

            self.update(dt)
            self.draw()



    def update(self, dt):
        
        self.player.update(self.walls, dt)
        self.bullets.update(self.walls, dt)
        # Collision detection
        
        

    def draw(self):
        self.window.fill(BLACK)

        self.player.draw(self.window)
        self.walls.draw(self.window)        
        self.bullets.draw(self.window)
        self.window.blit(self.text, self.text_rect)

        pygame.display.update()


    def read_map(self):
        gamemap = []
        with open("map1.txt", "r") as fr:
            lines = fr.readlines()
            for line in lines:
                temp = []
                for char in line:
                    temp.append(char)
                gamemap.append(temp)

        return gamemap