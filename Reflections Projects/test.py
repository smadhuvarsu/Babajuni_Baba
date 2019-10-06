# Pygame template - skeleton for a new pygame project
import pygame
import random
import os

#image=[pygame.image.load("("GF_1.png") , pygame.image.load(" pygame.image.load("("GF_2.png") , pygame.image.load(" pygame.image.load("("GF_3.png") , pygame.image.load(" pygame.image.load("("GH_4.png")]
#image=[pygame.image.load("("swirlstroke_yellow.png"), pygame.image.load("pygame.image.load("("bean_blue.png"), pygame.image.load("pygame.image.load("("bean_green.png"), pygame.image.load("pygame.image.load("("bean_orange.png"), pygame.image.load("pygame.image.load("("bean_pink.png"), pygame.image.load("pygame.image.load("("bean_purple.png"), pygame.image.load("pygame.image.load("("bean_red.png"), pygame.image.load("pygame.image.load("("bean_white.png"), pygame.image.load("pygame.image.load("("bean_yellow.png"), pygame.image.load("pygame.image.load("("swirl_blue.png"), pygame.image.load("pygame.image.load("("swirl_green.png"), pygame.image.load("pygame.image.load("("swirl_orange.png"), pygame.image.load("pygame.image.load("("swirl_pink.png"), pygame.image.load("pygame.image.load("("swirl_purple.png"), pygame.image.load("pygame.image.load("("swirl_red.png"), pygame.image.load("pygame.image.load("("swirl_teal.png"), pygame.image.load("pygame.image.load("("swirl_yellow.png"), pygame.image.load("pygame.image.load("("swirlstroke_blue.png"), pygame.image.load("pygame.image.load("("swirlstroke_green.png"), pygame.image.load("pygame.image.load("("swirlstroke_orange.png"), pygame.image.load("pygame.image.load("("swirlstroke_pink.png"), pygame.image.load("pygame.image.load("("swirlstroke_purple.png"), pygame.image.load("pygame.image.load("("swirlstroke_red.png"), pygame.image.load("pygame.image.load("("swirlstroke_teal.png")]
#image=[pygame.image.load("Water Bottle.png"), pygame.image.load("Apricot Jam.png"),pygame.image.load("Bagel.png"), pygame.image.load("Boiled Egg.png"), pygame.image.load("Cereal.png"), pygame.image.load("Cheese.png"), pygame.image.load("Coffee.png"), pygame.image.load("Egg.png"), pygame.image.load("Fork.png"),pygame.image.load("Fried Egg.png"), pygame.image.load("Glass Orange Juice.png"), pygame.image.load("Glass Strawberry Milk.png"),pygame.image.load("Green Bottle.png"),pygame.image.load("Green Tea.png"), pygame.image.load("Honey.png"), pygame.image.load("Jug.png"), pygame.image.load("Knife.png"), pygame.image.load("Milk Glass.png"), pygame.image.load("Milk.png"), pygame.image.load("Nutella.png"), pygame.image.load("Pancakes.png"), pygame.image.load("Peanutbutter.png"), pygame.image.load("Plate.png"), pygame.image.load("Pretzel.png"), pygame.image.load("Spoon.png"), pygame.image.load("Strawberry Jam.png"), pygame.image.load("Strawberry Milk.png"), pygame.image.load("Tea.png")]

'''left=[pygame.image.load("Boochi_left")]
right=[pygame.image.load("Boochi_Right")]
stand=[pygame.image.load("Boochi_Straight")]
back=[pygame.image.load("Boochi_back")]'''


WIDTH = 1000
HEIGHT = 500
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0,255,255)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bunny's Breakfast Instructions: Use the arrow keys to help bunny eat it's breakfast. Watch out for the red poison dots!")
clock = pygame.time.Clock()


#Fruits class
class Fruits(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((10,20))
        self.image.fill(RED)
        self.images=[pygame.image.load("Buddha_Bg.png"), pygame.image.load("RB.png"),pygame.image.load("OB.png"),pygame.image.load("YB.png"),pygame.image.load("GB.png"),pygame.image.load("BB.png"),pygame.image.load("VB.png"),pygame.image.load("PB.png")]
        #self.image=pygame.image.load("bean_blue.png").convert()
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(0,WIDTH-self.rect.width)
        self.rect.y=random.randrange(10,50)

all_sprites = pygame.sprite.Group()
fruits = pygame.sprite.Group()

for i in range(100):
    f=Fruits()
    all_sprites.add(f)
    fruits.add(f)

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
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()


