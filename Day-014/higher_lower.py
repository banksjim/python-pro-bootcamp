# higher_lower - A simplified version of the higherlowergame.com which 
#                compares who has more followers on Instagram

import random

from typing import Any, Optional

from game_data import data
from higher_lower_banners import app_banner
from higher_lower_banners import vs_banner
from shared_modules.system_modules import clear_terminal, press_any_key_to_continue

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
        choice_A:         dict[str, Any] = {}
        choice_B:         dict[str, Any] = {}
        chosen_choice:    dict[str, Any] = {}
        correct_choice:   str = ''
        game_over:        bool = False
        unchosen_choice:  dict[str, Any] = {}
        user_guess:       str = ''
        score:            int = 0

        # Seed choice_A for round 1
        choice_A = self.fetch_random_dict_entry()
        
        # Loop until player loses or decides to quit
        while game_over is False:
        
            # Clear terminal screen and print app banner
            self.reset_screen()           

            # Clear user's previous guess
            user_guess = ''

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
           
            # Input and validate user guess
            while user_guess not in {'A', 'B', 'Q'}:
                user_guess = input('\n--> Who has the most followers (\'A\' or \'B\')? ').upper()
            
            # Assign chosen_choice and alternative_choice values
            if user_guess in {'A', 'B'}:
                chosen_choice = choice_A if user_guess == 'A' else choice_B
                unchosen_choice = choice_B if user_guess == 'A' else choice_A            
            
            # Assess and determine the correct choice for highest followers
            if int(choice_A['follower_count']) > int(choice_B['follower_count']):
                correct_choice = 'A'
            elif int(choice_A['follower_count']) == int(choice_B['follower_count']):
                correct_choice = 'T' # Tie - Followers for each choice are equal
            else:
                correct_choice = 'B'         
            
            # Evaluate the user's guess. Assess choice, handle tie, or quit early
            if user_guess == 'Q':
                game_over = True # Quit game early
            elif (user_guess == correct_choice) or (correct_choice == 'T'): # Correct guess or tie                               
                if correct_choice == 'T':
                    print(f'\nBoth choices had {choice_A['follower_count']} million followers. '
                          'Lucky win for you!')                  
                else:
                    print(f'\nGreat guess. Choice {user_guess} has '
                          f'{chosen_choice["follower_count"]} million followers.')
                
                # If the user guessed 'B' then assign choice B to choice A for next round
                if user_guess == 'B':
                    choice_A = choice_B
               
                # Increase score by 1
                score += 1
                
            else: # Incorrect guess
                game_over = True
                print(f'\nSorry. {unchosen_choice['name']} has '
                      f'{unchosen_choice['follower_count']} million followers. '
                      f'But {chosen_choice['name']} only has '
                      f'{chosen_choice['follower_count']} million followers. You lose.')
                
            # Press any key to continue
            if game_over is False:
                press_any_key_to_continue()
                    
        # Clear terminal screen and print app banner
        self.reset_screen()
                
        # Show final score
        print(f'Final score: {score}')

        return None

if __name__ == '__main__':
    app = HigherLower()
    app.main()
