import pygame
import os
pygame.init()
from get_image import *
from pygame.locals import *
from board import *
from matrix import *
from read_and_write import *

max_score = 0
max_score = read_score(max_score)

pygame.display.set_caption("2048")

screen = pygame.display.set_mode((w_size, h_size), DOUBLEBUF)
screen.fill(black_color)
draw_first_board(screen)

matrix       = [[None] * 4] * 4
matrix_down  = [[None] * 4] * 4
matrix_up    = [[None] * 4] * 4
matrix_left  = [[None] * 4] * 4
matrix_right = [[None] * 4] * 4

running = True
reset = True

# While game is running
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        if(x >= 25) & (x < 25 + 100) & (y >= 25) & (y < 25 + 26):
            game_on = False
            reset = True

    if reset == True:
# Reset
        matrix = zeroes(matrix)
        matrix_up = zeroes(matrix_up)
        matrix_down = zeroes(matrix_down)
        matrix_right = zeroes(matrix_right)
        matrix_left = zeroes(matrix_left)

        matrix = initialize(matrix)

        matrix_up = copy(matrix_up, matrix)
        matrix_down = copy(matrix_down, matrix)
        matrix_left = copy(matrix_left, matrix)
        matrix_right = copy(matrix_right, matrix)

        matrix_up = move_up(matrix_up)
        matrix_down = move_down(matrix_down)
        matrix_right = move_right(matrix_right)
        matrix_left = move_left(matrix_left)
        screen.fill(black_color)
        draw_first_board(screen)
        put_images(matrix, screen)

        game_on = True
        reset = False

    # Game is on
    while game_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
	    		running = False
	    		game_on = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if(x >= 25) & (x < 25 + 100) & (y >= 25) & (y < 25 + 26):
                    game_on = False
                    reset = True

            if event.type == KEYDOWN:
                screen.fill(black_color)
                draw_first_board(screen)

                if event.key == K_UP:
                    if check_eq(matrix, matrix_up) == 0:
                        matrix = move_up(matrix)
                        matrix = add_random_number(matrix)

                if event.key == K_DOWN:
                    if check_eq(matrix, matrix_down) == 0:
                        matrix = move_down(matrix)
                        matrix = add_random_number(matrix)

                if event.key == K_LEFT:
                    if check_eq(matrix, matrix_left) == 0:
                        matrix = move_left(matrix)
                        matrix = add_random_number(matrix)

                if event.key == K_RIGHT:
                    if check_eq(matrix, matrix_right) == 0:
                        matrix = move_right(matrix)
                        matrix = add_random_number(matrix)

                matrix_up = copy(matrix_up, matrix)
                matrix_down = copy(matrix_down, matrix)
                matrix_right = copy(matrix_right, matrix)
                matrix_left = copy(matrix_left, matrix)

                matrix_up = move_up(matrix_up)
                matrix_down = move_down(matrix_down)
                matrix_right = move_right(matrix_right)
                matrix_left = move_left(matrix_left)

                if check_end(matrix_up, matrix_down, matrix_left, matrix_right) == 1:
                    game_on = False
                    score = sum(matrix)
                    label_score = score_font.render("SCORE:    " + str(score), 1, red_color)
                    screen.blit(label_score, (170, 27))

                    if score > max_score:
                        write(score)
                        max_score = score
                        label_score_max = score_font.render("NEW RECORD:  " + str(max_score), 1, yellow_color)
                        screen.blit(label_score_max, (170, 57))
                    else:
                        label_score_max = score_font.render("RECORD:  " + str(max_score), 1, blue_color)
                        screen.blit(label_score_max, (170, 57))
                
            if game_on == True:
                score = sum(matrix)

                label_score = score_font.render("SCORE:     " + str(score), 1, yellow_color)
                screen.blit(label_score, (170, 27))

                label_score_max = score_font.render("RECORD:  " + str(max_score), 1, blue_color)
                screen.blit(label_score_max, (170, 57)) 

            put_images(matrix, screen)

            pygame.display.flip()
pygame.quit()
