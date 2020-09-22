import pygame
import pygame.draw as d

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

d.rect(screen, (255, 255, 255), (0, 0, 400, 400))
d.circle(screen, (255, 255, 0), (200, 175), 100)
d.circle(screen, (0, 0, 0), (200, 175), 101, 1)
d.line(screen, (0, 0, 0), (95, 80), (180, 140), 10)
d.line(screen, (0, 0, 0), (220, 140), (300, 105), 10)
d.circle(screen, (255, 0, 0), (150, 150), 20)
d.circle(screen, (0, 0, 0), (150, 150), 21,1)
d.circle(screen, (255, 0, 0), (250, 150), 15)
d.circle(screen, (0, 0, 0), (250, 150), 16,1)
d.circle(screen, (0, 0, 0), (150, 150), 10)
d.circle(screen, (0, 0, 0), (250, 150), 8)
d.rect(screen, (0, 0, 0), (145, 220, 110, 25))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
