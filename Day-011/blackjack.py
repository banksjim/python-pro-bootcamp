import random

from blackjack_banner import banner
from shared_modules.system_modules import clear_terminal

# declare static global variables
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# check_play_again() - Check if the player wants to play another round
def check_play_again():
    # initialize function variables
    play_again: str = 'n'
       
    # Ask user to play another game
    play_again = input('\nPlay again (y/n)? ').lower()

    if play_again == 'y' or play_again == 'yes':
        return False
    elif play_again == 'n' or play_again == 'no':
        print("Goodbye!")
        return True
    else:
        return check_play_again()

# deal_cards() - Deals any player 1 or 2 random cards from the cards list
def deal_cards(number_of_cards: int = 0):
    # initialize function variables
    draw1: str = ""
    draw2: str = ""  
    
    draw1 = random.choice(cards)
            
    if number_of_cards == 1:    
        return draw1
    elif number_of_cards == 2:
        draw2 = random.choice(cards)
        return draw1, draw2
    else: 
        print("Error: Call to deal_cards must pass 1 or 2.")

# main() program logic module
def main():

    # initialize function variables
    card1:     str = ""
    card2:     str = ""
    hand_over: bool = False
    game_over: bool = False
    
    card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    computers_hand = []
    players_hand = []    

    # mainline statements
    
    # clear the terminal screenNo 
    clear_terminal()

    # print the application banner
    print(banner)
    
    # Deal player's first two cards
    card1, card2 = deal_cards(2)
    
    players_hand.append(card1)
    players_hand.append(card2)
    
    # move to Show hands below
    print(f'Your hand: {", ".join(players_hand)}')
    
    # Deal computer's first two cards
    card1, card2 = deal_cards(2)
    
    computers_hand.append(card1)
    computers_hand.append(card2)
    
    # move to Show hands below
    print(f'Your hand: {", ".join(computers_hand[1:])}')
    
    # Loop until hand is over
    
        # Add player and computer scores
        # Change score for Ace from 11 to 1 if a total score is > 21
        
        # Show hands
        
        # Check for blackjack
        
        
        # Declare winner or push
        
        
        # Ask player for hit or stand
        
        
        # Computer hit or stand  


    # Ask user to play another game
    game_over = check_play_again()
    if game_over is False:
        main()

    return None

if __name__ == '__main__':
    main()
