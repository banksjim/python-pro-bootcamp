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
    end_game: bool = False
    
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    computers_hand = []
    players_hand = []    

    # mainline statements

    while end_game is False:

        # clear the terminal screen
        clear_terminal()

        # print the application banner
        print(banner)

        # Ask user to play another game
        end_game = check_play_again()

    return None

if __name__ == '__main__':
    main()
