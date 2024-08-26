from blackjack_banner import banner
from shared_modules.system_modules import clear_terminal

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

# main() program logic module
def main():

    # initialize function variables
    hand_over: bool = False
    game_over: bool = False
    
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    computers_hand = []
    players_hand = []    

    # mainline statements
    
    # clear the terminal screenNo 
    clear_terminal()

    # print the application banner
    print(banner)
    
    # Deal player's first two cards
    
    
    # Deal computer's first two cards
    
    
    # Loop until hand over
    
    
        # Add player and computer scores
        # Change score for Ace from 11 to 1 if a total score is > 21
        
        
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
