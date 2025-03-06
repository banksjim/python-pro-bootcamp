# Coffee machine - Simulation of the software required to operate a coffee dispenser machine

from coffee_machine_config_data import menu, resources
from shared_modules.system_modules import clear_terminal, press_any_key_to_continue

class coffee_machine:

    # Declare AppOrServiceName constants here

    def __init__(self): # Initializer function
        # Declare global variables and constants here
        return None          

    def check_ingredients(self, drink_requested_option: int = 0, \
                                machine_coffee: float = 0.0,
                                machine_milk: float = 0.0,
                                machine_water: float = 0.0):
        """Receive the option selected by the user for a specific drink and """ \
        """the remaining machine ingredients. Check the ingredients available for that drink. """ \
        """Return flag signaling if the drink has the required ingredients remaining """ \
        """in the machine. If enough ingredients were available also return the  """ \
        """ingredient amounts to deduct after order."""
        
        # Initialize check_ingredients() variables
        drink_type:          str = ''
        ingredients_missing: str = ''
        required_coffee:     float = 0.0
        required_milk:       float = 0.0
        required_water:      float = 0.0
        unfillable_order:    bool = False
        
        # Load ingredients required for the user's drink selection
        match drink_requested_option:
            
            # Set the drink type ordered value
            case 1: # Espresso order
                drink_type = 'espresso'
            case 2: # Latte order
                drink_type = 'latte'
            case 3: # 
                drink_type = 'cappuccino'
                
        # Lookup the required ingredients for the selected drink              
        required_coffee = menu[drink_type]["ingredients"]["coffee"]
        required_milk   = menu[drink_type]["ingredients"]["milk"]
        required_water  = menu[drink_type]["ingredients"]["water"]
        
        # Determine if there are enough ingredients for the drink
        if machine_coffee < required_coffee:
            unfillable_order = True
            ingredients_missing += 'coffee '
        
        if machine_milk < required_milk:
            unfillable_order = True
            ingredients_missing += 'milk '
            
        if machine_water < required_water:
            unfillable_order = True
            ingredients_missing += 'water '
            
        # If drink order cannot be filled zero out all required ingredients
        if unfillable_order is True:
            required_coffee = 0
            required_milk   = 0
            required_water  = 0
        
        return unfillable_order, required_coffee, required_milk, required_water

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

    def deposit_currency(self):
        """"""
        
        # Initialize deposit_currency() variables
        total_deposited:    float = 0.0
        
        quarters_deposited: int = 0
        dimes_deposited:    int = 0
        nickels_deposited:  int = 0
        pennies_deposited:  int = 0
        
        # Clear terminal screen if used
        clear_terminal()
        
        # Accept coin deposits for purchase
        print('Insert coins...\n')               
        
        # Accept and count coins for supported currency types
        quarters_deposited = self.get_coins('quarters')
        dimes_deposited    = self.get_coins('dimes')
        nickels_deposited  = self.get_coins('nickels')
        pennies_deposited  = self.get_coins('pennies')
        
        return total_deposited, quarters_deposited, dimes_deposited, \
            nickels_deposited, pennies_deposited

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

    def get_coins(self, currency_unit: str = ''):
        """Input number of coins for requested current type. """ \
        """Return number of coins input for the currency type requested."""
    
        # Initialize get_coins() function variables
        coin_count:         int = 0
        coin_slot_counter:  str = ''
        valid_coin_deposit: bool = False
        
        # Loop until until a valid number is provided for coin_slot_counter
        while valid_coin_deposit is False:
        
            # Fetch currency type from coin_slot
            coin_slot_counter = input(f'Number of {currency_unit}: ')
            
            # Validate that the coin slot returned numeric count of the coin type
            if coin_slot_counter.isdigit():
                coin_count = int(coin_slot_counter)
                valid_coin_deposit = True
            else: 
                print(f'Error: Invalid number of {currency_unit} provided')
        
        return coin_count                  

    def report_resources(self):
        """On-demand output of current remaining machine resources"""
        
        # Initialize report_resources() variables
        cash_bin_total: float = 0.00
        
        # Calculate the cash_bin total
        cash_bin_total = self.total_currency(resources["USD_quarters"], \
                                             resources["USD_dimes"],
                                             resources["USD_nickels"],
                                             resources["USD_pennies"])
        
        # Output resource report header
        print('\nResource report')
        print('-------------------')
                    
        # Output current resources from config data
        print(f'Water:    {resources["water"]} ml')
        print(f'Milk:     {resources["milk"]} ml')
        print(f'Coffee:   {resources["coffee"]} g')
        print('-------------------')
        print(f'Cash bin: ${cash_bin_total:0.2f}')
        print(f'{resources["USD_quarters"]:>3} - Quarters')
        print(f'{resources["USD_dimes"]:>3} - Dimes')
        print(f'{resources["USD_nickels"]:>3} - Nickels')
        print(f'{resources["USD_pennies"]:>3} - Pennies')
        print('-------------------')
                    
        # Press any key to continue
        press_any_key_to_continue()
        
        return None
    
    def total_currency(self, quarters: int = 0, \
                             dimes: int = 0,\
                             nickels: int = 0, \
                             pennies: int = 0):
        """Receive currency type counts and calculate the total currency"""

        # Initialize total_currency() function variables
        total_currency: float = 0.00
        
        # Calculate sum total of all coins 
        total_currency += quarters * resources["USD_quarters_value"] # Add total for all quarters
        total_currency += dimes * resources["USD_dimes_value"] # Add total for all dimes
        total_currency += nickels * resources["USD_nickels_value"] # Add total for all nickels
        total_currency += pennies * resources["USD_pennies_value"] # Add total for all pennies
    
        return total_currency

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
        action:                int = 0
        coin_slot_counter:     str = ''
        coin_slot_error:       bool = False
        controlled_power_down: bool = False
        
        coffee_use:            float = 0.0
        milk_use:              float = 0.0
        water_use:             float = 0.0
        
        deposited_quarters:    int = 0
        deposited_dimes:       int = 0
        deposited_nickels:     int = 0
        deposited_pennies:     int = 0
        ingredient_shortage:   bool = False
        
        remaining_coffee:      float = 0.0
        remaining_milk:        float = 0.0
        remaining_water:       float = 0.0
        
        remaining_quarters:    int = 0
        remaining_dimes:       int = 0
        remaining_nickels:     int = 0
        remaining_pennies:     int = 0
        
        # Main() logic
        
        # Load available resources from machine config
        remaining_coffee   = resources["coffee"]
        remaining_milk     = resources["milk"]
        remaining_water    = resources["water"]
        
        remaining_quarters = resources["USD_quarters"]
        remaining_dimes    = resources["USD_dimes"]
        remaining_nickels  = resources["USD_nickels"]
        remaining_pennies  = resources["USD_pennies"]
        
        # Accept user requests until powered down
        while controlled_power_down is False: # Continuously operate while power is on      
            
            # Accept coin deposits for purchase
            total_deposited, deposited_quarters, deposited_dimes, \
                deposited_nickels, deposited_pennies = self.deposit_currency()
            
            # Retrieve user selection
            action = self.validate_user_action()     
            
            # Redisplay the menu screen read-only and clear any previous errors 
            self.display_machine_options('', True, action)
            
            # Process machine request options               
            match action:
                
                # Handle drink order request
                case 1 | 2 | 3:
                    
                    # Confirm that ingredients required are available and
                    # return ingredients that will be used if the order can be filled
                    ingredient_shortage, coffee_use, milk_use, water_use = \
                        self.check_ingredients(action, remaining_coffee, remaining_milk, \
                                               remaining_water)
                    
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
