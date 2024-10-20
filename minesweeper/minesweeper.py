﻿# coding=utf-8

import pygame
# import random
import os

os.system('cls')

'''
changes to make (find with ctr+f):
format: change0001

change0001: change frame rate to 60
change0002: change input method
'''


# function to choose difficulty level
# change input method to button on UI instead of text input #change0002
def choose_difficulty():
    while True:
        difficulty = input("Choose diff")
        if difficulty == "easy":
            return 10, 10
        elif difficulty == "medium":
            return 30, 20
        elif difficulty == "hard":
            return 60, 45
        else:
            print("Wrong input! Try again")
            continue





WIDTH = 1280
HEIGHT = 720

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        print(event)

    pygame.display.update()
    clock.tick(12)  #change later to 60 (12 is more visible in terminal) find with change0001
pygame.quit()