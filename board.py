import pygame
import os
from colors import *
from get_image import *
def draw_first_board(screen):
    # Vertical lines
    pygame.draw.rect(screen,grey_color,(0,100,5,425))
    pygame.draw.rect(screen,grey_color,(105,100,5,425))
    pygame.draw.rect(screen,grey_color,(210,100,5,425))
    pygame.draw.rect(screen,grey_color,(315,100,5,425))
    pygame.draw.rect(screen,grey_color,(420,100,5,425))

    # Horizontal lines
    pygame.draw.rect(screen,grey_color,(0,95,425,5))
    pygame.draw.rect(screen,grey_color,(0,200,425,5))
    pygame.draw.rect(screen,grey_color,(0,305,425,5))
    pygame.draw.rect(screen,grey_color,(0,410,425,5))
    pygame.draw.rect(screen,grey_color,(0,515,425,5))

def put_images(matrix, screen):
    for i in range(0,4):
        for j in range(0,4):
            if matrix[i][j] != 0:
                path = './src/images/image_'
                path = path + str(matrix[i][j])+ '.png'
                screen.blit(get_image(path), (5 + 105 * j, 100 + 105 * i))
