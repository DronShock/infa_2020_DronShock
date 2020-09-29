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

d.ellipse(bear, (255, 0, 0), (447, 577, 20, 30))
d.rect(bear, (22, 80, 68), (447, 592, 20, 30))
d.rect(bear, (0, 0, 255), (447, 592, 20, 10))

d.circle(bear, (128, 128, 192), (249, 406), 15)
d.circle(bear, (0, 0, 0), (249, 406), 10, 5)

d.lines(bear, (0, 0, 1), False, [(180, 497), (220, 430), (450, 240)], 4)

d.ellipse(bear, (255, 255, 255), (95, 294, 120, 71))
d.ellipse(bear, (0, 0, 1), (94, 293, 122, 73), 1)
d.circle(bear, (1, 0, 0), (145, 323), 5)
d.circle(bear, (1, 0, 0), (215, 326), 5)
d.lines(bear, (0, 0, 1), False, [(144, 348), (173, 350), (210, 343)], 1)
d.ellipse(bear, (255, 255, 255), (14, 350, 170, 320))
d.ellipse(bear, (0, 0, 1), (13, 349, 172, 322), 1)
d.ellipse(bear, (255, 255, 255), (102, 580, 135, 100))
d.ellipse(bear, (0, 0, 1), (101, 579, 135, 102), 1)
d.ellipse(bear, (255, 255, 255), (183, 660, 100, 35))
d.ellipse(bear, (0, 0, 1), (182, 659, 102, 37), 1)
d.ellipse(bear, (255, 255, 255), (150, 421, 70, 30))
d.ellipse(bear, (0, 0, 1), (149, 420, 72, 32), 1)
d.polygon(bear, (255, 255, 255),
          [(105, 306), (104, 310), (106, 313), (108, 317), (115, 319), (121, 314), (125, 309), (122, 303), (116, 301),
           (108, 302)])
d.polygon(bear, (0, 0, 1),
          [(105, 306), (104, 310), (106, 313), (108, 317), (115, 319), (121, 314), (125, 309), (122, 303), (116, 301),
           (108, 302)], 1)

d.polygon(fish, (221, 166, 166),
          [(431, 679), (427, 675), (422, 673), (401, 667), (447, 659), (452, 662), (456, 667), (456, 674)])
d.polygon(fish, (221, 166, 166), [(410, 708), (411, 716), (407, 722), (403, 727), (427, 724), (427, 718), (423, 708)])
d.polygon(fish, (221, 166, 166),
          [(456, 701), (457, 710), (460, 717), (465, 722), (471, 718), (478, 711), (483, 705), (474, 705), (468, 704),
           (463, 700)])
d.polygon(fish, (191, 203, 200),
          [(386, 710), (403, 710), (410, 711), (418, 711), (425, 711), (432, 711), (439, 710), (447, 708), (453, 705),
           (461, 703), (467, 700), (474, 696), (480, 692), (485, 687), (490, 681),
           (484, 677), (477, 675), (471, 673), (465, 672), (457, 672), (450, 672), (444, 673), (438, 674), (433, 676),
           (427, 678), (422, 681), (417, 684), (411, 687), (406, 691), (401, 694), (396, 698), (392, 703), (385, 706),
           (376, 710), (341, 713), (357, 742), (387, 709)])
d.circle(fish, (0, 0, 255), (468, 686), 5)
d.circle(fish, (0, 0, 1), (468, 686), 2)
d.circle(fish, (255, 255, 255), (466, 683), 2)

d.polygon(bear, (127, 127, 127), [(285, 555), (328, 555), (348, 462), (265, 462)])
d.ellipse(bear, (127, 127, 127), (268, 456, 80, 20))
d.ellipse(bear, (0, 0, 1), (268, 463, 75, 10))

fish.set_colorkey((0, 0, 0))
med.set_colorkey((0, 0, 0))

bear1 = pygame.transform.scale(bear, (211, 300))
bear2 = pygame.transform.scale(bear, (280, 400))
bear3 = pygame.transform.flip(bear, 1, 0)
bear4 = pygame.transform.scale(bear3, (211, 300))

fish1 = pygame.transform.scale(fish, (200, 200))
fish_r1 = pygame.transform.rotate(fish1, 30)
fish_r2 = pygame.transform.rotate(fish1, 60)
fish_r3 = pygame.transform.rotate(fish1, 90)
fish_r4 = pygame.transform.rotate(fish1, 120)
fish_group = pygame.Surface((400, 400))
fish_group.blit(fish_r1, (70, 80))
fish_group.blit(fish_r2, (75, 80))
fish_group.blit(fish_r3, (100, 100))
fish_group.blit(fish_r4, (100, 150))
fish_group.set_colorkey((0, 0, 0))

sc.blit(bear1, (50, 300))
sc.blit(bear2, (300, 300))
sc.blit(bear4, (50, 500))
sc.blit(fish_group, (200, 500))
sc.blit(fish_group, (100, 530))
sc.blit(fish_r1, (100, 500))
sc.blit(fish_r2, (40, 600))
sc.blit(fish_r3, (90, 470))
sc.blit(fish_r4, (60, 540))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
