import pygame
import random
import time


pygame.init()
display = pygame.display.set_mode((720, 720))
screen = pygame.image.load('8x8.png')
clock = pygame.time.Clock()
screen = pygame.transform.scale(screen, (720, 720))
black = (0, 0, 0)
pygame.display.set_caption('FIND-WAY!')
squares = [[x, y, 90, 90] for x in range(0, 720, 90) for y in range(0, 720, 90)]
font = pygame.font.SysFont('comicsansms', 30)
font2 = pygame.font.SysFont('arial', 60)
playing = True
clock = pygame.time.Clock()


def newgame():
    global occupied_squares
    display.fill((255, 255, 119))
    display.blit(font2.render('FIND-WAY', True, black), [190, 150])
    display.blit(font.render('Press q to quit', True, black), [170, 300])
    display.blit(font.render('Any other key to continue', True, black), [170, 340])
    display.blit(font.render('Press s in game to see solution', True, black), [170, 390])
    pygame.display.update()
    getting_event = True
    while getting_event:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                else:
                    getting_event = False
    display.fill((72, 4, 98))
    display.blit(screen, (0, 0))
    pygame.display.update()
    atleast = 1
    while atleast < 40:  # 15
        p_squares = random.randrange(50, 60)
        current_square = random.choice(squares)
        occupied_squares = []
        occupied_squares.append(current_square)
        while p_squares:
            adj_squares = [x for x in[
                [current_square[0] + 90, current_square[1], current_square[2], current_square[3]],
                [current_square[0], current_square[1] + 90, current_square[2], current_square[3]],
                [current_square[0] - 90, current_square[1], current_square[2], current_square[3]],
                [current_square[0], current_square[1] - 90, current_square[2], current_square[3]]
            ] if (x[0] >= 0 and x[1] >= 0 and x not in occupied_squares and x in squares)]
            try:
                current_square = random.choice(adj_squares)
                occupied_squares.append(current_square)
            except:
                p_squares = 1
            p_squares -= 1
        atleast = len(occupied_squares)
    for i in occupied_squares:
        pygame.draw.rect(display, (255, 0, 0), i)
    pygame.draw.rect(display, (255, 150, 0), occupied_squares[0])
    display.blit(screen, (0, 0))
    pygame.display.update()


def solution():
    display.fill((72, 4, 98))
    for i in occupied_squares:
        pygame.draw.rect(display, (255, 0, 0), i)
    display.blit(screen, (0, 0))
    pygame.display.update()
    for i in occupied_squares:
        clock.tick(5)
        pygame.draw.rect(display, (255, 150, 0), i)
        display.blit(screen, (0, 0))
        pygame.display.update()


while playing:
    newgame()
    game = True
    my_squares = [occupied_squares[0]]
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_s:
                    game = False
                    solution()

                elif event.key == pygame.K_r:
                    my_squares = [occupied_squares[0]]

                elif event.key == pygame.K_UP:
                    xyz = [my_squares[-1][0], my_squares[-1][1] - 90, my_squares[-1][2], my_squares[-1][3]]
                    if xyz in my_squares:
                        my_squares = my_squares[:my_squares.index(xyz) + 1]
                    elif xyz in occupied_squares:
                        my_squares.append(xyz)
                elif event.key == pygame.K_DOWN:
                    xyz = [my_squares[-1][0], my_squares[-1][1] + 90, my_squares[-1][2], my_squares[-1][3]]
                    if xyz in my_squares:
                        my_squares = my_squares[:my_squares.index(xyz) + 1]
                    elif xyz in occupied_squares:
                        my_squares.append(xyz)
                elif event.key == pygame.K_LEFT:
                    xyz = [my_squares[-1][0] - 90, my_squares[-1][1], my_squares[-1][2], my_squares[-1][3]]
                    if xyz in my_squares:
                        my_squares = my_squares[:my_squares.index(xyz) + 1]
                    elif xyz in occupied_squares:
                        my_squares.append(xyz)
                elif event.key == pygame.K_RIGHT:
                    xyz = [my_squares[-1][0] + 90, my_squares[-1][1], my_squares[-1][2], my_squares[-1][3]]
                    if xyz in my_squares:
                        my_squares = my_squares[:my_squares.index(xyz) + 1]
                    elif xyz in occupied_squares:
                        my_squares.append(xyz)
        for i in occupied_squares:
            pygame.draw.rect(display, (255, 0, 0), i)
        for z in my_squares:
            pygame.draw.rect(display, (255, 150, 0), z)
        display.blit(screen, (0, 0))
        pygame.display.update()
        if all(sqr in my_squares for sqr in occupied_squares):
            game = False
            display.fill((random.randrange(255), random.randrange(255), random.randrange(255)))
            display.blit(font2.render('YOU WIN.', True, black), [190, 300])
            pygame.display.update()
            won_play = True
            while won_play:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pygame.quit()
                            quit()
                        else:
                            won_play = False

pygame.quit()
