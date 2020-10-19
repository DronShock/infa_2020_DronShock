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
    l = 0  # считает количество объектов, по которым не было произведено нажатие
    # (если оно равно общему числу, то получем промах)
    for i in range(n):  # проверка попадания по шарику
        if (event.pos[0] - ball_opisanye[i][0]) ** 2 + \
                (event.pos[1] - ball_opisanye[i][1]) ** 2 < ball_opisanye[i][3] ** 2:  # случай попадания
            print('Nice click!')
            """Начисление очков, число которых зависит от размера и скорости шарика"""
            score += 1 + 1 / ball_opisanye[i][3] * 100 + abs(ball_opisanye[i][5]) / 2
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
                """Начисление очков, число которых зависит от размера и скорости треугольника"""
                score += 1 + 100 / triangle_opisanye[i][2] + abs(triangle_opisanye[i][3]) / 3
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
    score = round(score)
    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()

""" Работа с текстовым файлом 'leaders.txt', являющемся таблицей лучших игроков

Просит ввести имя(без пробела) и сообщает информацию о вхождении в таблицу, указывая на существовании рекорда.

"""

name = input('Введите ваше имя')
inp = open('leaders.txt', 'r')
text = inp.read().split('\n')  # делит файл на элементы массива
tabl = [0] * len(text)  # объединяет в двумерный массив
for i in range(len(text)):
    tabl[i] = text[i].split('-')
schet = 0  # считает количество проверенных строк таблицы
for i in range(len(text)):
    if tabl[i][1] == name:  # случай, когда игрок уже есть в таблице
        print('Вы уже есть в списке')
        if int(tabl[i][0]) >= score:  # случай, когда игрок не побил свой рекорд
            print('Не расслабляйтесь,у вас есть более высокий результат')
            break
        else:  # случай, когда игрок не побил свой рекорд
            print('Отлично, вы побили свой рекорд!')
            z = tabl.pop(i)
            for j in range(len(text)):
                if int(tabl[j][0]) < score:
                    tabl.insert(j, [str(score), name])
                    break
    else:
        schet += 1
if schet == len(text):  # случай, когда игрока ещё нет в таблице
    schet = 0
    print('Вас ещё нет в списке')
    for j in range(len(text)):
        if int(tabl[j][0]) < score:
            tabl.insert(j, [str(score), name])
            break
        else:
            schet += 1
if schet == len(text):  # обратный перевод двумерного массива в текст
    tabl.append([str(score), name])
vivod1 = []
for i in range(len(tabl)):
    vivod1.append('-'.join(tabl[i]))
text2 = '\n'.join(vivod1)
inp.close()
out = open('leaders.txt', 'w')
out.write(text2)
out.close()
