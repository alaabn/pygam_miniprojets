import pygame, sys
from pygame.locals import *
import random, time
 
pygame.init()
 
font = pygame.font.SysFont(None, 40)

#setting up fps  
FPS = 60
FramePerSec = pygame.time.Clock()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
 
gamewinner = pygame.image.load("6.png")
gamewinner = pygame.transform.scale(gamewinner, (1000, 700)) 

gameover = pygame.image.load("7.png")
gameover = pygame.transform.scale(gameover, (1000, 700)) 

floor = pygame.image.load("1.png")
floor = pygame.transform.scale(floor, (1000, 700)) 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

polytec = pygame.image.load("polytec.png")
pygame.display.set_caption("Projet Semestriel - Alaa Ben Nasr")
pygame.display.set_icon(polytec)

class Elm(pygame.sprite.Sprite):
      def __init__(self, image, center):
        super().__init__() 
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100)) 
        self.rect = self.image.get_rect(center=(50, 50), width=50, height=50)
        self.rect.center = center
      
      def move(self):
        pass
 
 
class Vacuum(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("3.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (180, 140)) 
        self.rect = self.image.get_rect()
        self.rect.center = (170,170)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.bottom < SCREEN_HEIGHT: 
              if pressed_keys[K_DOWN]:
                  self.rect.move_ip(0, 5)
        if self.rect.top > 0:
              if pressed_keys[K_UP]:
                  self.rect.move_ip(0, -5)
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
    
                   
       
V = Vacuum()
 
D1 = Elm("4.png", (830,120))
G1 = Elm("5.png", (830,350))
D2 = Elm("4.png", (830,590))

G2 = Elm("5.png", (590,120))
D3 = Elm("4.png", (590,350))
G3 = Elm("5.png", (590,590))

D4 = Elm("4.png", (350,120))
G4 = Elm("5.png", (350,350))
D5 = Elm("4.png", (350,590))

D6 = Elm("4.png", (110,350))
G5 = Elm("5.png", (110,590))


glasses = pygame.sprite.Group()
glasses.add([G1, G2, G3, G4, G5])

dusts = pygame.sprite.Group()
dusts.add([D1, D2, D3, D4, D5, D6])


all_sprites = pygame.sprite.Group()
all_sprites.add(V)

all_sprites.add(glasses)
all_sprites.add(dusts)
  
while True:   
    DISPLAYSURF.blit(floor, (0,0))
    pygame.time.Clock().tick()
    counting_string = pygame.time.get_ticks() // 1000

    for event in pygame.event.get():  
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
    
 
    for entity in all_sprites:
         DISPLAYSURF.blit(entity.image, entity.rect)
         entity.move()
 
    if pygame.sprite.spritecollideany(V, dusts):
            pygame.sprite.spritecollideany(V, dusts).kill()
 
    if pygame.sprite.spritecollideany(V, glasses) or pygame.time.get_ticks()//1000 > 10:
        time.sleep(1)
        DISPLAYSURF.blit(gameover, (0,0))
        pygame.time.delay(1000)
        pygame.quit()
        sys.exit()

    if len(dusts.sprites()) == 0:
        time.sleep(1)
        DISPLAYSURF.blit(gamewinner, (0,0))   

    counting_text = font.render(str(counting_string), 1, (255,0,0))
    notice_text = font.render("clean the area in less than 10 seconds: ", 1, (140,255,255))

    pygame.draw.rect(DISPLAYSURF, (0,0,0), pygame.Rect(180, 0, 600, 50))
    DISPLAYSURF.blit(notice_text, (200, 10, 600, 50))
    DISPLAYSURF.blit(counting_text, (740, 10, 600, 50))
    pygame.display.update()
    FramePerSec.tick(FPS)