import pygame, sys

width= 680
height= 480

screen= pygame.display.set_mode((width, height))
screen.fill ((200,250,0))
pygame.display.set_caption("Ciclo Básico Pygame")

pygame.init()

gameOver= False

while not gameOver:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameOver= True
            
    pygame.display.flip()
    
pygame.quit()