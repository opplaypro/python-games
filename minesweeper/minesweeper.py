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

for other things to fix look for comments with "TO_FIX"
'''

# function to choose difficulty level
# change input method to button on UI instead of text input #change0002
def choose_difficulty():
    while True:
        difficulty = input("Wybierz poziom trudności: ")
        if difficulty.lower() in ("łatwy", "0"):
            print("rozmiar to 10 x 10")
            return 0
        elif difficulty.lower() in ("średni", "1"):
            print("rozmiar to 20 x 30")
            return 1
        elif difficulty.lower() in ("trudny", "2"):
            print("rozmiar to 45 x 60")
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
                        c += 1
                    else:
                        c += 1


                elif c == horizontal:
                    if box == 9:

                        grid = change_numbers(grid, r, c - 1)
                        grid = change_numbers(grid, r + 1, c - 1)
                        grid = change_numbers(grid, r + 1, c)
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
                        c += 1
                    else:
                        c += 1

                elif c == horizontal:
                    if box == 9:

                        grid = change_numbers(grid, r - 1, c - 1)
                        grid = change_numbers(grid, r - 1, c)
                        grid = change_numbers(grid, r, c - 1)
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
            bombs_coords[y][x] = 9

    elif diff == 1:
        bombs_coords = [[0 for _ in range(30)] for _ in range(20)]
        for i in range(120):
            x = random.randint(0, 29)
            y = random.randint(0, 19)
            bombs_coords[y][x] = 9

    elif diff == 2:
        bombs_coords = [[0 for _ in range(60)] for _ in range(45)]
        for i in range(300):
            x = random.randint(0, 59)
            y = random.randint(0, 44)
            bombs_coords[y][x] = 9
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

    play = True
    max_x, max_y = [9, 29, 59][diff], [9, 19, 44][diff]
    if diff not in [0, 1, 2]:
        print("error")
        max_x = 9
        max_y = 9

    visible_grid = [["_" for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    print("Współrzędne miejsca wprowadzaj w formacie 'x, y'\n")
    visited_cells = []
    while play:
        guess = input("Wprowadź współrzędne: ").split(",")
        os.system('cls')
        if len(guess) == 2:
            try:
                y = int(guess[0]) - 1
                x = int(guess[1]) - 1
            except ValueError:
                print("BŁĄD, ZŁE WSPÓŁRZĘDNE")
                continue
            if 0 <= x <= max_x and 0 <= y <= max_y:
                visible_grid, play, visited_cells = uncover_cells(grid, visible_grid, diff, (int(x), int(y)), visited_cells)

            else:
                print("error, za dużo")

        else:
            print("error")
            continue


def show_cells_near(grid, visible_grid, diff, guess, visited_cells):

    x, y = guess
    if guess in visited_cells:
        return visible_grid

    visited_cells.append(guess)
    horizontal = [9, 29, 59][diff]
    vertical = [9, 19, 44][diff]


    cells_nearby = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    visible_grid[x][y] = str(grid[x][y])

    if grid[x][y] == 0:
        for dx, dy in cells_nearby:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < horizontal and 0 <= ny < vertical:
                if (nx, ny) not in visited_cells:
                    visible_grid, visited_cells = show_cells_near(grid, visible_grid, diff, (nx, ny), visited_cells)

    return visible_grid, visited_cells

'''
    if 0 <= nx < horizontal and 0 <= ny < vertical:
        if (nx, ny) not in visited_cells:
            visible_grid = show_cells_near(grid, visible_grid, diff, (nx, ny), visited_cells)'''



'''for dx, dy in cells_nearby:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < horizontal and 0 <= ny < vertical:
                if (nx, ny) not in visited_cells:
                    if grid[ny][nx] in [1, 2, 3, 4, 5, 6, 7, 8]:
                        visible_grid[ny][nx] = grid[ny][nx]
                    else:
                        visible_grid = show_cells_near(grid, visible_grid, diff, (nx, ny), visited_cells)
                        
                        
                        '''



''''
    #   CODE BELOW ENTERS RECURSIVE LOOP
    #   FIX THAT SHIT PLS
    #   TO_FIX
    visited_cells.append(guess)

    if x == 0:
        if y == 0:
            if grid[x][y] == 0:
                visible_grid = show_cells_near(grid, visible_grid, diff, (x, y + 1))
                visible_grid = show_cells_near(visible_grid, diff, (x + 1, y))
                visible_grid = show_cells_near(visible_grid, diff, (x + 1, y + 1))

        elif y < vertical:

            visible_grid = show_cells_near(visible_grid, diff, (x, y - 1))
            visible_grid = show_cells_near(visible_grid, diff, (x, y + 1))                visible_grid = show_cells_near(visible_grid, diff, (x + 1, y - 1))
            visible_grid = show_cells_near(visible_grid, diff, (x + 1, y))
            visible_grid = show_cells_near(visible_grid, diff, (x + 1, y + 1))
        elif y == vertical:

            visible_grid = show_cells_near(visible_grid, diff, (x, y - 1))
            visible_grid = show_cells_near(visible_grid, diff, (x + 1, y - 1))
            visible_grid = show_cells_near(visible_grid, diff, (x + 1, y))

    elif x < horizontal:
        if y == 0:

            visible_grid = show_cells_near(visible_grid, diff, (x - 1, y))
            visible_grid = show_cells_near(visible_grid, diff, (x - 1, y + 1))
            visible_grid = show_cells_near(visible_grid, diff, (x, y + 1))
            visible_grid = show_cells_near(visible_grid, diff, (x + 1, y))
            visible_grid = show_cells_near(visible_grid, diff, (x + 1, y + 1))

        elif y < vertical:

            visible_grid = show_cells_near(visible_grid, diff, (x - 1, y - 1))
            visible_grid = show_cells_near(visible_grid, diff, (x - 1, y + 1))
            visible_grid = show_cells_near(visible_grid, diff, (x - 1, y - 1))
            visible_grid = show_cells_near(visible_grid, diff, (x, y - 1))
            visible_grid = show_cells_near(visible_grid, diff, (x, y + 1))
            visible_grid = show_cells_near(visible_grid, diff, (x + 1, y - 1))
            visible_grid = show_cells_near(visible_grid, diff, (x + 1, y))
            visible_grid = show_cells_near(visible_grid, diff, (x + 1, y + 1))


        elif y == vertical:

            visible_grid = show_cells_near(visible_grid, diff, (x - 1, y - 1))
            visible_grid = show_cells_near(visible_grid, diff, (x - 1, y))
            visible_grid = show_cells_near(visible_grid, diff, (x, y - 1))
            visible_grid = show_cells_near(visible_grid, diff, (x + 1, y - 1))
            visible_grid = show_cells_near(visible_grid, diff, (x + 1, y))
    elif x == horizontal:
        if y == 0:

            visible_grid = show_cells_near(visible_grid, diff, (x - 1, y))
            visible_grid = show_cells_near(visible_grid, diff, (x - 1, y + 1))
            visible_grid = show_cells_near(visible_grid, diff, (x, y + 1))

        elif y < vertical:

            visible_grid = show_cells_near(visible_grid, diff, (x - 1, y - 1))
            visible_grid = show_cells_near(visible_grid, diff, (x - 1, y))
            visible_grid = show_cells_near(visible_grid, diff, (x - 1, y + 1))
            visible_grid = show_cells_near(visible_grid, diff, (x, y - 1))
            visible_grid = show_cells_near(visible_grid, diff, (x, y + 1))

        elif y == vertical:

            visible_grid = show_cells_near(visible_grid, diff, (x - 1, y - 1))
            visible_grid = show_cells_near(visible_grid, diff, (x - 1, y))
            visible_grid = show_cells_near(visible_grid, diff, (x, y - 1))
    visited_cells.append(guess)
'''


def uncover_cells(grid, visible_grid, diff, guess, visited_cells):
    x = guess[0]
    y = guess[1]
    if grid[x][y] == 9:
        print("Bomba\nPrezgrałeś")
        play = False

    else:
        visible_grid, visited_cells = show_cells_near(grid, visible_grid, diff, guess, visited_cells)
        play = True

    for row in visible_grid:
        print(row)

    return visible_grid, play, visited_cells


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


#   below is pygame part of the code
#   (at least I want to add it)

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