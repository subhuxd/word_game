

import random
name = input("what is your name?\n")
print("good luck",name)
words = ['ranbow','sky','river','moon','star','ocean','tree']
print(words)

while True:
    turns = 3
    while turns > 0:
        word = random.choice(words)
        guess = input("guess the word: ")
        if guess == word:
            print("you win")
            break
        else:
            turns -= 1
            print("try again!")
            print("you have",turns,"more guesses")
            if turns == 0:
                print("you lose! the word is", word)
    play_again = input("Do you want to continue the game? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")