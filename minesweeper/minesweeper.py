# coding=utf-8

# import pygame
import random
import os

# from pygame import mouse


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


'''
# button place and size
button_1_pos = ()
button_1_size = ()'''


def numbers_near_bombs(grid, diff):
    horizontal = 9
    vertical = 9
    if diff == 0:
        horizontal = 9
        vertical = 9
    elif diff == 1:
        horizontal = 29
        vertical = 19
    elif diff == 2:
        horizontal = 59
        vertical = 44

    r = c = 0
    for row in grid:
        for box in row:
            if r == 0:
                # only for first row
                if c == 0:
                    # if in first column
                    if box == 9:
                        if grid[r][c + 1] != 9:
                            grid[r][c + 1] += 1
                        if grid[r + 1][c + 1] != 9:
                            grid[r + 1][c + 1] += 1
                        if grid[r + 1][c] != 9:
                            grid[r + 1][c] += 1
                        c += 1
                    else:
                        c += 1
                elif c < horizontal:
                    if box == 9:
                        if grid[r][c + 1] != 9:
                            grid[r][c + 1] += 1
                        if grid[r][c - 1] != 9:
                            grid[r][c - 1] += 1
                        if grid[r + 1][c] != 9:
                            grid[r + 1][c] += 1
                        if grid[r + 1][c - 1] != 9:
                            grid[r + 1][c - 1] += 1
                        if grid[r + 1][c + 1] != 9:
                            grid[r + 1][c + 1] += 1
                        c += 1
                    else:
                        c += 1


                elif c == horizontal:
                    if box == 9:
                        if grid[r][c - 1] != 9:
                            grid[r][c - 1] += 1
                        if grid[r + 1][c - 1] != 9:
                            grid[r + 1][c - 1] += 1
                        if grid[r + 1][c] != 9:
                            grid[r + 1][c] += 1
                        c = 0
                        r += 1
                    else:
                        c = 0
                        r += 1
                else:
                    c = 0
                    r += 1
            elif r < vertical:
                if c == 0:
                    if box == 9:
                        if grid[r - 1][c] != 9:
                            grid[r - 1][c] += 1
                        if grid[r - 1][c + 1] != 9:
                            grid[r - 1][c + 1] += 1
                        if grid[r][c + 1] != 9:
                            grid[r][c + 1] += 1
                        if grid[r + 1][c] != 9:
                            grid[r + 1][c] += 1
                        if grid[r + 1][c + 1] != 9:
                            grid[r + 1][c + 1] += 1
                        c += 1
                    else:
                        c += 1

                elif c < horizontal:
                    if box == 9:
                        if grid[r - 1][c - 1] != 9:
                            grid[r - 1][c - 1] += 1
                        if grid[r - 1][c] != 9:
                            grid[r - 1][c] += 1
                        if grid[r - 1][c + 1] != 9:
                            grid[r - 1][c + 1] += 1
                        if grid[r][c - 1] != 9:
                            grid[r][c - 1] += 1
                        if grid[r][c + 1] != 9:
                            grid[r][c + 1] += 1
                        if grid[r + 1][c - 1] != 9:
                            grid[r + 1][c - 1] += 1
                        if grid[r + 1][c] != 9:
                            grid[r + 1][c] += 1
                        if grid[r + 1][c + 1] != 9:
                            grid[r + 1][c + 1] += 1
                        c += 1
                    else:
                        c += 1

                elif c == horizontal:
                    if box == 9:
                        if grid[r - 1][c] != 9:
                            grid[r - 1][c] += 1
                        if grid[r - 1][c - 1] != 9:
                            grid[r - 1][c - 1] += 1
                        if grid[r][c - 1] != 9:
                            grid[r][c - 1] += 1
                        if grid[r + 1][c] != 9:
                            grid[r + 1][c] += 1
                        if grid[r + 1][c - 1] != 9:
                            grid[r + 1][c - 1] += 1
                        c = 0
                        r += 1
                    else:
                        c = 0
                        r += 1
                else:
                    c = 0
                    r += 1
            elif r == vertical:
                if c == 0:
                    # if in first column
                    if box == 9:
                        if grid[r][c + 1] != 9:
                            grid[r][c + 1] += 1
                        if grid[r - 1][c + 1] != 9:
                            grid[r - 1][c + 1] += 1
                        if grid[r - 1][c] != 9:
                            grid[r - 1][c] += 1
                        c += 1
                    else:
                        c += 1

                elif c < horizontal:
                    if box == 9:
                        if grid[r][c + 1] != 9:
                            grid[r][c + 1] += 1
                        if grid[r][c - 1] != 9:
                            grid[r][c - 1] += 1
                        if grid[r - 1][c] != 9:
                            grid[r - 1][c] += 1
                        if grid[r - 1][c - 1] != 9:
                            grid[r - 1][c - 1] += 1
                        if grid[r - 1][c + 1] != 9:
                            grid[r - 1][c + 1] += 1
                        c += 1
                    else:
                        c += 1

                elif c == horizontal:
                    if box == 9:
                        if grid[r][c - 1] != 9:
                            grid[r][c - 1] += 1
                        if grid[r - 1][c - 1] != 9:
                            grid[r - 1][c - 1] += 1
                        if grid[r - 1][c] != 9:
                            grid[r - 1][c] += 1

                        c = 0
                        r += 1
                    else:
                        c = 0
                        r += 1
                else:
                    c = 0
                    r += 1
    return grid


def set_bombs(diff):

    if diff == 0:
        bombs_coords = [[0 for i in range(10)] for j in range(10)]
        for i in range(15):
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            bombs_coords[x][y] = 9

    elif diff == 1:
        bombs_coords = [[0 for i in range(20)] for j in range(30)]
        for i in range(31):
            x = random.randint(0, 29)
            y = random.randint(0, 19)
            bombs_coords[x][y] = 9

    elif diff == 2:
        bombs_coords = [[0 for i in range(45)] for j in range(60)]
        for i in range(91):
            x = random.randint(0, 59)
            y = random.randint(0, 44)
            bombs_coords[x][y] = 9
    return bombs_coords


'''
def check_if_bomb(x,y, bombs):
    1

def set_number_of_bombs(bombs):
    1
'''


bombs_grid = bombs = set_bombs(0)
print(len(bombs[0]))
print(len(bombs))
print(bombs)
k = m = 0
for i in bombs:
    for j in i:
        if j == 9:
            print(k, m, end="   ")
        m += 1
    print()
    m = 0
    k += 1
for i in bombs:
    print(i)
corrected = numbers_near_bombs(bombs_grid, 0)
print("\n\n\n")
for i in corrected:
    print(i)












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