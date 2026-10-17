import pygame
pygame.init()

import time

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Birthday Card")


while True:
    vc = pygame.image.load("images/vanilla_cake.jpg")
    vc = pygame.transform.scale(vc, (WIDTH, HEIGHT))
    screen.blit(vc, (0,0))
    pygame.display.update()
    time.sleep(5)
    
    b = pygame.image.load("images/balloons.png")
    b = pygame.transform.scale(b, (WIDTH, HEIGHT))
    screen.blit(b, (0,0))
    pygame.display.update()
    time.sleep(5)
    
    pp = pygame.image.load("images/party_popper.jpg")
    pp = pygame.transform.scale(pp, (WIDTH, HEIGHT))
    screen.blit(pp, (0,0))
    pygame.display.update()
    time.sleep(5)


