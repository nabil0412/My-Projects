import os
clear = lambda: os.system('cls')

def SetBid(Dict):
  Name = input("What is your name? ")
  Bid = int(input("How much would you like to bid? $"))
  Dict[Name] = Bid
  
  Choice = "X"
  while Choice != "Y" and Choice != "N":
    Choice = input("Would you like to continue? (Y/N) ")

  clear()


  return Choice


Bids = {}

logo = r'''

___________
\         /
)_______(
|"""""""|_.-._,.---------.,_.-._
|       | | |               | | ''-.
|       |_| |_             _| |_..-'
|_______| '-' `'---------'` '-'
)"""""""(
/_________\
`'-------'`

'''

endlogo = r'''

            $$ $             
             \O/$            
            $ |              
             /_\             
           _|___|_           
         _|___|___|_         
       _|___|___|___|_       
     _|___|___|___|___|_     
   _|___|___|___|___|___|_   
 _|___|___|___|___|___|___|_ 
|___|___|___|___|___|___|___|
 \o/ \o/ \o/ \o/ \o/ \o/ \o/ 
  |   |   |   |   |   |   |  
 / \ / \ / \ / \ / \ / \ / \ 


'''

print(logo)
print("Welcome to the silent auction")
Choice = SetBid(Bids)
while Choice != "N":
  Choice = SetBid(Bids) 

HighestBid = 0
for name in Bids:
  val = Bids[name]
  if val > HighestBid:
    HighestBid = val
    BidWinner = name


print(f"{BidWinner} has won the auction with a bid of ${HighestBid}")  
print(endlogo)  
    
    