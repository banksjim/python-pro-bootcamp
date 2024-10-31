# Guess_the_Number - Guess the number from 1 to 100 with two difficulty levels
import random

from guess_the_number_banner import banner
from shared_modules.system_modules import clear_terminal

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

class Guess_the_Number:
   
    def __init__(self): # Initializer function
        return None

    def choose_difficulty(self): # User chooses difficulty level 'easy' or 'hard'
                                 # Set max guesses
        
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
                
                print('Alright, let\'s go!\n')
                   
                if (level == 'e' or
                    level == 'easy'):
                   
                    return EASY_LEVEL_TURNS
                   
                elif (level == 'h' or
                    level == 'hard'):
                    
                    return HARD_LEVEL_TURNS               
                
        return None

    def end_game(self, correct_guess, guess_count, random_number): # Show final game results
        
        if correct_guess is True:
            print(f'You got it in {guess_count} guesses! The answer was {random_number}.')  
        else:
            print(f'You lose. The correct number was {random_number}.')

    def evaluate_guess(self, random_number, user_guess): # Test if the guess is
                                                         # matching, high, or low
        
        # Initialize function variables
        matching_guess: bool = False
        
        if user_guess == random_number:  

            # Winner!
            matching_guess = True                            

        elif user_guess < random_number:
            
            # Too low
            matching_guess = False
            print('Too low.')

        else:

            # Too high
            matching_guess = False
            print('Too high.')
        
        return matching_guess

    def guess_number(self): # Input user guess and validate it
        
        # Initialize function variables
        user_guess_input: str = ''
        valid_guess:      bool = False
        
        # Loop until valid guess is confirmed
        while valid_guess is False:
            
            # User inputs their guess
            user_guess_input = input('Make a guess: ')
            
            # Check that the user's guess is an integer
            if user_guess_input.isdigit():
                
                # Check that the guess is between 1 and 100
                if int(user_guess_input) in range(1, 101):
                    
                    # A guess in the correct range is returned by the function
                    valid_guess = True
                    return int(user_guess_input)
                else:
                    print('Guesses must be in the range of 1 to 100.')
                
            else:
                print('Error: Input a valid integer number.')            

    def main(self): # Main app routine

        # Initialize main() variables
        correct_guess:    bool = False
        guess_count:      int = 0
        max_guesses:      int = 0
        random_number:    int = 0
        user_guess:       int = ''

        # Clear terminal screen and show banner
        clear_terminal()
        print(f'{banner}\n')
        print('Welcome to the number guessing game!\n')

        # Main() logic  
        
        # User chooses difficulty level
        max_guesses = self.choose_difficulty()
        
        # Start game
        print('I\'m thinking of a number between 1 and 100.\n')
        
        # Choose random number for game round
        random_number = random.randint(1, 100)
        
        # Loop until number is guessed or run out of guesses
        while (correct_guess is False and
               guess_count < max_guesses):
            
            # Show user remaining guesses
            print(f'You have {max_guesses - guess_count} attempts remaining to guess the number.')           
            
            # Receive and validate the user's guess
            user_guess = self.guess_number()
            guess_count += 1
            
            # Evaluate the guess
            correct_guess = self.evaluate_guess(random_number, user_guess)
                
        # Show final result       
        self.end_game(correct_guess, guess_count, random_number)
                
        return None

if __name__ == '__main__':
    app = Guess_the_Number()
    app.main()
