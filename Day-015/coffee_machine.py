# Coffee machine - Simulation of the software required to operate a coffee dispenser machine

from shared_modules.system_modules import clear_terminal

class coffee_machine:

    # Declare AppOrServiceName constants here

    def __init__(self): # Initializer function
        # Declare global variables and constants here
        return None

    def report_resources(self):
        """On-demand output of current remaining machine resources"""
        return None

    def valid_user_action(self):
        """Accept and valid requested user action. Return a valid action option."""
        
        # Initialize valid_user_action() variables
        user_action: int = 0
        
        return user_action

    def main(self): # Main app routine

        # Initialize main() variables
        action:                int = 0
        controlled_power_down: bool = False
        
        # Main() logic
        while controlled_power_down is False: # Continuously operate while power is on
        
            # Clear terminal screen if used
            clear_terminal()
        
            # Show user options
            print('Available options:\n')
            print('  1. Order espresso')
            print('  2. Order latte')
            print('  3. Order cappuccino')
            print('  4. Print machine report')
            print('  5. Power down\n')
            
            # Request and validate next action
            action = self.valid_user_action()
        

            # self.report_resources() # Output remaining machine resources
            self.bar2() # Call bar() function

        return None

if __name__ == '__main__':
    app = coffee_machine()
    app.main()
