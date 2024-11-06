"""
fish is angry cause he cant catch orange box floating around
"""

#import and initialize
import pygame
pygame.init()

#display configuration
screen = pygame.display.set_mode((480, 480))
#pygame.display.set_caption("insert text here")

#Entities
#background
background = pygame.Surface(screen.get_size())
background.fill(pygame.Color(50,100,150))

#box entity 
box = pygame.Surface((25,25))
box.fill((200,100,50))

#fish entity
fish = pygame.image.load("Angryfish.png")
#fish = fish.convert_alpha()
fish = pygame.transform.scale(fish, (75,75))

#assign values to key variables
clock = pygame.time.Clock()

#box start point
box_x = 100
box_y = 100

#fish start point
fish_x = 0
fish_y = 0

#Loop
keepgoing = True
while keepgoing:
    #timer to set frame rate
    clock.tick(24)
    
    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepgoing = False
    
    #make the box move
    box_x = box_x + 5
    box_y = box_y + 5
    if box_x > screen.get_width():
        box_x = 0
        box_y = 0
     
    #make the fish move
    fish_x = fish_x + 5
    fish_y = fish_y + 5
    if fish_x > screen.get_width():
        fish_x = 0
        fish_y = 0
    
    #refresh display
    screen.blit(background, (0, 0))
    screen.blit(box, (box_x, box_y))
    screen.blit(fish,(fish_x, fish_y))
    pygame.display.flip()
    
#pygame.quit()
    #idk if this is working right?