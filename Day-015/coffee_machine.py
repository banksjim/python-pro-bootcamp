# Coffee machine - Simulation of the software required to operate a coffee dispenser machine
from coffee_machine_config_data import menu, resources
from shared_modules.system_modules import clear_terminal, press_any_key_to_continue

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
        valid_selection:        bool = False
        requested_action:       str = ''
        requested_action_error: str = ''
        validated_action:       int = 0
        
        while valid_selection is False: # Loop until a valid user action is input
        
            # Clear terminal screen if used
            clear_terminal()  
            
            # Show requested action error if present then clear it
            if requested_action_error is not '':
                print(f'{requested_action_error}\n')
                requested_action_error = ''                           
        
            # Show user options
            print('Available options:\n')
            print('  1. Order espresso')
            print('  2. Order latte')
            print('  3. Order cappuccino')
            print('  4. Refund change')
            print('  5. Print machine report')
            print('  6. Power down\n')
            
            # Retrieve next action from terminal
            requested_action = input('Selection: ')
            
            # Validate that requested action is numeric
            if requested_action.isdigit():
                
                # validate that requested action is in the valid range
                if int(requested_action) in range(1, 7):
                    validated_action = int(requested_action)
                    valid_selection = True
                else:
                    requested_action_error = 'Error: Request not in valid range'
                    valid_selection = False
                
            else:
                requested_action_error = 'Error: Request must be numeric'
                valid_selection = False          
            
        return validated_action

    def main(self): # Main app routine

        # Initialize main() variables
        action:                int = 0
        controlled_power_down: bool = False
        
        # Main() logic
        while controlled_power_down is False: # Continuously operate while power is on      
            
            # Retrieve next action
            action = self.valid_user_action()      
            
            # Process machine request options               
            match action:
                
                # Handle drink order request
                case 1 | 2 | 3:
                    print('') # placeholder statement
                
                # Handle refund change request
                case 4:
                    print('') # placeholder statement
                    
                # Handle machine report request
                case 5:
                    print('\nResource report:')
                    
                    # Output current resources from config data
                    print(f'Water: {resources["water"]} ml')
                    
                    # Press any key to continue
                    press_any_key_to_continue()                       
                    
                # Handle controlled power down
                case 6:
                    print('') # placeholder statement    

        return None

if __name__ == '__main__':
    app = coffee_machine()
    app.main()
