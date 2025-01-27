# higher_lower - A simplified version of the higherlowergame.com which 
#                compares who has more followers on Instagram

import random

from typing import Any, Optional

from game_data import data
from higher_lower_banners import app_banner
from higher_lower_banners import vs_banner
from shared_modules.system_modules import clear_terminal

class HigherLower:
    
    # Declare constants here
    
    # Initializer function
    def __init__(self):
        # Declare global variables and constants here
        return None

    # Clear screen and print app banner
    def reset_screen(self):
        clear_terminal()
        print(f'{app_banner}\n')
        return None

     # Fetch a random entry from the data list
    def fetch_random_dict_entry(self, previous_data_dict_entry: Optional[dict[str, Any]] = {}):        
        
        # Initialize fetch_random_dict_entry() variables
        random_data_dict_entry: dict[str, Any] = {}
                
        # Retrieve a random, but also unique, game data dictionary entry
        while (random_data_dict_entry == previous_data_dict_entry) or (not random_data_dict_entry):
            random_data_dict_entry: dict[str, Any] = random.choice(data)
        
        return random_data_dict_entry

    # Main app routine
    def main(self):

        # Initialize main() variables
        choice_A:   dict[str, Any] = {}
        choice_B:   dict[str, Any] = {}
        game_over:  bool = False
        user_guess: str = ""
        score:      int = 0

        # Seed choice_A for round 1
        choice_A = self.fetch_random_dict_entry()
        
        # Loop until player loses or decides to quit
        while game_over is False:
        
            # Clear terminal screen and print app banner
            self.reset_screen()           

            # Show current current score
            if score > 0:
                print(f'That\'s right! Your current score is: {score}.\n')
                        
            # Retrieve random values for choice_b
            choice_B = self.fetch_random_dict_entry(choice_A)
            
            # Show current comparisons
            print('Ready? Compare or \'Q\' to quit...\n')
                       
            if (choice_A['country'] == 'United States') or \
               (choice_A['country'] == 'United Kingdom'):
                print(f'A: {choice_A['name']}, a {choice_A['description']} from the '
                      f'{choice_A['country']}.')
            else:
                print(f'A: {choice_A['name']}, a {choice_A['description']} from '
                      f'{choice_A['country']}.')
            
            print(f'{vs_banner}')
            
            if (choice_B['country'] == 'United States') or \
               (choice_B['country'] == 'United Kingdom'):
                print(f'B: {choice_B['name']}, a {choice_B['description']} from the '
                      f'{choice_B['country']}.')
            else:
                print(f'B: {choice_B['name']}, a {choice_B['description']} from '
                      f'{choice_B['country']}.')
           
            # input user guess
            user_guess = input('\n Who has the most followers (\'A\' or \'B\')? ').upper()
            
            
            
            # TEMP: Break loop       
            game_over = True     
                    
        # Clear terminal screen and print app banner
        #self.reset_screen()
        
        # Show final score         

        return None

if __name__ == '__main__':
    app = HigherLower()
    app.main()
