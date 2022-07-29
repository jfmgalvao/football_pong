from os.path import join

import pygame

from src import ASSETS_PATH, SCORE_PATH

pygame.init()

window = pygame.display.set_mode([1280, 720])
title = pygame.display.set_caption('Football Pong')

win = pygame.image.load(join(ASSETS_PATH, 'win.png'))

score1 = 0
score1_img = pygame.image.load(join(SCORE_PATH, '0.png'))
score2 = 0
score2_img = pygame.image.load(join(SCORE_PATH, '0.png'))

ball = pygame.image.load(join(ASSETS_PATH, 'ball.png'))
ball_x = 617
ball_y = 290
ball_dir = 2
ball_dir_y = 1

field = pygame.image.load(join(ASSETS_PATH, 'field.png'))
player1 = pygame.image.load(join(ASSETS_PATH, 'player1.png'))
player1_y = 290
player1_move_up = False
player1_move_down = False

player2 = pygame.image.load(join(ASSETS_PATH, 'player2.png'))
player2_y = 290


def move_player1():
    global player1_y

    if player1_move_up:
        if player1_y != 0:
            player1_y -= 5
    else:
        player1_y += 0

    if player1_move_down:
        if player1_y != 575:
            player1_y += 5
    else:
        player1_y += 0


def move_ball():
    global ball_x
    global ball_y
    global ball_dir
    global ball_dir_y
    global score1
    global score2
    global score1_img
    global score2_img

    ball_x += ball_dir
    ball_y += ball_dir_y

    if ball_x < 120:
        if player1_y < ball_y + 23:
            if player1_y + 146 > ball_y:
                ball_dir *= -1
    if ball_x > 1100:
        if player2_y < ball_y + 23:
            if player2_y + 146 > ball_y:
                ball_dir *= -1

    if ball_y > 685:
        ball_dir_y *= -1
    elif ball_y <= 0:
        ball_dir_y *= -1

    if ball_x < -50:
        ball_x = 617
        ball_y = 337
        ball_dir_y *= -1
        ball_dir *= -1
        score2 += 1
        score2_img = pygame.image.load(join(SCORE_PATH, f'{score2}.png'))
    elif ball_x > 1320:
        ball_x = 617
        ball_y = 337
        ball_dir_y *= -1
        ball_dir *= -1
        score1 += 1
        score1_img = pygame.image.load(join(SCORE_PATH, f'{score1}.png'))


def move_player2():
    global player2_y

    player2_y = ball_y


def draw():
    if score1 or score2 < 9:
        window.blit(field, (0, 0))
        window.blit(player1, (50, player1_y))
        window.blit(player2, (1150, player2_y))
        window.blit(ball, (ball_x, ball_y))
        window.blit(score1_img, (500, 50))
        window.blit(score2_img, (710, 50))

        move_ball()
        move_player1()
        move_player2()
    else:
        window.blit(win, (300, 330))


loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1_move_up = True
            if event.key == pygame.K_s:
                player1_move_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player1_move_up = False
            if event.key == pygame.K_s:
                player1_move_down = False

    draw()
    pygame.display.update()
