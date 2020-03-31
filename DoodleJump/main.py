import pygame
import sys
import random
class DoodleJump():
    def __init__(self):
        self.screen = pygame.display.set_mode((800,600))
        pygame.font.init()
        # pygame.display.init()
        self.green = pygame.image.load("/home/martos/Documents/code/python/DoodleJump/images/green.png").convert_alpha()
        self.platforms=[]
        self.font = pygame.font.SysFont("Arial", 25)
        self.cameray = 0
        self.direction = 0
        self.playerx = 400
        self.playery = 400
        self.jump = False
        self.gravity = 0
        self.xmovement = 0
        self.playerRight = pygame.image.load("/home/martos/Documents/code/python/DoodleJump/images/right.png").convert_alpha()
    def updatePlayer(self):
        # if not self.jump:
        #     self.playery += self.gravity
        #     self.gravity += 1
        # else:
        #     self.playery -= self.jump
        #     self.jump -= 1
        key = pygame.event.get()
        for event in key:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self.xmovement < 10:
                        self.xmovement += 1
                        print('lol')
                    self.direction = 0
                elif event.key == pygame.K_RIGHT:
                    if self.xmovement > -10:
                        self.xmovement -= 1 
                    self.direction = 1
                else:
                    if self.xmovement>0:
                        self.xmovement -= 1
                    elif self.xmovement<0:
                        self.xmovement+=1
            self.playerx + self.xmovement
        self.screen.blit(self.playerRight, (self.playerx, 250))
    def updatePlatforms(self):
        self.cameray -= 5
        for p in self.platforms:
            self.screen.blit(self.green, (p[0], p[1] - self.cameray))

    def drawPlatforms(self):
        for p in self.platforms:
            check = self.platforms[1][1] - self.cameray
            if check > 600:
                self.platforms.append([random.randint(0,700), self.platforms[-1][1] - 50])
                self.platforms.pop(0)
            self.screen.blit(self.green, (p[0], p[1]-self.cameray))
    def generatePlatforms(self):
        on = 600
        while on > -100:
            x = random.randint(0, 700)
            self.platforms.append([x, on])
            on -= 50
    def drawGrid(self):
        for x in range(80):
            pygame.draw.line(self.screen, (222,222,222), (x*12,0), (x*12,600))
            pygame.draw.line(self.screen, (222,222,222), (0,x*12), (800,x*12))
    def run(self):
        clock = pygame.time.Clock()
        self.generatePlatforms()
        while True:
            self.screen.fill((255,255,255))
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
            self.drawGrid()
            self.drawPlatforms()
            self.updatePlatforms()
            self.updatePlayer()
            pygame.display.flip()
DoodleJump().run()
            
