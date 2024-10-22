# coding=utf-8

import pygame
import random
import os

from pygame import mouse



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

# button place and size
button_1_pos = ()
button_1_size = ()

def set_bombs(diff):

    if diff == 0:
        bombs_coords = [["0" for i in range(10)] for j in range(10)]
        for i in range(15):
            x = random.randint(0,9)
            y = random.randint(0,9)
            bombs_coords[x][y] = "9"


    if diff == 1:
        bombs_coords = [["0" for i in range(20)] for j in range(30)]
        for i in range(30):
            x = random.randint(0,29)
            y = random.randint(0,19)
            bombs_coords[x][y] = "9"


    if diff == 2:
        bombs_coords = [["0" for i in range(45)] for j in range(60)]
        for i in range(90):
            x = random.randint(0,59)
            y = random.randint(0,44)
            bombs_coords[x][y] = "9"
    return bombs_coords


def check_if_bomb(x,y, bombs):
    1

def set_number_of_bombs(bombs):
    1

bombs = set_bombs(2)
print(len(bombs[0]))
print(len(bombs))
print(bombs)





'''
WIDTH = 800
HEIGHT = 480

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")
clock = pygame.time.Clock()
running = True
width = screen.get_width()
height = screen.get_height()
while running:

    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        print(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            check_if_bomb(mouse[0],mouse[1])





    clock.tick(10)  #change later to 60 (10 is more visible in terminal) find with change0001
pygame.quit()
'''