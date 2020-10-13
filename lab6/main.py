from random import randint, random

import numpy
import pygame

pygame.init()

FPS = 30
screen = pygame.display.set_mode((900, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, GREEN, BLUE, YELLOW, MAGENTA, CYAN]

# задание каличества объектов на экране
n = 5  # шариков
m = 2  # треугольников


def new_ball(ball_opisanye, i):
    """
    Создаёт новый шарик на экране в случае попадания по нему мышкой
    :param ball_opisanye: массив, хранящий описание характеристик шарика
    :param i: итератор массива
    :return: None
    """
    ball_opisanye[i][0] = randint(100, 1000)  # значение координаты x центра шарика
    ball_opisanye[i][1] = randint(100, 800)  # значение координаты y центра шарика
    ball_opisanye[i][2] = COLORS[randint(0, 5)]  # один из шести цветов для шарика
    ball_opisanye[i][3] = randint(30, 50)  # радиус окружности
    ball_opisanye[i][4] = randint(-5, 5)  # коэффициент зависимости координаты у от х при движении по прямой
    ball_opisanye[i][5] = randint(-10, 10)  # скорость приращения координат за одну итерацию цикла отрисовки


def new_triangle(triangle_opisanye, i):
    """
    Создаёт новый треугольник на экране в случае попадания по нему мышкой
    :param triangle_opisanye: массив, хранящий описание характеристик треугольника
    :param i: итератор массива
    :return: None
    """
    triangle_opisanye[i][0] = randint(1000, 1500)  # значение координаты x левой вершины треугольника
    triangle_opisanye[i][1] = randint(500, 700)  # значение координаты у левой вершины треугольника
    triangle_opisanye[i][2] = randint(60, 100)  # высота треугольника, опущенная из левой вершины(характерный размер)
    triangle_opisanye[i][3] = randint(-15, 0)  # скорость приращения координат за одну итерацию цикла отрисовки
    triangle_opisanye[i][4] = randint(0, 2000)  # характерное время для смены цвета с красного на зелёный
    triangle_opisanye[i][5] = RED  # один из двух цветов треугольника: красный или зелёный


""" Наполнение массива, хранящего описание характеристик шарика и треугольника

Сопоставлет каждому значению ball_opisanye[i] и triangle_opisanye[i] соответствующее значение переменной 
при помощи двумерного массива

"""
ball_opisanye = [0] * n
for i in range(n):
    ball_opisanye[i] = [0] * 6
for i in range(n):
    new_ball(ball_opisanye, i)

triangle_opisanye = [0] * m
for i in range(m):
    triangle_opisanye[i] = [0] * 6
for i in range(m):
    new_triangle(triangle_opisanye, i)


def ball_moving(x_cord, y_cord, color, radius):
    """
    Выводит на экран изображение шарика за каждую итерацию цикла орисовки
    :param x_cord: значение координаты x центра шарика
    :param y_cord: значение координаты y центра шарика
    :param color: один из шести цветов для шарика
    :param radius: радиус окружности
    :return: None
    """
    pygame.draw.circle(screen, color, [round(x_cord), round(y_cord)], radius)


def triangle_moving(x_cord, y_cord, color, length):
    """
    Выводит на экран изображение треугольника за каждую итерацию цикла орисовки
    :param x_cord: значение координаты x левой вершины треугольника
    :param y_cord: значение координаты у левой вершины треугольника
    :param color: один из двух цветов треугольника: красный или зелёный
    :param length: высота треугольника, опущенная из левой вершины(характерный размер)
    :return: None
    """
    pygame.draw.polygon(screen, color, [(x_cord, y_cord), (x_cord + length, y_cord - length // 2),
                                        (x_cord + length, y_cord + length // 2)])


score = 0


def click(event):
    """
    Обрабатывает нажатие мышкой
    :param event: метод pygame, отвечающий за левую кнопку мыши
    :return: Выводит в консоль информацию о попадании по объекту
    """
    global score
    l = 0
    for i in range(n):  # проверка попадания по шарику
        if (event.pos[0] - ball_opisanye[i][0]) ** 2 + \
                (event.pos[1] - ball_opisanye[i][1]) ** 2 < ball_opisanye[i][3] ** 2:  # случай попадания
            print('Nice click!')
            score += 1 + 1 / ball_opisanye[i][3] * 100
            new_ball(ball_opisanye, i)
            for j in range(10):
                pygame.draw.circle(screen, COLORS[randint(0, 5)], [event.pos[0], event.pos[1]], (j + 1) * 3, 1)
            break
        else:
            l += 1
    for i in range(m):  # проверка попадания по треугольнику
        if ((event.pos[0] - triangle_opisanye[i][0]) < triangle_opisanye[i][2]) and (
                abs(event.pos[1] - triangle_opisanye[i][1]) < 0.5 * (event.pos[0] - triangle_opisanye[i][0])):
            if triangle_opisanye[i][5] == RED:  # случай попадания по красному цвету
                score -= 3
                print('Oops!')
                new_triangle(triangle_opisanye, i)
                pygame.draw.line(screen, RED, [event.pos[0] - 25, event.pos[1] + 25],
                                 [event.pos[0] + 25, event.pos[1] - 25],
                                 10)
                pygame.draw.line(screen, RED, [event.pos[0] + 25, event.pos[1] + 25],
                                 [event.pos[0] - 25, event.pos[1] - 25],
                                 10)
            else:
                print('Nice click!')  # случай попадания по зелёному цвету
                score += 1 + triangle_opisanye[i][2] / 10
                new_triangle(triangle_opisanye, i)
                for j in range(10):
                    pygame.draw.circle(screen, COLORS[randint(0, 5)], [event.pos[0], event.pos[1]], (j + 1) * 3, 1)
            break
        else:
            l += 1
    if l == n + m:  # случай промаха
        print('Miss!')
        pygame.draw.line(screen, RED, [event.pos[0] - 25, event.pos[1] + 25], [event.pos[0] + 25, event.pos[1] - 25],
                         10)
        pygame.draw.line(screen, RED, [event.pos[0] + 25, event.pos[1] + 25], [event.pos[0] - 25, event.pos[1] - 25],
                         10)


""" Работа главного цикла отрисовки"""
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, 900, 900), 3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(round(score))
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
    """Отрисовка шариков"""
    for i in range(n):
        ball_opisanye[i][0] += ball_opisanye[i][5]
        ball_opisanye[i][1] += ball_opisanye[i][5] * ball_opisanye[i][4]
        ball_moving(ball_opisanye[i][0], ball_opisanye[i][1], ball_opisanye[i][2], ball_opisanye[i][3])
        """Рассчёт отражение шариков от стенок"""
        if ball_opisanye[i][0] + ball_opisanye[i][3] > 900:
            ball_opisanye[i][0] = 899 - ball_opisanye[i][3] - ball_opisanye[i][5]
            ball_opisanye[i][5] = -round(ball_opisanye[i][5] * (random() + 0.5))
            ball_opisanye[i][4] = -ball_opisanye[i][4]
            ball_opisanye[i][3] = randint(30, 50)

        if ball_opisanye[i][0] - ball_opisanye[i][3] < 0:
            ball_opisanye[i][0] = 1 + ball_opisanye[i][3] - ball_opisanye[i][5]
            ball_opisanye[i][5] = -round(ball_opisanye[i][5] * (random() + 0.5))
            ball_opisanye[i][4] = -ball_opisanye[i][4]
            ball_opisanye[i][3] = randint(30, 50)

        if ball_opisanye[i][1] + ball_opisanye[i][3] > 900:
            ball_opisanye[i][1] = 899 - ball_opisanye[i][3] - (ball_opisanye[i][5] * ball_opisanye[i][4])
            ball_opisanye[i][4] = -ball_opisanye[i][4]
            ball_opisanye[i][5] = round(ball_opisanye[i][5] * (random() + 0.5))
            ball_opisanye[i][3] = randint(30, 50)

        if ball_opisanye[i][1] - ball_opisanye[i][3] < 0:
            ball_opisanye[i][1] = 1 + ball_opisanye[i][3] - (ball_opisanye[i][5] * ball_opisanye[i][4])
            ball_opisanye[i][4] = -ball_opisanye[i][4]
            ball_opisanye[i][5] = round(ball_opisanye[i][5] * (random() + 0.5))
            ball_opisanye[i][3] = randint(30, 50)
    """Отрисовка треугольников"""
    for i in range(m):
        triangle_opisanye[i][0] += triangle_opisanye[i][3]
        triangle_opisanye[i][1] += 10 * (numpy.sin(triangle_opisanye[i][0] / 100))
        triangle_opisanye[i][4] += triangle_opisanye[i][3]
        triangle_moving(triangle_opisanye[i][0], round(triangle_opisanye[i][1]), triangle_opisanye[i][5],
                        triangle_opisanye[i][2])
        """Смена цвета треугольников"""
        if triangle_opisanye[i][4] < 0:
            triangle_opisanye[i][5] = GREEN
        if triangle_opisanye[i][4] < -300:
            triangle_opisanye[i][5] = RED
            triangle_opisanye[i][4] = 500
        """Создание нового треугольника в случае его выхода за пределы экрана"""
        if (triangle_opisanye[i][0] + triangle_opisanye[i][2]) < 0:
            new_triangle(triangle_opisanye, i)

    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()
