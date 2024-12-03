# higher_lower - A simplified version of the higherlowergame.com which 
#                compares who has more followers on Instagram

import random

from shared_modules.system_modules import clear_terminal
from higher_lower_banners import app_banner
from higher_lower_banners import vs_banner

class higher_lower:
    
    # Declare constants here
    
    def __init__(self): # Initializer function
        # Declare global variables and constants here
        return None

    def foo1(self): # First function template
        return None

    def bar2(self): # Second function template
        return None

    def main(self): # Main app routine

        # Initialize main() variables

        # Clear terminal screen if used
        clear_terminal()

        # Main() logic
        print(app_banner)

        self.foo1() # Call foo() function
        self.bar2() # Call bar() function

        return None

if __name__ == '__main__':
    app = higher_lower()
    app.main()
