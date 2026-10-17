
import pygame
pygame.init()

screen = pygame.display.set_mode((750, 750))
pygame.display.set_caption("Bulb Simulator")

# Create the bulb images
off = pygame.image.load("images/lights_off.png")
on = pygame.image.load("images/lights_on.png")

# Resize the images
off = pygame.transform.scale(off, (300, 400))
on = pygame.transform.scale(on, (300, 400))


class Bulb:
    def __init__(self):
        self.screen = screen
        self.is_on = False

    def draw(self):
        if self.is_on == True:
            self.screen.blit(on, (225, 175))
        else:
            self.screen.blit(off, (225, 175))


# Create the bulb object
bulb = Bulb()

running = True

while running:
    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            running = False

        # Mouse button down: turn the bulb on
        elif i.type == pygame.MOUSEBUTTONDOWN:
            bulb.is_on = True

        # Mouse button up: turn the bulb off
        elif i.type == pygame.MOUSEBUTTONUP:
            bulb.is_on = False

    # Draw the current bulb image
    screen.fill((30, 30, 30))
    bulb.draw()
    pygame.display.update()

pygame.quit()
