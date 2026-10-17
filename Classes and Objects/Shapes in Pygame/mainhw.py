
import pygame
pygame.init()
import random

screen = pygame.display.set_mode((750, 750))

class Rect:
    def __init__(self, color, x, y, w, h):
        self.color = color
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.w, self.h))

    def grow(self):
        self.w += 50
        self.h += 50
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.w, self.h))


rectangle = Rect((random.randint(0,255), random.randint(0,255), random.randint(0,255)), 300, 300, 50, 100)

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()

        if i.type == pygame.MOUSEBUTTONDOWN:
            rectangle.draw()
            pygame.display.update()

        elif i.type == pygame.MOUSEBUTTONUP:
            rectangle.grow()
            pygame.display.update()

        elif i.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            mouse_rect = Rect(
                (random.randint(0, 255),
                 random.randint(0, 255),
                 random.randint(0, 255)),
                pos[0], pos[1], 20, 40
            )
            mouse_rect.draw()
            pygame.display.update()

pygame.quit()