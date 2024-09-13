import pygame

pygame.init()

window = pygame.display.set_mode((1000, 1000))
window.fill((0,0,0))

GREEN = (0, 100, 0)

pygame.draw.circle(window, GREEN, (300,300), 50)
pygame.draw.circle(window, GREEN, (300,500), 50,3)

pygame.display.update()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
pygame.QUIT