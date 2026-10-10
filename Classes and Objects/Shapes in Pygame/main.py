import pygame
pygame.init()
import random

screen = pygame.display.set_mode((750, 750))

class Circles:
    def __init__(self, radius, color, position):
        self.radius = radius
        self.color = color
        self.position = position
        self.screen = screen
    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.radius)
    def grow(self):
        self.radius += 50
        pygame.draw.circle(self.screen, self.color, self.position, self.radius)

circles = Circles(50,(random.randint(0,255), random.randint(0,255), random.randint(0,255)), (random.randint(50,600), random.randint(50, 600)))

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            circles.draw()
            pygame.display.update()
        elif i.type == pygame.MOUSEBUTTONUP:
            circles.grow()
            pygame.display.update()
        elif i.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            mousecircles = Circles(10,(random.randint(0,255), random.randint(0,255), random.randint(0,255)), pos)
            mousecircles.draw()
            pygame.display.update()

    
    

