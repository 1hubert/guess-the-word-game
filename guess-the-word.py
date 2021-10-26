""" todo:
zastanowić się czy na pewno potrzebne są zmienne global
it took you 6 moves, the best possible is 4
"""

import random

word_bank = [["Games", "No Mans Sky"], ["Anime", "Kono Subarashii Sekai ni Shukufuku o"], ["Hobbies", "programming"], ["Books", "The Martian"], ["Movies", "Zodiac"], ["Movies", "Fight Club"]]


def prepare_guess():
    word = word_bank[random.randrange(len(word_bank))]
    print("Category: " + word[0])
    guess = []
    chars = 0
    for char in word[1]:
        if char != " ":
            guess.append(["_", char])
            chars += 1
        elif char == " ":
            guess.append("  ")
    print(str(chars) + " letters.")
    return guess


def show():
    hidden_guess = ""
    for elem in guess:
        hidden_guess += elem[0] + " "
    return hidden_guess


def remaining():
    letters = ""
    for elem in guess:
        if elem != " " and elem[0] != elem[1]:
            letters += elem[1].lower()

    return letters


guess = prepare_guess()
moves = 0


def input_and_check():
    global is_running
    global moves
    global guess

    moves += 1
    remaining_letters = remaining()

    hidden_guess = show()
    print()
    print(hidden_guess)
    print()
    print()
    print()
    print("What is your guess?")
    inp = input(">>> ")

    while len(inp) != 1 or inp is False:
        print()
        print(hidden_guess)
        print()
        print("Sorry, wrong input.")
        print("Your guess must be single character.")
        print("What is your guess?")
        inp = input(">>> ")

    if inp != " " and inp.lower() in remaining_letters:
        print(inp + " is a part of the word!")
        for i in guess:
            if i != " " and inp.lower() == i[1] or inp.upper() == i[1]:
                i[0] = i[1]
    else:
        print(inp + " is not a part of the word or was already used.")

    remaining_letters = remaining()
    if remaining_letters == "":
        hidden_guess = show()
        print()
        print(hidden_guess)
        print()
        print("YOU WIN!")
        print("It took you " + str(moves) + " moves.")
        print("Play again? (yes/no)")
        choice = input(">>> ")
        while choice != "no" and choice != "nah" and choice != "yes" and choice != "yeah":
            print("Wrong input!")
            print("Play again? (yes/no)")
            choice = input(">>> ")
            if choice == "no" or choice == "nah":
                is_running = False
            elif choice == "yes" or choice == "yeah":
                guess = prepare_guess()
                moves = 0
        if choice == "no" or choice == "nah":
            is_running = False
        elif choice == "yes" or choice == "yeah":
            guess = prepare_guess()
            moves = 0


is_running = True

while is_running:
    input_and_check()
