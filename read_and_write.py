import os
import pygame

def read_score(score):
	file = open('score.txt', 'r')
	
	for line in file:
		max_score=int(line)
    
	file.close()
	return max_score

def write(score):
	file = open('score.txt', 'w')

	file.write(str(score))

	file.close()

