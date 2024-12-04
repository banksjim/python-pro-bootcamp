# higher_lower - A simplified version of the higherlowergame.com which 
#                compares who has more followers on Instagram

import random

from shared_modules.system_modules import clear_terminal
from higher_lower_banners import app_banner
from higher_lower_banners import vs_banner
from game_data import data

class HigherLower:
    
    # Declare constants here
    
    def __init__(self): # Initializer function
        # Declare global variables and constants here
        return None

    def reset_screen(self): # Clear screen and print app banner
        clear_terminal()
        print(f'{app_banner}\n')
        return None

    def fetch_random_dict_entry(self, previous_data_dict_entry: Optional[dict[str, Any]] = None): # Fetch a random entry from the data list
        # Initialize fetch_random_dict_entry() variables
        random_data_dict_entry: dict[str, Any] = None
        
        # Retrieve a random game data dictionary entry
        random_data_dict_entry: dict[str, Any] = random.choice(data)
        
        # Ensure 
        while random_data_dict_entry == previous_data_dict_entry:
            random_data_dict_entry: dict[str, Any] = random.choice(data)
        
        return random_data_dict_entry

    def main(self): # Main app routine

        # Initialize main() variables
        choice_A: dict[str, Any] = None
        choice_B: dict[str, Any] = None
        game_over:     bool = False
        score:         int = 0

        # Main() logic
        while game_over is False:
        
            # Clear terminal screen and print app banner
            self.reset_screen()

            # Show current current score
            
            # Set a random dictionary 
            
            # Retrieve dict and show current questions
            choice_A = self.fetch_random_dict_entry()
            print(f'Compare: {choice_A['name']}')
            
            # TEMP: Break loop       
            game_over = True     
                    
        # Clear terminal screen and print app banner
        #self.reset_screen()
        
        # Show final score         

        return None

if __name__ == '__main__':
    app = HigherLower()
    app.main()
