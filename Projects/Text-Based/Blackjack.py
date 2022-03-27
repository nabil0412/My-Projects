import random
import os
clear = lambda: os.system('cls')
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
UserHand = []
DealerHand = []

def Deal(Hand,cards):
    Hand.append(random.choice(cards))
    
def Set1 (Hand):
    Result = 0
    for i in range(len(Hand)):
        Result = Result + Hand[i]
        if Hand[i] == 11:
            AceIndex = i

    if 11 in Hand and Result >= 21:
        Hand[AceIndex] = 1


def Compare(UserHand,DealerHand):
    DealerHandSum = sum(DealerHand)
    UserHandSum = sum(UserHand)

    while DealerHandSum < 17:
        Deal(DealerHand,cards)
        Set1(DealerHand)
        DealerHandSum = sum(DealerHand)


    if DealerHandSum < UserHandSum:
       print("Congrats you win!")
      
    elif DealerHandSum > 21:
        print("Congrats you win")
        
    elif DealerHandSum == UserHandSum:
        print("Draw") 
        
    else:
        print("Dealer wins, better luck next time")
        
    OutputHand(UserHand,DealerHand)
    quit()
       



def Hit(UserHand):
    Deal(UserHand,cards)
    Set1(UserHand)
    Result = sum(UserHand)
    if Result < 21:
        print(f"User's hand: {UserHand}")
        choice = input("Hit or stand? (H/S)")
        Choice(choice)
    elif Result > 21:
        print("Bust, better luck next time") 
        OutputHand(UserHand,DealerHand)
        quit()
    else:
        Compare(UserHand,DealerHand)    



def Choice(choice):
    while choice != 'H' and choice != 'S':
        choice = input("Pick a valid option, hit or stand? (H/S)")
    
    if choice == 'H':
        Hit(UserHand)
        Prompt(UserHand,DealerHand)
    else:
        Compare(UserHand,DealerHand)    



def Prompt(UserHand,DealerHand):
    if len(UserHand) == 2:
        print(f"User's hand: {UserHand}")
        print(f"Dealer's hand {DealerHand[0]}")
    else:
        print(f"User's hand: {UserHand}")
        print(f"Dealer's hand {DealerHand}")   

    
    choice = input("Hit or stand? (H/S)")
    Choice(choice)

def OutputHand(UserHand,DealerHand):
    print(f"User's hand: {UserHand}")
    print(f"Dealer's hand {DealerHand}")  


Deal(UserHand,cards)
Deal(UserHand,cards)
Set1(UserHand)

Deal(DealerHand,cards)
Deal(DealerHand,cards)
Set1(DealerHand)


Prompt(UserHand,DealerHand)    

  