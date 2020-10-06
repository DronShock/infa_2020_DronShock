import pygame
import pygame.draw as d

pygame.init()

FPS = 30
sc = pygame.display.set_mode((565, 800))
sun = pygame.Surface((565, 800), pygame.SRCALPHA)
bear = pygame.Surface((565, 800))
fish = pygame.Surface((565, 800))

d.rect(sc, (0, 255, 255), (0, 0, 794, 442))
d.rect(sc, (255, 255, 255), (0, 442, 794, 358))
'''
фон
'''
d.ellipse(bear, (77, 77, 77), (313, 557, 215, 70))
d.ellipse(bear, (0, 0, 0), (339, 579, 162, 48), 1)
d.ellipse(bear, (22, 80, 68), (340, 580, 160, 46))
d.line(bear, (0, 0, 1), (449, 242), (454, 593))
d.circle(sc, (255, 255, 255), (340, 140), 20)
d.circle(sc, (255, 255, 255), (510, 140), 10)
d.circle(sc, (255, 255, 255), (329, 300), 10)
d.circle(sc, (255, 255, 255), (175, 135), 10)
d.circle(sun, (255, 255, 255, 150), (340, 140), 180, 25)
d.line(sun, (255, 255, 255, 150), (160, 134), (520, 141), 30)
d.line(sun, (255, 255, 255, 150), (345, -10), (327, 312), 30)
sun.set_colorkey((0, 0, 0))
sc.blit(sun, (0, 0))
'''
солнце
'''

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
