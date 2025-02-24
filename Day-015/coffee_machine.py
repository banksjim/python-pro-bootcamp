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
        
        # Initialize report_resources() variables
        cash_bin_total: float = 0.00
        
        # Output resource report header
        print('\nResource report')
        print('-------------------')
                    
        # Output current resources from config data
        print(f'Water:    {resources["water"]} ml')
        print(f'Milk:     {resources["milk"]} ml')
        print(f'Coffee:   {resources["coffee"]} g')
        print('-------------------')
        print(f'Cash bin: ${cash_bin_total:0.2f}')
        print(f'{resources["quarters"]:>3} - Quarters')
        print(f'{resources["dimes"]:>3} - Dimes')
        print(f'{resources["nickels"]:>3} - Nickels')
        print(f'{resources["pennies"]:>3} - Pennies')
        print('-------------------')
                    
        # Press any key to continue
        press_any_key_to_continue()
        
        return None

    def confirm_shutdown(self):
        """Perform controlled shutdown"""
        
        # Initialize confirm_shutdown() variables
        confirmation_action:        str = ''
        shutdown_action:            bool = False
        valid_confirmation_request: bool = False
        
        # Loop until valid shutdown confirmation is provided
        while valid_confirmation_request is False:
            
            # Prompt for shutdown confirmation
            confirmation_action = input('\nConfirm shutdown (Y/N)? ').upper()
            
            # Validate shutdown confirmation
            if confirmation_action == 'Y':
                shutdown_action = True
                valid_confirmation_request = True
                print('Shutdown successful...\n')
            elif confirmation_action == 'N':
                shutdown_action = False
                valid_confirmation_request = True                
            else:
                valid_confirmation_request = False           
        
        return shutdown_action

    def display_machine_options(self, menu_selection_error: str = '', \
                                read_only: bool = False, \
                                validated_menu_action: int = 0):
        """Display the current menu selections and error if present. """ \
        """Return the user's menu selection value for validation.""" \
        """Also support optional parameters to display the menu again read-only """ \
        """and with any previous error cleared showing the user's validated selection."""

        # Initialize display_machine_options() variables
        menu_selection: str = ''
        
        # Clear terminal screen if used
        clear_terminal()  
        
        # Show requested action error if present then clear it
        if menu_selection_error != '':
            print(f'{menu_selection_error}\n')                       
    
        # Show user options
        print('Available options:\n')
        print('  1. Order espresso')
        print('  2. Order latte')
        print('  3. Order cappuccino')
        print('  4. Refund change')
        print('  5. Print machine report')
        print('  6. Power down\n')
        
        # Retrieve next action from user, or display user's validated selection
        if read_only is False:
            menu_selection = input('Selection: ')
        else:
            print(f'Selection: {validated_menu_action}')
            menu_selection = ''
    
        return menu_selection

    def validate_user_action(self):
        """Accept and valid requested user action. """ \
        """Return a valid action option."""
        
        # Initialize valid_user_action() variables
        valid_selection:        bool = False
        requested_action:       str = ''
        requested_action_error: str = ''
        validated_action:       int = 0
        
        while valid_selection is False: # Loop until a valid user action is input
        
            # Display available coffee machine options
            requested_action = self.display_machine_options(requested_action_error)
            
            # Clear any previous error message
            requested_action_error = ''
                   
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
        action:                    int = 0
        controlled_power_down:     bool = False
        
        # Main() logic
        while controlled_power_down is False: # Continuously operate while power is on      
            
            # Retrieve next action
            action = self.validate_user_action()     
            
            # Redisplay the menu screen read-only and clear any previous errors 
            self.display_machine_options('', True, action)
            
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
                    self.report_resources()                  
                    
                # Handle controlled power down
                case 6:
                    controlled_power_down = self.confirm_shutdown()                    

        return None

if __name__ == '__main__':
    app = coffee_machine()
    app.main()
