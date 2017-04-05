import pygame
import os
from get_image import *
from pygame.locals import *
from board import *
from matrix import *
screen = pygame.display.set_mode((w_size, h_size), DOUBLEBUF)
screen.fill(black_color)
draw_first_board(screen)

matrix       = [[None] * 4] * 4
matrix_down  = [[None] * 4] * 4
matrix_up    = [[None] * 4] * 4
matrix_left  = [[None] * 4] * 4
matrix_right = [[None] * 4] * 4

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

running = True
game_on = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    while game_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
	    		running = False
	    		game_on = False
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

            put_images(matrix, screen)

            pygame.display.flip()
pygame.quit()
