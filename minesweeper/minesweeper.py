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
        difficulty = input("Wybierz poziom trudności: ")
        if difficulty.lower() in ("łatwy", "0"):
            return 0
        elif difficulty.lower() in ("średni", "1"):
            return 1
        elif difficulty.lower() in ("trudny", "2"):
            return 2
        elif difficulty == "KONIEC":
            break
        else:
            print("Wrong input! Try again")
            continue


'''
# button place and size
button_1_pos = ()
button_1_size = ()'''


def change_numbers(grid, x, y):
    if grid[x][y] != 9:
        grid[x][y] += 1
    return grid


#   funcion sets every position to number of bombs near
def numbers_near_bombs(grid, diff):

    #   IT WORKS !!! BEFORE CHANGING TEST IF IT WORKS THE SAME
    #   GRID = [[]]

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

                        grid = change_numbers(grid, r, c + 1)
                        grid = change_numbers(grid, r + 1, c + 1)
                        grid = change_numbers(grid, r + 1, c)
                        '''
                        if grid[r][c + 1] != 9:
                            grid[r][c + 1] += 1

                        if grid[r + 1][c + 1] != 9:
                            grid[r + 1][c + 1] += 1

                        if grid[r + 1][c] != 9:
                            grid[r + 1][c] += 1
                        '''

                        c += 1
                    else:
                        c += 1
                elif c < horizontal:
                    if box == 9:

                        grid = change_numbers(grid, r, c + 1)
                        grid = change_numbers(grid, r, c - 1)
                        grid = change_numbers(grid, r + 1, c - 1)
                        grid = change_numbers(grid, r + 1, c)
                        grid = change_numbers(grid, r + 1, c + 1)
                        '''
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
                        '''
                        c += 1
                    else:
                        c += 1


                elif c == horizontal:
                    if box == 9:

                        grid = change_numbers(grid, r, c - 1)
                        grid = change_numbers(grid, r + 1, c - 1)
                        grid = change_numbers(grid, r + 1, c)
                        '''
                        if grid[r][c - 1] != 9:
                            grid[r][c - 1] += 1

                        if grid[r + 1][c - 1] != 9:
                            grid[r + 1][c - 1] += 1

                        if grid[r + 1][c] != 9:
                            grid[r + 1][c] += 1
                        '''
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

                        grid = change_numbers(grid, r - 1, c)
                        grid = change_numbers(grid, r - 1, c + 1)
                        grid = change_numbers(grid, r, c + 1)
                        grid = change_numbers(grid, r + 1, c)
                        grid = change_numbers(grid, r + 1, c + 1)

                        '''
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
                        '''
                        c += 1
                    else:
                        c += 1

                elif c < horizontal:
                    if box == 9:

                        grid = change_numbers(grid, r - 1, c - 1)
                        grid = change_numbers(grid, r - 1, c)
                        grid = change_numbers(grid, r - 1, c + 1)
                        grid = change_numbers(grid, r, c - 1)
                        grid = change_numbers(grid, r, c + 1)
                        grid = change_numbers(grid, r + 1, c - 1)
                        grid = change_numbers(grid, r + 1, c)
                        grid = change_numbers(grid, r + 1, c + 1)


                        '''
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
                            '''

                        c += 1
                    else:
                        c += 1

                elif c == horizontal:
                    if box == 9:

                        grid = change_numbers(grid, r - 1, c - 1)
                        grid = change_numbers(grid, r - 1, c)
                        grid = change_numbers(grid, r, c - 1)
                        grid = change_numbers(grid, r + 1, c - 1)
                        grid = change_numbers(grid, r + 1, c)

                        '''
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
                        '''
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

                        grid = change_numbers(grid, r - 1, c)
                        grid = change_numbers(grid, r - 1, c + 1)
                        grid = change_numbers(grid, r, c + 1)

                        '''
                        if grid[r][c + 1] != 9:
                            grid[r][c + 1] += 1

                        if grid[r - 1][c + 1] != 9:
                            grid[r - 1][c + 1] += 1

                        if grid[r - 1][c] != 9:
                            grid[r - 1][c] += 1
                        '''
                        c += 1
                    else:
                        c += 1

                elif c < horizontal:
                    if box == 9:

                        grid = change_numbers(grid, r - 1, c - 1)
                        grid = change_numbers(grid, r - 1, c)
                        grid = change_numbers(grid, r - 1, c + 1)
                        grid = change_numbers(grid, r, c - 1)
                        grid = change_numbers(grid, r, c + 1)

                        '''
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
                        '''
                        c += 1
                    else:
                        c += 1

                elif c == horizontal:
                    if box == 9:

                        grid = change_numbers(grid, r - 1, c - 1)
                        grid = change_numbers(grid, r - 1, c)
                        grid = change_numbers(grid, r, c - 1)


                        '''
                        if grid[r][c - 1] != 9:
                            grid[r][c - 1] += 1

                        if grid[r - 1][c - 1] != 9:
                            grid[r - 1][c - 1] += 1

                        if grid[r - 1][c] != 9:
                            grid[r - 1][c] += 1
                        '''
                        c = 0
                        r += 1
                    else:
                        c = 0
                        r += 1
                else:
                    c = 0
                    r += 1
    return grid


# sets grid size and places bombs depending on difficulty
# easy = 0 , medium = 1 , hard = 2
def set_bombs(diff):
    bombs_coords = []
    if diff == 0:
        bombs_coords = [[0 for _ in range(10)] for _ in range(10)]
        for i in range(15):
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            bombs_coords[x][y] = 9

    elif diff == 1:
        bombs_coords = [[0 for _ in range(20)] for _ in range(30)]
        for i in range(31):
            x = random.randint(0, 29)
            y = random.randint(0, 19)
            bombs_coords[x][y] = 9

    elif diff == 2:
        bombs_coords = [[0 for _ in range(45)] for _ in range(60)]
        for i in range(91):
            x = random.randint(0, 59)
            y = random.randint(0, 44)
            bombs_coords[x][y] = 9
    return bombs_coords



# test if everything works !!! TERMINAL ONLY!!! NO PYGAME
def test_script():
    player_guess(
        [[0 for _ in range(10)] for _ in range(10)],0)
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


def player_guess(grid, diff):
    visible_grid = []
    play = True
    if diff == 0:
        max_x = 9
        max_y = 9
    elif diff == 1:
        max_x = 29
        max_y = 19
    elif diff == 2:
        max_x = 59
        max_y = 44
    print("Współrzędne miejsca wprowadzaj w formacie 'x, y'\n")
    while play:
        guess = input("Wprowadź współrzędne: ").split(",")
        if len(guess) == 2:
            try:
                x = int(guess[0])
                y = int(guess[1])
            except ValueError:
                print("BŁĄD, ZŁE WSPÓŁRZĘDNE")
                continue
            if 0 <= x <= max_x and 0 <= y <= max_y:
                visible_grid = uncover_cells(grid, visible_grid, diff, (int(x), int(y)))
            else:
                print("error, za dużo")
        else:
            print("error")
            continue




def uncover_cells(grid, visible_grid, diff, guess):
    x = guess[0]
    y = guess[1]
    if grid[x][y] == 9:
        print("Bomba\nPrezgrałeś")
    else:
        visible_grid = (grid, visible_grid, diff, (x - 1, y - 1))
        visible_grid = (grid, visible_grid, diff, (x - 1, y))
        visible_grid = (grid, visible_grid, diff, (x - 1, y + 1))
        visible_grid = (grid, visible_grid, diff, (x, y - 1))
        visible_grid = (grid, visible_grid, diff, (x, y + 1))
        visible_grid = (grid, visible_grid, diff, (x + 1, y - 1))
        visible_grid = (grid, visible_grid, diff, (x + 1, y))
        visible_grid = (grid, visible_grid, diff, (x + 1, y + 1))
        return visible_grid
        pass


def first_interaction():
    print("Witaj w grze Saper!\nJeśli pojawią się błędy, zgłoś proszę!")

def game():
    first_interaction()
    diff = choose_difficulty()
    bomb_grid = set_bombs(diff)
    bomb_grid = numbers_near_bombs(bomb_grid, diff)
    player_guess(bomb_grid, diff)


TESTS = 0


if __name__ == "__main__":
    if TESTS:
        test_script()
    else:
        game()




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