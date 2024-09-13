import pygame

pygame.init()
screen = pygame.display.set_mode((400,300))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen, (255,255, 255),pygame.Rect(90,90,60,60))

    pygame.display.flip()