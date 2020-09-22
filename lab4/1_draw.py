import pygame
import pygame.draw as d

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

d.rect(screen, (255, 0, 255), (100, 100, 200, 200))
d.rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
d.polygon(screen, (255, 255, 0), [(100, 100), (200, 50),
                                  (300, 100), (100, 100)])
d.polygon(screen, (0, 0, 255), [(100, 100), (200, 50),
                                (300, 100), (100, 100)], 5)
d.circle(screen, (255, 255, 0), (200, 175), 100)
d.circle(screen, (255, 0, 0), (150, 150), 20)
d.circle(screen, (255, 0, 0), (250, 150), 20)
d.circle(screen, (0, 0, 0), (150, 150), 10)
d.circle(screen, (0, 0, 0), (250, 150), 10)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
