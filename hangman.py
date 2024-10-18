import random
import os

os.system('cls')

#open file and create variables
word_list_eng = open('words_alpha.txt', 'r')
all_words_eng = word_list_eng.read().splitlines()
playable_words = []
guessed_letters_word = []
already_guessed_letters = []
guessed = False
hp_left = 10
is_single_letter = True
guessed_word_word = ""
is_in_word = False
chosen_word = ""
len_min = 0
len_max = 0




#get random word to guess
def get_random_word(word_list_chosen_lang,len_min,len_max):
    global guessed_letters_word
    for i000 in all_words_eng:
        if len_min <= len(i000) <= len_max:
            word_list_chosen_lang.append(i000)
    rand_word = random.choice(playable_words)
    for i001 in range(len(rand_word)):
        guessed_letters_word.append("_")        #create string with length len(rand_word) and '_' on each letter
    return rand_word


#function to check if guessed letter is in random word
def check_letter(letter,word):
    global is_in_word
    global guessed_letters_word
    global is_in_word
    global hp_left
    global already_guessed_letters
    place = 0
    for i002 in word:
        place += 1
        if i002 == letter:
            guessed_letters_word[place-1] = letter      #replace '_' with guessed letter at correct place
            is_in_word = True
    if not is_in_word:
        print ("This letter is not in this word")
        hp_left = hp_left - 1
    else:
        print("This letter is in this word")
    if is_in_word:
        is_in_word = False


#choose lang
def choose_lang():
    lang = input("Choose language: \n1. English\n2. Polish\nENTER NUMBER: ")
    if lang == "1":
        return("EN")
    elif lang == "2":
        return("PL")
    else:
        print("Wrong input! Try again")
        choose_lang()


#choose min and max word length
def choose_len():
    if chosen_lang == "EN":
        len_min = input("Choose minimum word length: ")
        len_max = input("Choose maximum word length: ")
        return(len_min,len_max)
    elif chosen_lang == "PL":
        len_min = input("Wybierz minimalną długość słowa: ")
        len_max = input("Wybierz maksymalną długość słowa: ")
        return(len_min,len_max)


# open file with words of chosen language
def open_file():
    1


def game():
    global chosen_lang
    global len_min
    global len_max
    print("Welcome to Hangman!")
     chosen_lang = choose_lang()
    len_min, len_max = choose_len()





#main game
random_word = get_random_word()
print ("Welcome in hangman!\nRandom word with length:",len(random_word),
       "has been chosen\nYour goal is to guess this word!\nEnter 'exit' to quit")
while not guessed:
    if hp_left == 0:
        print("sorry you lost :( better luck next time!")
        print("The word was:" , random_word)
        break
    guess_letter = input("Enter the letter you want to guess: ")
    if guess_letter == "exit":
        break
    os.system('cls')
    print("You guessed: ","'"+guess_letter+"'")
    if len(guess_letter) == 1 and not guess_letter in already_guessed_letters:
        check_letter(guess_letter, random_word)
        already_guessed_letters.append(guess_letter)
        guessed_word_word = ''.join(guessed_letters_word)
        print("Guessed letters:",guessed_word_word,"\nRemaining lives:",hp_left)
        if "_" not in guessed_letters_word:
            guessed = True
        if guessed:
            print("Congratulations! You guessed the word!")
    else:
        if len(guess_letter) != 1:
            if is_single_letter:
                print("This is not a single letter! Try again")
                print("Guessed letters:", guessed_word_word, "\nRemaining lives:", hp_left)
        elif guess_letter in already_guessed_letters:
            print("You already guessed this letter!")
            print("Guessed letters:", guessed_word_word, "\nRemaining lives:", hp_left)