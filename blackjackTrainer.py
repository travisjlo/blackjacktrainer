import random
import os
import multiprocessing
import math
import time

# Atom shotrtcuts:
#f5 to run or control-shift-b

print ("Welcome to Blackjack training!\n")

session = True

while session:
    #random initial player hand total (9-20 assuming no blackjack)
    from random import randrange
    player_hand = random.randint(9,20)
    print("Players hand total: " + str(player_hand))

    #random initial dealer card total (4-20 assuming no blackjack)
    from random import randrange
    dealer_card = random.randint(2,11)
    print("Dealer's face-up card: "+ str(dealer_card))

    print("What should you do: hit, double or stay")
    user_input = input("please type H, D, or S: ")
    print("You selected: " + str(user_input))

    if player_hand == 9:
        if dealer_card == 2:
            if user_input == "H":
                print("Correct choice")
            else:
                print("Wrong choice should have hit")
        elif dealer_card >=3 and dealer_card < 7:
            if user_input == "D":
                print("Correct choice")
            else:
                print("Wrong choice should have double")
        else:
            if user_input == "H":
                print("Correct choice")
            else:
                print("Wrong choice should have hit")

    if player_hand == 10:
        if dealer_card >=2 and dealer_card < 10:
            if user_input == "D":
                print("Correct choice")
            else:
                print("Wrong choice should have double")
        else:
            if user_input == "H":
                print("Correct choice")
            else:
                print("Wrong choice should have hit")

    if player_hand == 11:
        if user_input == "D":
            print("Correct choice")
        else:
            print("Wrong choice should have double")

    if player_hand == 12:
        if dealer_card >= 4 and dealer_card < 7:
            if user_input == "S":
                print("Correct choice")
            else:
                print("Wrong choice should have stayed")
        else:
            if user_input == "H":
                print("Correct choice")
            else:
                print("Wrong choice should have hit")

    if player_hand == 13 or player_hand == 14 or player_hand == 15 or player_hand == 16:
        if dealer_card >= 2 and dealer_card <7:
            if user_input == "S":
                print("Correct choice")
            else:
                print("Wrong choice should have stayed")
        else:
            if user_input == "H":
                print("Correct choice")
            else:
                print("Wrong choice should have hit")

    if player_hand >=17:
        if user_input == "S":
            print("Correct choice")
        else:
            print("Wrong choice should have stayed")

    print("")
    again = input("Would you like to play again? (y/n): ")
    if again == 'y':
        session = True
    else:
        print("Goodbye!")
        session = False
