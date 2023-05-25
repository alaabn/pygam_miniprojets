import pygame, sys
from pygame.locals import *
import random, time
 
pygame.init()
 
#setting up fps  
FPS = 60
FramePerSec = pygame.time.Clock()
 

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

health_bar_color = GREEN

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
SPEED = 5
 
 
gameover = pygame.image.load("gameover.png")
gameover = pygame.transform.scale(gameover, (240, 120)) 
street = pygame.image.load("road.png")
polytec = pygame.image.load("polytec.png")
 

ROAD = pygame.display.set_mode((500,800))
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)

pygame.display.set_caption("Projet Semestriel - Alaa Ben Nasr")
pygame.display.set_icon(polytec)

scroll = 0 

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("bump.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (90, 90)) 
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 900):
            self.rect.top = 0
            self.rect.center = (random.randint(50, SCREEN_WIDTH - 50), 0)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("car.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 160)) 
        self.rect = self.image.get_rect()
        self.rect.center = (160, 690)
        self.health_bar = 300
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
    
                   
       
E1 = Enemy()
P1 = Player()
 
#grouping elements in different sprites
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(E1)
all_sprites.add(P1)
 
#when user acts the game speed up incrementallu
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
#main game looop
while True:   
    for i in range(3):
         ROAD.blit(street, (0, 0 - i * street.get_height() - scroll  ))

    scroll -= SPEED
    if abs(scroll) >  street.get_height():
        scroll = 0

    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 1.2     
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
    

 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound("crash.mp3").play()
          if P1.health_bar <= 30:
            time.sleep(0.5)

            DISPLAYSURF.fill((0,0,0))      
            DISPLAYSURF.blit(gameover, (130,280))
            
            pygame.display.update()
            for entity in all_sprites:
                    entity.kill() 
            time.sleep(2)
            pygame.quit()
            sys.exit()  
          else:
            if  100 < P1.health_bar < 290:
                health_bar_color = ORANGE
            elif P1.health_bar < 100:
                health_bar_color = RED
            P1.health_bar -= 2     
    
    pygame.draw.rect(DISPLAYSURF, health_bar_color , pygame.Rect(100, 60, P1.health_bar , 60))
    pygame.draw.rect(DISPLAYSURF, (0,0,0), pygame.Rect(100, 60, 300, 60),3)
    pygame.display.update()
    FramePerSec.tick(FPS)