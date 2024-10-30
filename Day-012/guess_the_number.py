# Guess_the_Number - Guess the number from 1 to 100 with two difficulty levels
import random

from guess_the_number_banner import banner
from shared_modules.system_modules import clear_terminal

class Guess_the_Number:
    
    def __init__(self): # Initializer function
        return None

    def choose_difficulty(self): # User chooses difficulty level 'easy' or 'hard'
        
        # Initialize function variables
        level:            str = ''
        user_input_valid: bool = False
        
        # Loop asking user for difficulty level until easy or hard is chosen
        while user_input_valid is False:
            level = input('Choose a difficulty. Type \'easy\' or \'hard\': ')
        
            # Validate user input for level
            if (level == 'easy' or
               level == 'e'    or
               level == 'hard' or
               level == 'h'):
                user_input_valid = True
                   
                if level == 'e':
                    level = 'easy'
                elif level == 'h':
                    level = 'hard'
                
                print('Alright, let\'s go!\n')
                    
                return level             
        
        return level

    def set_guess_count(self, user_difficulty: str = ''): # Set max number of user guesses
                                                          # based on difficulty selected earlier
        
        easy_level_max_guesses: int = 5
        hard_level_max_guesses: int = 10
        
        # Set the max guesses based on the user_difficulty provided
        if user_difficulty == 'easy':
            return easy_level_max_guesses
        elif user_difficulty == 'hard':
            return hard_level_max_guesses
        else:
            print(f'ERROR: Invalid difficulty level passed to function: {user_difficulty}.')        
        
        return None

    def main(self): # Main app routine

        # Initialize main() variables
        correct_guess:    bool = False
        difficulty_level: str = ''
        guess_count:      int = 0
        max_guesses:      int = 0
        random_number:    int = 0
        user_guess:       str = ''

        # Clear terminal screen and show banner
        clear_terminal()
        print(f'{banner}\n')
        print('Welcome to the number guessing game!\n')

        # Main() logic  
        
        # User chooses difficulty level
        difficulty_level = self.choose_difficulty()
        
        # Set maximum guess count based on difficulty level
        max_guesses = self.set_guess_count(difficulty_level)
        
        # Start game
        print('I\'m thinking of a number between 1 and 100.\n')
        
        # Choose random number for game round
        random_number = random.randint(1, 100)
        
        # Loop until number is guessed or run out of guesses
        while (correct_guess is False and
               guess_count <= max_guesses):
            
            # Show user remaining guesses
            print(f'You have {max_guesses - guess_count} attempts remaining to guess the number.')           
            
            # User inputs their guess (**Turn the lines below into a function that loops for a valid response**)
            user_guess = input('Make a guess: ')
            
            # Check that the user's guess is an integer
            if user_guess.isdigit():
                #stuff
            else:
                print('Please input a valid integer number.')
            

        return None

if __name__ == '__main__':
    app = Guess_the_Number()
    app.main()







# main() program logic module
def main():

    # initialize module variables   


    # mainline statements
    clear_terminal()
    print(f'{banner}\n')

    return None

if __name__ == '__main__':
    main()
