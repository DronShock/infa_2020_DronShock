# imports
import pygame
import pygame.draw as d

# initialise game engine
pygame.init()

FPS = 30

# colors in RGB
black = (2, 2, 2)
white = (255, 255, 255)
snow_white = (255, 250, 250)
sky_blue = (135, 206, 235)
red = (255, 0, 0)
fish_fin_color = (221, 166, 166)
fish_body_color = (255, 215, 0)
grey = (128, 128, 128)
see_water_color = (22, 80, 68)
dark_grey = (77, 77, 77)
dark_blue = (0, 0, 128)
green = (0, 128, 128)

# initialise surfaces
main_screen = pygame.display.set_mode((565, 800))
sun = pygame.Surface((565, 800), pygame.SRCALPHA)
bear = pygame.Surface((565, 800))
fish = pygame.Surface((565, 800))

# sky + show
d.rect(main_screen, sky_blue, (0, 0, 794, 442))
d.rect(main_screen, snow_white, (0, 442, 794, 358))

# ice hole
d.ellipse(bear, dark_blue, (313, 557, 215, 70))
d.ellipse(bear, black, (339, 579, 162, 48), 2)
d.ellipse(bear, see_water_color, (340, 580, 160, 46))
d.line(bear, black, (449, 242), (454, 593))  # rope

# sun
d.circle(main_screen, white, (340, 140), 20)
d.circle(main_screen, white, (510, 140), 10)
d.circle(main_screen, white, (329, 300), 10)
d.circle(main_screen, white, (175, 135), 10)
d.circle(sun, (255, 255, 255, 150), (340, 140), 180, 25)
d.line(sun, (255, 255, 255, 150), (160, 134), (520, 141), 30)
d.line(sun, (255, 255, 255, 150), (345, -10), (327, 312), 30)
sun.set_colorkey(black)
main_screen.blit(sun, (0, 0))

# bobber (поплавок)
d.ellipse(bear, red, (447, 577, 20, 30))
d.rect(bear, see_water_color, (447, 592, 20, 30))
d.rect(bear, red, (447, 592, 20, 10))

# coil (катушка)
d.circle(bear, green, (249, 406), 15)
d.circle(bear, black, (249, 406), 10, 5)

# stick (палка = удочка)
d.lines(bear, black, False, [(180, 497), (220, 430), (450, 240)], 4)

# bear body
d.ellipse(bear, white, (95, 294, 120, 71))  # face
d.ellipse(bear, black, (94, 293, 122, 73), 2)  # head
d.circle(bear, black, (145, 323), 5)  # left eye
d.circle(bear, black, (215, 326), 5)  # right eye
d.lines(bear, black, False, [(144, 348), (173, 350), (210, 343)], 2)  # smile
d.ellipse(bear, white, (14, 350, 170, 320))  # body
d.ellipse(bear, black, (13, 349, 172, 322), 2)  # body
d.ellipse(bear, white, (102, 580, 135, 100))  # leg
d.ellipse(bear, black, (101, 579, 135, 102), 2)  # leg
d.ellipse(bear, white, (150, 421, 70, 30))  # hand
d.ellipse(bear, black, (149, 420, 72, 32), 2)  # hand

# bear ear
d.polygon(bear, white,
          [(105, 306), (104, 310), (106, 313), (108, 317), (115, 319),
           (121, 314), (125, 309), (122, 303), (116, 301), (108, 302)])
d.polygon(bear, black,
          [(105, 306), (104, 310), (106, 313), (108, 317), (115, 319),
           (121, 314), (125, 309), (122, 303), (116, 301), (108, 302)], 2)

# fish fins (плавники)
d.polygon(fish, fish_fin_color,
          [(431, 679), (427, 675), (422, 673), (401, 667),
           (447, 659), (452, 662), (456, 667), (456, 674)])
d.polygon(fish, fish_fin_color, [(410, 708), (411, 716), (407, 722),
                                 (403, 727), (427, 724), (427, 718), (423, 708)])
d.polygon(fish, fish_fin_color,
          [(456, 701), (457, 710), (460, 717), (465, 722), (471, 718),
           (478, 711), (483, 705), (474, 705), (468, 704), (463, 700)])

# fish body
d.polygon(fish, fish_body_color,
          [(386, 710), (403, 710), (410, 711), (418, 711), (425, 711),
           (432, 711), (439, 710), (447, 708), (453, 705), (461, 703),
           (467, 700), (474, 696), (480, 692), (485, 687), (490, 681),
           (484, 677), (477, 675), (471, 673), (465, 672), (457, 672),
           (450, 672), (444, 673), (438, 674), (433, 676), (427, 678),
           (422, 681), (417, 684), (411, 687), (406, 691), (401, 694),
           (396, 698), (392, 703), (385, 706), (376, 710), (341, 713),
           (357, 742), (387, 709)])

# fish eye
d.circle(fish, red, (468, 686), 5)
d.circle(fish, black, (468, 686), 2)
d.circle(fish, white, (466, 683), 2)

# bowl
d.polygon(bear, grey, [(285, 555), (328, 555), (348, 462), (265, 462)])
d.ellipse(bear, grey, (268, 456, 80, 20))
d.ellipse(bear, black, (268, 463, 75, 10))

fish.set_colorkey((0, 0, 0))
bear.set_colorkey((0, 0, 0))

# multiplying bears
bear1 = pygame.transform.scale(bear, (211, 300))
bear2 = pygame.transform.scale(bear, (280, 400))
bear3 = pygame.transform.flip(bear, 1, 0)
bear4 = pygame.transform.scale(bear3, (211, 300))

# multiplying fish
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

# posting new bears and fish
main_screen.blit(bear1, (50, 300))
main_screen.blit(bear2, (300, 300))
main_screen.blit(bear4, (50, 500))
main_screen.blit(fish_group, (200, 500))
main_screen.blit(fish_group, (100, 530))
main_screen.blit(fish_r1, (100, 500))
main_screen.blit(fish_r2, (40, 600))
main_screen.blit(fish_r3, (90, 470))
main_screen.blit(fish_r4, (60, 540))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
