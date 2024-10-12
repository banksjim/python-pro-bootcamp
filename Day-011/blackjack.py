import random
import time

from blackjack_banner import banner
from shared_modules.system_modules import clear_terminal

# declare static global variables
dealer_score: int = 0
player_score: int = 0 

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
        print('Goodbye!')
        return True
    else:
        return check_play_again()

# compute_score() - Add up and return the score for each player
def compute_score(current_hand):
    
    # initialize function variables
    calculated_score: int = 0
    card:             str = ''
    
    card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    # add raw score of current_hand
    for card in current_hand:
        calculated_score += card_values[cards.index(card)]
    
    # if calculated_score is over 21 and aces are in the hand
    # then reduce each ace from a value of 11 to 1
    # until score < 21 (if possible)
    for card in current_hand:
        if (calculated_score > 21) and (card == 'A'):
            calculated_score -= 10
    
    return calculated_score

# deal_cards() - Deals any player 1 or 2 random cards from the cards list
def deal_card():
    
    # initialize function variables
    draw: str = ''
    
    # deal card and handle out of bounds function call
    draw = random.choice(cards)
            
    return draw

# hit_or_stand() - Hand dealer and user action for hit or stand
def hit_or_stand(person_up: str = '', hand_value: int = 0):
    
    # initialize function variables
    hit:        str = ''
    draw_card:       str = ''
        
    # Handle hit or stand
    if person_up == 'Player':
        hit = input('\nHit another card (y/n)? ').lower()
    elif person_up == 'Dealer':
        if hand_value < 17:
            hit = 'y'
        else:
            hit = 'n'
    else:
        print('Error: Call to hit_or_stand must pass "Player" or "Dealer".')

    # handle hit or stand responses, or out of bounds function call
    if hit == 'y' or hit == 'yes':
        draw_card = deal_card() 
        return draw_card
    elif hit == 'n' or hit == 'no':
        draw_card = "STAND"
        return draw_card
    else:
        return hit_or_stand(person_up)                

# main() program logic module
def main():

    # declare global variables
    global dealer_score
    global player_score
        
    # initialize function variables   
    draw_card:           str = ''
    computer_stands:     bool = False
    computer_hand_value: int = 0
    computer_wins:       bool = False
    game_over:           bool = False
    player_stands:       bool = False
    player_hand_value:   int = 0
    player_wins:         bool = False
    
    computers_hand = []
    players_hand = []    
      
    # Deal first two cards for player and dealer
    for _ in range(2):    
        players_hand.append(deal_card())
        computers_hand.append(deal_card())
    
    # Loop until hand is over
    while player_wins is False and computer_wins is False:

        # Add player and computer scores
        # Change score for Ace from 11 to 1 if a total score is > 21
        player_hand_value = compute_score(players_hand)
        computer_hand_value = compute_score(computers_hand)
    
        # clear the terminal screen 
        clear_terminal()

        # print the application banner
        print(banner)
    
        # print the current score
        print(f'Player: {player_score} | Dealer: {dealer_score}\n')
    
        # Show hands and player's score
        print(f'Your hand:     {", ".join(players_hand)}')
        print(f'Dealer\'s hand: _, {", ".join(computers_hand[1:])}') 
           
        # Check player for blackjack
        if player_hand_value == 21:
            player_wins = True
            print('\nPlayer has Blackjack! Congratulations!')
            
        # Check dealer for blackjack
        if computer_hand_value == 21:
            computer_wins = True
            
            if player_wins is False:
                print('\nDealer has Blackjack!')
            else:
                print('But... The Dealer also Blackjack!')       
        
        # Check player for busted
        if player_hand_value > 21:
            computer_wins = True
            print(f'\nPlayer has BUSTED with a hand value of {player_hand_value}!')
            
        # Check dealer for busted
        if computer_hand_value > 21:
            player_wins = True
            print('\nDealer has BUSTED!')
        
        # Check if both player and dealer stand
        if player_stands is True and computer_stands is True:
            if player_hand_value > computer_hand_value:
                player_wins = True
            elif player_hand_value < computer_hand_value:
                computer_wins = True
            else:
                player_wins = True
                computer_wins = True                
        
        # Declare winner or push        
        if player_wins is True and computer_wins is True:
            print(f'\nDealer\'s hand is: {", ".join(computers_hand)}. ' \
                  f'Hand value: {computer_hand_value}')
            print('\nGame ends in a push.')
        elif player_wins is True:
            player_score += 1
            print(f'\nDealer\'s hand was: {", ".join(computers_hand)}. ' \
                  f'Hand value: {computer_hand_value}')
            print('\nThe player WINS!')
        elif computer_wins is True:
            dealer_score += 1
            print(f'\nDealer\'s hand was: {", ".join(computers_hand)}. ' \
                  f'Hand value: {computer_hand_value}')
            print('\nThe dealer WINS!')

        # Hit or stand
        if player_wins is False and computer_wins is False:
           
            # Player hit or stand
            if player_stands is False:
                draw_card = hit_or_stand('Player')
                
                if draw_card != 'STAND':
                    print('\n--> Player draws...')
                    time.sleep(3) 
                    players_hand.append(draw_card)
                else:
                    player_stands = True
                    print('\n--> Player stands...')
                    time.sleep(3)          
        
            # Computer hit or stand
            if computer_stands is False:
                draw_card = hit_or_stand('Dealer', computer_hand_value)
                
                if draw_card != 'STAND':                       
                    print('\n--> Dealer draws...')
                    time.sleep(3)
                    computers_hand.append(draw_card)
                else:
                    computer_stands = True
                    print('\n--> Dealer stands...')
                    time.sleep(3)    

    # Ask user to play another game
    game_over = check_play_again()
    if game_over is False:
        main()

    return None

if __name__ == '__main__':
    main()
