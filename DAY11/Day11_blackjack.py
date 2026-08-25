"""BLACKJACK"""
import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
###### deal cards
def deal_card():
    """Returns random card from the deck"""
    if to_play == "y" or to_deal_another_hand =="y":
        return random.choice(cards)

def result():
    """Takes chosen cards and return result"""
    if sum(user_card) <= 21 and (sum(user_card) > sum(computer_card) or sum(computer_card) > 21):
        return "Congratulations. You win"
    elif sum(user_card) <= 21 and (sum(user_card) == sum(computer_card)):
        return "It's a draw"
    elif sum(user_card) > 21:
        return "You went over. You lose"
    else:
        return("You lose")
    
    
 
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_card = []
computer_card = []

to_play = str(input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")).lower()
clear_screen()

while to_play == "y":
    user_card = []
    computer_card = []
    
###### Deal first hand
    for i in range(2):
        #to run it twice#
        user_card.append(deal_card())
        user_view_card = user_card.copy()
        computer_card.append(deal_card())
        computer_view_card = computer_card.copy()  
    
###### ACE CONDITION
    if sum(user_card) > 21 and 11 in user_card:
        user_card[user_card.index(11)] = 1
            
    if sum(computer_card) > 21 and 11 in computer_card:
        computer_card[computer_card.index(11)] = 1     
    
    print(f"Your cards: {user_view_card}, current score: {sum(user_card)} \n Computer's first card: {computer_view_card[0]}")
    
    outcome = result()
    if sum(user_card) == 21 or sum(computer_card) == 21:
        print(outcome)
        to_play = str(input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")).lower()
        
    else:
###### ANOTHER HAND
        to_deal_another_hand = str(input("\nType 'y' to get another card, type 'n' to pass: ")).lower()
        
            
        while to_deal_another_hand == "y" and sum(user_card) < 21:
              
            user_card.append(deal_card())
            user_view_card= user_card.copy()
            
            for i in user_card:
                if sum(user_card) > 21 and 11 in user_card:
                    user_card[user_card.index(11)] = 1
        
            print(f"Your cards: {user_view_card}, current score: {sum(user_card)}")
            
            
            outcome = result()
            if sum(user_card) == 21:
                to_deal_another_hand = "n"
                if sum(computer_card) >= 17:
                    print(outcome)
                    to_deal_another_hand = "n"
                    
            elif sum(user_card) > 21:
                    #print(outcome)
                    to_deal_another_hand = "n"
                    
            else:
                to_deal_another_hand = str(input("\nType 'y' to get another card, type 'n' to pass: ")).lower()                 
             
        else:
            if to_deal_another_hand == "n":
                print(f"\nComputer's first hand: {computer_view_card}")
                print("\nRESULT:")       
            else:
                print("Invalid input")
        
            
       #### Computer less than 17
        while sum(computer_card) < 17 and sum(user_card) <= 21:
            computer_card.append(deal_card())
            computer_view_card = computer_card.copy()
            for i in computer_card:
                if sum(computer_card) > 21 and 11 in computer_card:
                    computer_card[computer_card.index(11)] = 1

        print(f"Your final cards: {user_view_card}, final_score: {sum(user_card)} \nComputer's final cards: {computer_view_card}, final score: {sum(computer_card)} \n")   
        
        outcome = result()
        print(outcome)
            
        
        to_play = str(input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")).lower()
        
if to_play == "n":
    print("GAME ENDS")
else:
    print("Invalid input")
    

