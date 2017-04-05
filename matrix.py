import pygame
import os
from random import randint

def zeroes(matrix):
    matrix = [[0, 0 ,0, 0], [0, 0 ,0, 0], [0, 0 ,0, 0], [0, 0 ,0, 0]]
    return matrix

def initialize(matrix):
    rnd_i = randint(0,3)
    rnd_j = randint(0,3)

    for i in range(0,2):
        while matrix[rnd_i][rnd_j] != 0:
            rnd_i = randint(0,3)
            rnd_j = randint(0,3)

        percent = randint(0,99)
        number = 2

        if percent > 90:
            number = 4

        matrix[rnd_i][rnd_j] = number
    return matrix

def check_if_exists(matrix):
    ok = 0
    for i in range(0,4):
        for j in range(0,4):
            if matrix[i][j] == 0:
                ok = 1
    return ok

def add_random_number(matrix):
    rnd_i = randint(0,3)
    rnd_j = randint(0,3)

    while matrix[rnd_i][rnd_j] != 0:
        rnd_i = randint(0,3)
        rnd_j = randint(0,3)

    percent = randint(0,99)
    number = 2

    if percent > 90:
        number = 4

    matrix[rnd_i][rnd_j] = number

    return matrix

def move_up(matrix):
    k = 0
    for j in range(0,4):
		for i in range(1,4):
			if(matrix[i][j] != 0):
				k = i
				while (k > 0) & (matrix[k - 1][j] == 0):
					matrix[k - 1][j] = matrix[k][j]
					matrix[k][j] = 0
					k = k - 1

    for j in range(0, 4):
        for i in range(0, 3):
            if(matrix[i][j] != 0) & (matrix[i][j] == matrix[i + 1][j]):
                matrix[i][j] *= 2
                matrix[i + 1][j] = 0
                for k in range(i + 2, 4):
                    matrix[k - 1][j] = matrix[k][j]
                    matrix[k][j] = 0

    return matrix

def move_down_retarded_mode(matrix):
	for j in range(0,4):
		for i in range(2, -1, -1):
			if matrix[i][j] != 0:
			    k = i;
			    while (k < 3):
					if(matrix[k + 1][j] == 0):
					    matrix[k + 1][j] = matrix[k][j]
					    matrix[k][j] = 0
					k = k + 1

	for j in range(0,4):
		for i in range(3, 0, -1):
			if(matrix[i][j] != 0) & (matrix[i][j] == matrix[i - 1][j]):
			    matrix[i][j] *= 2
			    matrix[i - 1][j] = 0
			    for k in range(i - 2, -1, -1):
					matrix[k + 1][j] = matrix[k][j]
					matrix[k][j] = 0

	return matrix

def rotate_clockwise(matrix):
    rotate = [[None] * 4] * 4
    rotate = zeroes(rotate)
    for i in range(0,4):
        for j in range(0,4):
            rotate[i][j] = matrix[4 - j - 1][i]
    return rotate

def move_down(matrix):
    matrix = rotate_clockwise(matrix)
    matrix = rotate_clockwise(matrix)
    matrix = move_up(matrix)
    matrix = rotate_clockwise(matrix)
    matrix = rotate_clockwise(matrix)
    return matrix

def move_right(matrix):
    matrix = rotate_clockwise(matrix)
    matrix = rotate_clockwise(matrix)
    matrix = rotate_clockwise(matrix)
    matrix = move_up(matrix)
    matrix = rotate_clockwise(matrix)
    return matrix

def move_left(matrix):
    matrix = rotate_clockwise(matrix)
    matrix = move_up(matrix)
    matrix = rotate_clockwise(matrix)
    matrix = rotate_clockwise(matrix)
    matrix = rotate_clockwise(matrix)
    return matrix

def copy(matrix_copy, matrix):
    for i in range(0,4):
        for j in range(0,4):
            matrix_copy[i][j] = matrix[i][j]
    return matrix_copy

def check_eq(matrix1, matrix2):
    for i in range(0,4):
        for j in range(0,4):
            if matrix1[i][j] != matrix2[i][j]:
                return 0
    return 1

def check_end(matrix1, matrix2, matrix3, matrix4):
    ok1 = check_eq(matrix1, matrix2)
    ok2 = check_eq(matrix2, matrix3)
    ok3 = check_eq(matrix3, matrix4)

    return ok1 * ok2 * ok3
