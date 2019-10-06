# Pygame template - skeleton for a new pygame project
import pygame
import random
import time

WIDTH = 1000
HEIGHT = 700
FPS = 100

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Find Your Inner Rainbow")
clock = pygame.time.Clock()

bg=pygame.image.load("Buddha_Bg.png")
RB=pygame.image.load("RB.png")
OB=pygame.image.load("OB.png")
YB=pygame.image.load("YB.png")
GB=pygame.image.load("GB.png")
BB=pygame.image.load("BB.png")
VB=pygame.image.load("VB.png")
PB=pygame.image.load("PB.png")

#bg=[pygame.image.load("Buddha_Bg.png"), pygame.image.load("RB.png"),pygame.image.load("OB.png"),pygame.image.load("YB.png"),pygame.image.load("GB.png"),pygame.image.load("BB.png"),pygame.image.load("VB.png"),pygame.image.load("PB.png")]

class Buddha(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((10,20))
        self.image=[pygame.image.load("Buddha_Bg.png"), pygame.image.load("RB.png"),pygame.image.load("OB.png"),pygame.image.load("YB.png"),pygame.image.load("GB.png"),pygame.image.load("BB.png"),pygame.image.load("VB.png"),pygame.image.load("PB.png")]
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(0,WIDTH-self.rect.width)
        self.rect.y=random.randrange(10,50)

all_sprites = pygame.sprite.Group()
buddhagrp = pygame.sprite.Group()

for i in range(10):
    f=Buddha()
    all_sprites.add(f)
    buddhagrp.add(f)

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()
    
    # Draw / render
    
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()


