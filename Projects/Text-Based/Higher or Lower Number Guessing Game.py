import random

Num = random.randint(0,100)
print(Num)

def Guess(Num):
    Difficulty = input("Choose difficulty, easy or hard (E/H)")
    if Difficulty == 'E':
        NoOfGuesses = 9
    elif Difficulty == 'H':
        NoOfGuesses = 4
    else:
        NoOfGuesses = 0

    Guess = int(input("Enter your guess: "))
    while Guess != Num and NoOfGuesses != 0:
        if Guess < Num:
            Guess = int(input("Too low , try again: "))
            NoOfGuesses -= 1
        elif Guess > Num:
            Guess = int(input("Too high , try again: "))
            NoOfGuesses -= 1   

    print()
    print()
    if NoOfGuesses == 0 :
        print("Out of guesses, better luck next time")
    else:
        print("Correct guess , you win!")
        print(f"Your number of guesses was {NoOfGuesses}")

    print(f"The correct number is {Num}")        
          


Guess(Num)
