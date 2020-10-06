import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 10
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

n=5
class Ball:
    kol=0
    def move(self, dx, dy, dcolor):
        self.x += dx
        self.y += dy
        self.dcolor = dcolor

    def create(self):
        self.x = randint(100, 700)
        self.y = randint(100, 500)
        self.r = randint(30, 50)
        self.color = COLORS[randint(0, 5)]

    def __init__(self, x=0, y=0, r=0, color=0):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
ball=[]
while Ball.kol!=n:
    ball[n]=Ball
    ball[n].create

pygame.display.update()
clock = pygame.time.Clock()
finished = False
time = 0
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
    pygame.display.update()
    time += 1;
    screen.fill(BLACK)

pygame.quit()






"""
def click(event):
    global score,n
    end = 0
    if event.button == 1:
        for i in range(2):
            if ((event.pos[0] - x[i]) ** 2 + (event.pos[1] - y[i]) ** 2) < r[i] ** 2:
                print('Got it!')
                score += 1
                end = 1
                n-=1
                break
        if end == 0:
            print('Miss!')
score = 0
n=0
def click(event):
    global score,n
    end = 0
    if event.button == 1:
        for i in range(2):
            if ((event.pos[0] - x[i]) ** 2 + (event.pos[1] - y[i]) ** 2) < r[i] ** 2:
                print('Got it!')
                score += 1
                end = 1
                n-=1
                break
        if end == 0:
            print('Miss!')

"""
