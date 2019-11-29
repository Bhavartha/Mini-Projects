import pygame
import random
import time


pygame.init()
black = (0, 0, 0)
red = (255, 0, 0)
green = (152, 180, 61)
screen_color = (255, 255, 119)
display_width, display_height = 1080, 720
size_snake = 20
apple_size = 15
display = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
img = pygame.image.load('snake-head.png')
img = pygame.transform.scale(img, (size_snake, size_snake))
icon = pygame.image.load('logo.png')
icon = pygame.transform.scale(icon, (32, 32))

pygame.display.set_caption('Snake !')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
font = pygame.font.SysFont('comicsansms', 45)
h_font = pygame.font.SysFont('arial', 60)


def snake(size_snake, snakelist):
    if direction == 'right':
        head = pygame.transform.rotate(img, 270)
    elif direction == 'left':
        head = pygame.transform.rotate(img, 90)
    elif direction == 'south':
        head = pygame.transform.rotate(img, 180)
    elif direction == 'north':
        head = pygame.transform.rotate(img, 0)
    display.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    for xy in snakelist[:-1]:
        pygame.draw.rect(display, green, [xy[0], xy[1], size_snake, size_snake])


def pause():
    paused = True
    display.fill(background)
    message("GAME PAUSED", black, -100)
    message("Press P to Resume", black, 100, 35)
    message("Press Q to quit", black, 140, 35)
    pygame.display.update()
    while paused:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_p:
                    paused = False
        clock.tick(5)


def message(msg, color, y_displace=0, font=60):
    h_font = pygame.font.SysFont('arial', font)
    text2print = h_font.render(msg, True, color)
    text_rect = text2print.get_rect()
    text_rect.center = (display_width / 2), (display_height / 2) + y_displace
    display.blit(text2print, text_rect)


def reset():

    global fps_inc, FPS, option, pos_yc, background, pos_xc, gameover, applex, appley, pos_x, pos_y, snakelen, snakelist, crashed
    FPS = 15
    snakelist = []
    snakelen = 2
    fps_inc = 7
    crashed = False
    gameover = False
    applex = random.randrange(0, display_width - size_snake, apple_size)
    appley = random.randrange(0, display_height - size_snake, apple_size)
    pos_xc = 20
    pos_yc = 0
    pos_x = display_width / 2
    pos_y = display_height / 2
    background = (random.randint(155, 255), random.randint(155, 255), random.randint(155, 255))
    option = True


def startscreen():
    display.fill(background)
    display.blit(h_font.render('SNAKE', True, black), [380, 150])
    display.blit(font.render('1: No boundaries', True, black), [370, 300])
    display.blit(font.render('2: Boundaries', True, black), [370, 340])
    message("Press P to Pause/Resume", black, 170, 35)
    message("Press Q to quit", black, 210, 35)
    pygame.display.update()


while True:
    reset()
    direction = 'right'
    startscreen()

    while option:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    no_boun = True
                    option = False
                elif event.key == pygame.K_2:
                    option = False
                    no_boun = False
                if event.key == pygame.K_p:
                    pause()
                    startscreen()

                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        # pygame.display.update()
    reset()
    while not crashed:
        while gameover:
            display.fill(background)
            # display.blit(h_font.render('You Lose', True, black), [380, 200])
            # display.blit(font.render('C to continue', True, black), [370, 350])
            # display.blit(font.render('Q to quit', True, black), [370, 390])
            # display.blit(font.render(f'Score: {(snakelen-2)*10}', True, red), [400, 120])
            message(f'Score: {(snakelen-2)*10}', red, -200)
            message("You lose.", black, -50)
            message("C to continue", black, 50, 40)
            message("Q to quit", black, 100, 40)

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_c:
                        crashed = True
                        gameover = False
                    elif event.key == pygame.K_p:
                        pause()
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and pos_yc:
                    pos_xc = -size_snake
                    pos_yc = 0
                    direction = 'left'
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and pos_yc:
                    pos_xc = size_snake
                    pos_yc = 0
                    direction = 'right'
                elif (event.key == pygame.K_UP or event.key == pygame.K_w) and pos_xc:
                    pos_yc = -size_snake
                    pos_xc = 0
                    direction = 'north'
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and pos_xc:
                    pos_yc = size_snake
                    pos_xc = 0
                    direction = 'south'
                elif event.key == pygame.K_p:
                    pause()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        if no_boun:
            pos_y = (pos_yc + pos_y) % display_height
            pos_x = (pos_xc + pos_x) % display_width
        else:
            pos_y += pos_yc
            pos_x += pos_xc
            if pos_x < 0 or pos_x >= display_width or pos_y < 0 or pos_y >= display_height:
                gameover = True

        display.fill(screen_color)
        pygame.draw.rect(display, red, [applex, appley, apple_size, apple_size])
        display.blit(font.render(f'Score:{(snakelen-2)*10}', True, black), [0, 0])

        snakelist.append([pos_x, pos_y])
        if len(snakelist) > snakelen:
            del snakelist[0]
        for each in snakelist[:-1]:
            if each == [pos_x, pos_y]:
                gameover = True
        snake(size_snake, snakelist)
        pygame.display.update()
        if (applex + apple_size >= pos_x >= applex or applex <= pos_x + size_snake <= applex + apple_size) and (appley + apple_size >= pos_y >= appley or appley <= pos_y + size_snake <= appley + apple_size):
            applex = random.randrange(0, display_width - apple_size, apple_size)
            appley = random.randrange(0, display_height - apple_size, apple_size)
            snakelen += 1
        if snakelen > fps_inc:
            FPS+=5
            fps_inc+=7
        clock.tick(FPS)

pygame.quit()
quit()
