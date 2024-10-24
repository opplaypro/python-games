# coding=utf-8


import random
import os
import time


os.system('cls')


# function to choose difficulty level

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


def change_numbers(grid, x, y):
    if grid[x][y] != 9:
        grid[x][y] += 1
    return grid


#   funcion sets every position to number of bombs near
#   rewrite using less code if possible #createdby:opplaypro
def numbers_near_bombs(grid, diff):
    #   IT WORKS !!! BEFORE CHANGING TEST IF IT WORKS THE SAME
    #   GRID = [[]]
    horizontal, vertical = [9, 29, 59][ diff], [9, 19, 44][ diff]
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


def print_grid(grid, diff):
    k = 1
    if diff == 0:
        print("\t", end="   ")
        for i in range(0, 10):
            print(i + 1, end="    ")
        print()
        for row in grid:
            print(f"{k}\t {row}")
            k += 1
    if diff == 1:
        print("\t", end="   ")
        for i in range(0, 9):
            print(i + 1, end="    ")
        for i in range(0, 21):
            print(i + 10, end="   ")
        print()
        for row in grid:
            print(f"{k}\t {row}")
            k += 1
    if diff == 2:
        print("\t", end="   ")
        for i in range(10):
            print(i + 1, end="    ")
        for i in range(50):
            print(i + 11, end="   ")
        print()
        for row in grid:
            print(f"{k}\t {row}")
            k += 1


def player_guess(grid, diff):
    play = True
    max_y, max_x = [9, 29, 59][diff], [9, 19, 44][diff]

    visible_grid = [["_" for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    print("Współrzędne miejsca wprowadzaj w formacie 'x, y'\nOznaczona bomba ma symbol 'F'")

    for k in range(4):
        time.sleep(0.1 * random.randint(3, 7))
        print("Trwa Ładowanie", k+1, "/10")
    print("Jeżeli wybrałeś poziom trudności średni albo trudny, musisz zmienić rozmier okna i rozmier czcionki (ctrl + scroll)")

    for k in range(6):
        time.sleep(0.1 * random.randint(3, 7))
        print("Trwa Ładowanie", k+5, "/10")

    os.system('cls')
    visited_cells = []
    print_grid(visible_grid, diff)

    while play:
        guess = input("Aby odgadnąć komórkę, wprowadź współrzędne 'x,y'\nJeżeli chcesz oznaczyć bombę, wpisz 'x,y,B'"
                      "\nJeśli uważasz, że oznaczyłeś wszystkie bomby, wpisz 'koniec': ").split(",")
        os.system('cls')

        if len(guess) == 2:
            try:
                y = int(guess[0]) - 1
                x = int(guess[1]) - 1
            except ValueError:
                print("BŁĄD, ZŁE WSPÓŁRZĘDNE")
                continue
            if (x, y) in visited_cells:
                if 0 <= x <= max_x and 0 <= y <= max_y:
                    print("Ta komórka jest już odkryta")
                    print_grid(visible_grid, diff)
                else:
                    print("error, za dużo")
            elif visible_grid[x][y] == "F":
                if 0 <= x <= max_x and 0 <= y <= max_y:
                    print("Ta komórka została oflagowana, nie możesz jest teraz odkryć")
                    print_grid(visible_grid, diff)
                else:
                    print("error, za dużo")
            else:
                if 0 <= x <= max_x and 0 <= y <= max_y:
                    visible_grid, play, visited_cells = uncover_cells(grid, visible_grid, diff, (int(x), int(y)), visited_cells)
                else:
                    print("error, za dużo")
        elif len(guess) == 3:
            try:
                y = int(guess[0]) - 1
                x = int(guess[1]) - 1
            except ValueError:
                print("BŁĄD, ZŁE WSPÓŁRZĘDNE")
                continue
            if guess[2].lower() == "b" or "b\n":
                if visible_grid[x][y] == "F":
                    visible_grid[x][y] = "_"
                elif visible_grid[x][y] == "_":
                    visible_grid[x][y] = "F"
                else:
                    print("error, nie ustawiono flagi")
            else:
                print("error, nie ustawiono flagi")
            print_grid(visible_grid, diff)
        elif guess[0].lower() == "koniec":
            r = 0
            c = 0
            for q in grid:
                for w in q:
                    if w == 9:
                        if visible_grid[r][c] == "F":
                            continue
                        else:
                            print("źle")
                            play = False
                    r += 1
                r = 0
                c += 1

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
            if 0 <= nx <= horizontal and 0 <= ny <= vertical:
                if (nx, ny) not in visited_cells:
                    visible_grid, visited_cells = show_cells_near(grid, visible_grid, diff, (nx, ny), visited_cells)

    return visible_grid, visited_cells


def uncover_cells(grid, visible_grid, diff, guess, visited_cells):
    play = True
    x = guess[0]
    y = guess[1]
    if grid[x][y] == 9:
        print("Bomba\nPrezgrałeś")
        play = False
        time.sleep(5)
        visible_grid[x][y] = "B"
    elif grid[x][y] == "F":
        print("Ta komórka została oznaczona jako bomba, nie możesz jej teraz odkryć")
        play = True
    else:
        if 0 <= x <= [9, 29, 59][diff] and 0 <= y <= [9, 19, 44][diff]:
            visible_grid, visited_cells = show_cells_near(grid, visible_grid, diff, guess, visited_cells)
            play = True

    print_grid(visible_grid, diff)

    return visible_grid, play, visited_cells


def first_interaction():
    print("Witaj w grze Saper!\nJeśli pojawią się błędy, zgłoś proszę!")


def game():
    first_interaction()
    diff = choose_difficulty()
    bomb_grid = set_bombs(diff)
    bomb_grid = numbers_near_bombs(bomb_grid, diff)
    player_guess(bomb_grid, diff)


#   change to 1 if you want to use test function instead if game()
TESTS = 0

if __name__ == "__main__":
    if TESTS:
        test_script()
    else:
        game()