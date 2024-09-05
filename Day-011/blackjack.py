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

# compute_score() - Add up and return the score for each player
def compute_score(current_hand):
    
    # initialize function variables
    calculated_score: int = 0
    card:             str = ""
    
    card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    for card in current_hand:
        calculated_score += card_values[cards.index(card)]
    
    return calculated_score
    

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
    card1:               str = ""
    card2:               str = ""
    computer_hand_value: int = 0
    hand_over:           bool = False
    game_over:           bool = False
    player_hand_value:   int = 0
    
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

    # Deal computer's first two cards
    card1, card2 = deal_cards(2)
    
    computers_hand.append(card1)
    computers_hand.append(card2)
    
    # Loop until hand is over
    while hand_over is False:

        # Add player and computer scores
        # Change score for Ace from 11 to 1 if a total score is > 21
        player_hand_value = compute_score(players_hand)
        #computer_hand_value = compute_score(computers_hand)
    
        # Show hands and player's score
        print(f'Your hand:     {", ".join(players_hand)}. Hand value: {player_hand_value}')
        print(f'Dealer\'s hand: {", ".join(computers_hand[1:])}')
           
        # Check for blackjack
        
        
        # Declare winner or push
        
        
        # Ask player for hit or stand
        
        
        # Computer hit or stand  
        
        #//// Temp break hand_over while loop ////
        hand_over = True

    # Ask user to play another game
    game_over = check_play_again()
    if game_over is False:
        main()

    return None

if __name__ == '__main__':
    main()
