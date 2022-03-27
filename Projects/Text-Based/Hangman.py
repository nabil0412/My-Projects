import os
clear = lambda: os.system('cls')


print(r'''

 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  


''')


def Illustration(NoOfGuesses):
    print()
    print()
    if NoOfGuesses == 6:
        print(r'''

            _______
            |/    |
            |     
            |     
            |      
            |     
            |
           _|___
            
        
        ''')

    elif NoOfGuesses == 5:
        print(r'''
        
            _______
            |/    |
            |    (_)
            |     
            |      
            |     
            |
           _|___

        ''')    

    elif NoOfGuesses == 4:
        print(r'''
        
            _______
            |/    |
            |    (_)
            |     |
            |     | 
            |     
            |
           _|___


        ''')  

    elif NoOfGuesses == 3:

        print(r'''
        
            _______
            |/    |
            |    (_)
            |    \|
            |     | 
            |     
            |
           _|___
        
        ''')

    elif NoOfGuesses == 2:

        print(r'''
        
            _______
            |/    |
            |    (_)
            |    \|/
            |     | 
            |     
            |
           _|___
        
        ''')   

    elif NoOfGuesses == 1:

        print(r'''
        
            _______
            |/    |
            |    (_)
            |    \|/
            |     | 
            |    / 
            |
           _|___
        
        ''') 


    elif NoOfGuesses == 0:

        print(r'''Out of guesses, better luck next time
        
            _______
            |/    |
            |    (_)
            |    \|/
            |     | 
            |    / \
            |
           _|___
        
        ''') 

def SearchRepeats(SavedGuesses,Letter):
      
    for l in SavedGuesses: 
        while Letter == l:
            Letter = input("Letter already guessed, try again: ")

    return Letter




Word = input("Please enter word to be guessed: ")
clear()
print()
LowerWord= Word.lower()
GuessString = [""] * len(Word)
for i in range(len(Word)):
    GuessString[i]= '*'

print(f"{' '.join(GuessString)}")



NoOfGuesses = 7
SavedGuesses = []
while NoOfGuesses != 0:
    FoundFlag = False
    print(f'Your guessed letters so far: {SavedGuesses}')
    Letter = input("Guess a letter: ")
  
    Letter = SearchRepeats(SavedGuesses , Letter)

    SavedGuesses.append(Letter)    
    for i in range(len(Word)):
        if Letter == LowerWord[i]:
            GuessString[i] = Letter
            FoundFlag = True


    if FoundFlag == False and NoOfGuesses == 1:
        clear()
        NoOfGuesses -= 1
        Illustration(NoOfGuesses)
        print("The correct word was: " + LowerWord)
        quit()
    
    if FoundFlag == False:
        clear()
        NoOfGuesses -= 1
        print("Wrong,Try again")
        print()
        print(f"{' '.join(GuessString)}")
        Illustration(NoOfGuesses)
    else:
        clear()
        print("Correct Guess!")
        print()
        print(f"{' '.join(GuessString)}")

    
    if '*' not in GuessString:
        clear()
        print("The correct word was: " + LowerWord)
        print("CONGRATS YOU WIN!")
        quit()
    
    
    
           
           