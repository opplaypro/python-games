# -*- coding: utf-8 -*-
import random
import os
import time

os.system('cls')

#get random word to guess
def get_random_word(word_list_chosen_lang , length_min , length_max):
    playable_words = []
    guessed_letters = []
    for i in word_list_chosen_lang:
        if length_min <= len( i ) <= length_max:
            playable_words.append(i)
    rand_word = random.choice(playable_words)
    for i in range( len( rand_word ) ):
        guessed_letters.append("_")        #create string with length len(rand_word) and '_' on each letter
    return rand_word, guessed_letters


#choose lang
def choose_lang():
    while True:
        lang = input("Choose language: \n1. English (English)\n2. Polish (Polski)\nENTER NUMBER (WPISZ NUMER): ")
        if lang == "1":
            return "EN"
        elif lang == "2":
            print("Uwaga!!! Wśród słów znajdują się też odmiany przez przypadki!!! weż to pod uwagę!") #only in polish, weird lang
            time.sleep(3)
            os.system("cls")
            return "PL"
        else:
            os.system("cls")
            print("Wrong input! Try again")


#choose min and max word length
def choose_len(lang_lang):
    while True:
        if lang_lang == "EN":
            length_min = input("Choose minimum word length (recommended 5): ")
            length_max = input("Choose maximum word length (recommended 12): ")
            try:
                int(length_min)
                int(length_max)
            except ValueError:
                print("Wrong input! Try again")
            else:
                length_min = int(length_min)
                length_max = int(length_max)
                if length_min>length_max:
                    print("Wrong input! Try again")
                else:
                    return length_min, length_max
        elif lang_lang == "PL":
            length_min = input("Wybierz minimalną długość słowa (zalecana to 5): ")
            length_max = input("Wybierz maksymalną długość słowa (zalecana to 12): ")
            try:
                int(length_min)
                int(length_max)
            except ValueError:
                print("Błedne dane! Spróbuj ponownie!")
            else:
                length_min = int(length_min)
                length_max = int(length_max)
                if length_min>length_max:
                    print("Błędne dane! Spróbuj ponownie!")
                else:
                    return length_min, length_max


# open file with words of chosen language
def open_file(language):
    if language == "EN":
        list_all = open('words_EN.txt','r', encoding="utf-8")
        words = list_all.read().splitlines()
        return words
    elif language == "PL":
        list_all = open('words_PL.txt','r', encoding="utf-8")
        words = list_all.read().splitlines()
        return words


# main function of the game
def game_run():
    print("Welcome to Hangman!")
    lang_lang = choose_lang()
    len_min , len_max = choose_len(lang_lang)
    word_list = open_file(lang_lang)
    random_word,guesses_letters_word =  get_random_word(word_list, len_min, len_max)
    game_main_loop(lang_lang, random_word, guesses_letters_word)
    print("Thanks for playing! See you next time!")


#main loop of the game, works till player guesses or looses
def game_main_loop(lang_lang, word, guessed_letters_word):
    guess_history = []
    hp_left = 10 # if fancy, make choosable
    while True:
        if hp_left == 0:
            if lang_lang == "EN":
                print("Sorry you lost :( better luck next time! The word was:",word)
                break
            if lang_lang == "PL":
                print("Przykro mi, przegrałeś :( powodzenia następnym razem! słowo to:",word)
                break
        guessed_letters, guess_history, hp_left = user_guess(lang_lang, word, guessed_letters_word, guess_history,hp_left)
        if "_" not in guessed_letters_word:
            if lang_lang == "EN":
                print("You guessed the word!, it was:",word)
                break
            elif lang_lang == "PL":
                print("Odgadłeś słowo! to było:",word)
                break
        else:
                if lang_lang == "EN":
                    print("Guessed letters:",''.join(guessed_letters_word))
                elif lang_lang == "PL":
                    print("Odgadnięte litery:",''.join(guessed_letters_word))


# this function  gets input from user and checks if the letter is in word
def user_guess(lang_lang, word, guessed_letters_word, history, hp):
    if lang_lang == "EN":
        guess_letter = input("Guess a letter: ")
        valid = validate_guess(guess_letter,history)
        is_letter_in_word = False
        if valid:
            position = 0
            history.append(guess_letter)
            for i in word:
                if i == guess_letter:
                    guessed_letters_word[position] = guess_letter
                    is_letter_in_word = True
                position += 1
        else:
            if len(guess_letter) != 1:
                print("This is not a single letter! Try again")
            else:
                print("You already guessed this letter!")
        if is_letter_in_word:
            print("This letter is in this word")                    #FIX!!!!
        else:
            hp = hp - 1
            print("This letter is not in this word\nTries left:",hp)
        return guessed_letters_word, history, hp
    elif lang_lang == "PL":
        guess_letter = input("Zgadnij literę: ")
        valid = validate_guess(guess_letter,history)
        is_letter_in_word = False
        if valid:
            position = 0
            for i in word:
                if i == guess_letter:
                    guessed_letters_word[position] = guess_letter
                    is_letter_in_word = True
                position += 1
        else:
            if len(guess_letter) != 1:
                print("To nie jest pojedyncza litera!")
            else:
                print("Już zgadłeś tę literę!")
        if is_letter_in_word:
            print("Ta litera jest w słowie")                    #FIX!!!!
        else:
            hp = hp - 1
            print("Tej litery nie ma w tym słowie, pozostałe próby:",hp)
        return guessed_letters_word , history, hp


# checks if player already guessed that letter or input more than one letter
def validate_guess(guess,already_guessed):
    validated = True
    if len(guess) > 1:
        validated = False
    if guess in already_guessed:
        validated = False
    already_guessed.append(guess)
    return validated


# no comment here
if __name__ == "__main__":
    guessed_word_word = ""
    game_run()
