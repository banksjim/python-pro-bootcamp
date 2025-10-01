# Coffee machine - Simulation of the software required to operate a coffee dispenser machine

from coffee_machine_config_data import menu, resources
from shared_modules.system_modules import clear_terminal, press_any_key_to_continue

class coffee_machine:

    # Declare AppOrServiceName constants here

    def __init__(self): # Initializer function
        # Declare global variables and constants here
        return None          

    def check_ingredients(self, drink_ordered: str = '', \
                                machine_coffee: float = 0.0,
                                machine_milk: float = 0.0,
                                machine_water: float = 0.0):
        """Receive the drink ordered name as selected by the user and the remaining """ \
        """machine ingredients. Check the ingredients available for that drink. """ \
        """Return flag signaling if the drink has the required ingredients remaining """ \
        """in the machine. If enough ingredients were available also return the  """ \
        """ingredient amounts to deduct after order."""
        
        # Initialize check_ingredients() variables
        ingredients_missing: str = ''
        required_coffee:     float = 0.0
        required_milk:       float = 0.0
        required_water:      float = 0.0
        unfillable_order:    bool = False       
                
        # Lookup the required ingredients for the selected drink              
        required_coffee = menu[drink_ordered]["ingredients"]["coffee"]
        required_milk   = menu[drink_ordered]["ingredients"]["milk"]
        required_water  = menu[drink_ordered]["ingredients"]["water"]
        
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
        
        return unfillable_order

    def deposit_coins(self, total_deposited: float = 0.0, dispenser_message: str = ''):
        """Accept coin deposits by the user. """ \
        """Return updated total deposited amount number of coins deposited by currency type."""
        
        # Initialize deposit_currency() function variables
        quarters_deposited: int = 0
        dimes_deposited:    int = 0
        nickels_deposited:  int = 0
        pennies_deposited:  int = 0
               
        # Clear terminal screen
        clear_terminal()
                      
        # Show total deposited
        print(f'Total deposited: ${total_deposited:0.2f}\n')
        
        # Show total deposited and dispenser message if not blank
        if dispenser_message != '':
            print(f'{dispenser_message}\n')
        
        # Accept coin deposits
        print('Insert coins...\n')               
        
        # Accept and count coins for supported currency types
        quarters_deposited += self.get_coins('quarters')
        dimes_deposited    += self.get_coins('dimes')
        nickels_deposited  += self.get_coins('nickels')
        pennies_deposited  += self.get_coins('pennies')
               
        # Calculate the amount deposited based on the coins inserted        
        total_deposited += quarters_deposited * resources["USD_quarters_value"]
        total_deposited += dimes_deposited    * resources["USD_dimes_value"]
        total_deposited += nickels_deposited  * resources["USD_nickels_value"]
        total_deposited += pennies_deposited  * resources["USD_pennies_value"]      
        
        return total_deposited, quarters_deposited, dimes_deposited, \
                                nickels_deposited, pennies_deposited

    def display_machine_options(self, menu_selection_message: str = '', \
                                read_only: bool = False, \
                                validated_menu_action: int = 0, \
                                total_deposited: float = 0.0):
        """Display the current menu selections and error if present. """ \
        """Return the user's menu selection value for validation.""" \
        """Support an optional parameters to display the menu again read-only """ \
        """with any previous error cleared showing the user's validated selection.""" \
        """Receive and show the current total deposited amount."""

        # Initialize display_machine_options() variables
        menu_selection: str = ''
        
        # Clear terminal screen if used
        clear_terminal()  
               
        # Show current deposited amount
        print(f'Total deposited: ${total_deposited:0.2f}\n')
        
        # Show requested action error if present then clear it
        if menu_selection_message != '':
            print(f'{menu_selection_message}\n')                       
    
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
        """Return number of coins deposited by currency type."""
    
        # Initialize get_coins() function variables
        coin_count:         int = 0
        coin_slot_counter:  str = ''
        valid_coin_deposit: bool = False
        
        # Loop until until a valid number is provided for coin_slot_counter
        while valid_coin_deposit is False:
        
            # Fetch currency type from coin_slot
            coin_slot_counter = input(f'Number of {currency_unit} inserted: ')
            
            # Validate that the coin slot returned numeric count of the coin type
            if coin_slot_counter.isdigit():
                coin_count = int(coin_slot_counter)
                valid_coin_deposit = True
            else: 
                print(f'Error: Invalid number of {currency_unit} provided')
        
        return coin_count                  

    def get_drink_description(self, drink_requested_option: int = 0):
        # Initialize function variables
        drink_name: str = ''
    
        # Set the drink type ordered value
        match drink_requested_option:
            
            case 1: # Espresso order
                drink_name = 'espresso'
            case 2: # Latte order
                drink_name = 'latte'
            case 3: # 
                drink_name = 'cappuccino'
    
        return drink_name

    def refund_change(self, amount: float = 0.0, \
                            deposited_quarters: int = 0, \
                            deposited_dimes: int = 0, \
                            deposited_nickels: int = 0, \
                            deposited_pennies: int = 0):
        """Handle refund of unused coin deposits.""" \
        """Accept in the current total deposit amount and number of coins by currency type. """ \
        """Return a zeroed out total deposit value."""
        
        # Show user any refunded coin deposits with total returned
        print(f'\nRefund amount ${amount:0.2f}')
        print('-------------------------')
        print(f'- Number of quarters: {deposited_quarters}')
        print(f'- Number of dimes:    {deposited_dimes}')
        print(f'- Number of nickels:  {deposited_nickels}')
        print(f'- Number of pennies:  {deposited_pennies}')
        
        # Zero out total deposited and coin counts
        amount             = 0
        deposited_quarters = 0
        deposited_dimes    = 0
        deposited_nickels  = 0
        deposited_pennies  = 0        
        
        return amount, deposited_quarters, deposited_dimes, \
                       deposited_nickels, deposited_pennies

    def report_resources(self, coffee: float = 0.0, milk: float = 0.0, water: float = 0.0, \
                               quarters: int = 0, dimes: int=0, nickels: int = 0, pennies: int = 0):
        """On-demand output of current remaining machine resources"""
        
        # Initialize report_resources() variables
        cash_bin_total: float = 0.00
        
        # Calculate the cash_bin total
        cash_bin_total = self.total_currency(quarters, dimes, nickels, pennies)
        
        # Output resource report header
        print('\nResource report')
        print('-------------------')
                    
        # Output current resources from config data
        print(f'Coffee: {coffee:.1f} g')
        print(f'Milk:   {milk:.1f} ml')
        print(f'Water:  {water:.1f} ml')
        print('-------------------')
        print(f'Cash bin: ${cash_bin_total:0.2f}')
        print(f'{quarters:>3} - Quarters')
        print(f'{dimes:>3} - Dimes')
        print(f'{nickels:>3} - Nickels')
        print(f'{pennies:>3} - Pennies')
        print('-------------------')
                    
        # Press any key to continue
        press_any_key_to_continue()
        
        
        return None
    
    def shutdown(self, amount_deposited: float = 0.0, \
                       deposited_quarters: int = 0, \
                       deposited_dimes: int = 0, \
                       deposited_nickels: int = 0, \
                       deposited_pennies: int = 0):
        """Perform controlled shutdown and refund any existing deposit amount.""" \
        """Return whether or now the shutdown was successfully confirmed."""
        
        # Initialize confirm_shutdown() variables
        confirmation_action:        str = ''
        shutdown_action:            bool = False
        valid_confirmation_request: bool = False
        
        # Loop until valid shutdown confirmation is provided
        while valid_confirmation_request is False:
            
            # Prompt for shutdown confirmation
            confirmation_action = input('\nConfirm shutdown (y/n)? ').upper()
            
            # Validate shutdown confirmation
            if confirmation_action == 'Y':
                shutdown_action = True
                valid_confirmation_request = True
                
                # Refund any deposited coins that were not used
                # TODO: Complete refund display logic during shutdown 
                if amount_deposited > 0:
                    self.refund_change(amount_deposited, deposited_quarters, \
                                       deposited_dimes, deposited_nickels, \
                                       deposited_pennies)
                
                print('\nShutdown successful...')
            elif confirmation_action == 'N':
                shutdown_action = False
                valid_confirmation_request = True                
            else:
                valid_confirmation_request = False           
        
        return shutdown_action
    
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
 
    def handle_user_selection(self, total_deposited: float = 0.0, \
                                   dispenser_message: str = ''):
        """Accept and valid requested user action. """ \
        """Return a valid action option.""" \
        """Receive and pass along the current total deposited amount."""
        
        # Initialize valid_user_action() variables
        valid_selection:          bool = False
        requested_action:         str = ''
        requested_action_message: str = ''
        validated_action:         int = 0
        
        while valid_selection is False: # Loop until a valid user action is input
        
            # Initialize requested action message to the dispenser message if provided
            if dispenser_message:
                requested_action_message = dispenser_message
        
            # Display available coffee machine options
            requested_action = self.display_machine_options(requested_action_message, \
                                                            False, 0, total_deposited)
            
            # Clear any previous dispenser or error message
            dispenser_message = ''
            requested_action_message = ''
                   
            # Validate that requested action is numeric
            if requested_action.isdigit():
                
                # validate that requested action is in the valid range
                if int(requested_action) in range(1, 7):
                    validated_action = int(requested_action)
                    valid_selection = True
                else:
                    requested_action_message = 'Error: Request not in valid range'
                    valid_selection = False
                
            else:
                requested_action_message = 'Error: Request must be numeric'
                valid_selection = False          
            
        return validated_action

    def main(self): # Main app routine

        # Initialize main() variables
        action:                int = 0
        refund_amount:         float = 0.0
        controlled_power_down: bool = False
        dispenser_message:     str = ''
        drink_ordered:         str = ''
        ingredient_shortage:   bool = False     
        total_deposited:       float = 0.0
        
        # Variables to track ingredients in machine
        machine_coffee:        float = 0.0
        machine_milk:          float = 0.0
        machine_water:         float = 0.0
        
        # Variables to track coins in the machine cash bin
        bin_quarters:          int = 0
        bin_dimes:             int = 0
        bin_nickels:           int = 0
        bin_pennies:           int = 0
        
        # Variables to track coins inserted for purchase
        deposited_quarters:    int = 0
        deposited_dimes:       int = 0
        deposited_nickels:     int = 0
        deposited_pennies:     int = 0
        
        # Main() logic
        
        # Load available resources from machine config
        machine_coffee = resources["coffee"]
        machine_milk   = resources["milk"]
        machine_water  = resources["water"]
        
        bin_quarters = resources["USD_quarters"]
        bin_dimes    = resources["USD_dimes"]
        bin_nickels  = resources["USD_nickels"]
        bin_pennies  = resources["USD_pennies"]
        
        # Accept user requests until powered down
        while controlled_power_down is False: # Continuously operate while power is on      
            
            # Accept coin deposits for purchase only if more funds are needed for an order and
            # no ingredient shortage for an order has been found

            if (total_deposited == 0) or (refund_amount < 0): # Check if more funds needed
                if ingredient_shortage is False: # And no ingredient shortages
                    total_deposited, deposited_quarters, deposited_dimes, \
                    deposited_nickels, deposited_pennies = self.deposit_coins(total_deposited, dispenser_message) # Add dispenser message to the deposit_coins() function        

            # Add deposited coins to the cash bin
            bin_quarters += deposited_quarters
            bin_dimes    += deposited_dimes
            bin_nickels  += deposited_nickels
            bin_pennies  += deposited_pennies
            
            # Reset deposited coins from previous deposit
            deposited_quarters = 0
            deposited_dimes    = 0
            deposited_nickels  = 0
            deposited_pennies  = 0
            
            # Retrieve user selection
            action = self.handle_user_selection(total_deposited, dispenser_message)     
            
            # Redisplay the menu screen read-only and clear any previous errors 
            self.display_machine_options('', True, action, total_deposited)
            
            # Process machine request options               
            match action:
                
                # Handle drink order request
                case 1 | 2 | 3:
                    
                    # Set the name of the drink ordered
                    drink_ordered = self.get_drink_description(action)
                    
                    # Confirm that ingredients required are available and
                    # return ingredients that will be used if the order can be filled
                    ingredient_shortage = self.check_ingredients(drink_ordered, machine_coffee, \
                                              machine_milk, machine_water)  
                        
                    # Clear the order dispenser message
                    dispenser_message = ''
                    
                    # If enough machine ingredients then continue to try to fill order
                    # else inform user the drink is temporarily unavailable 
                    if ingredient_shortage is False: # Machine has enough ingredients to fill order
                        
                        # Calculate amount owed or to be refunded
                        refund_amount = total_deposited - menu[drink_ordered]["cost"]
                        
                        # Process order or request additional funds
                        if refund_amount >= 0.0: # Credit balance deposited
                            
                            # Show default dispenser message
                            dispenser_message = f'Here is your {drink_ordered}. '
                            
                            # Append dispenser message uniquely for refund owed or exact change
                            if refund_amount == 0.0:
                                dispenser_message += 'Thanks for using exact change.'
                            else:
                                dispenser_message += f'Returning ${refund_amount:.2f}.'
                                ### Refund change here
                        
                            # Update current machine resources
                            machine_coffee -= menu[drink_ordered]["ingredients"]["coffee"]
                            machine_milk -= menu[drink_ordered]["ingredients"]["milk"]
                            machine_water -= menu[drink_ordered]["ingredients"]["water"]
                        
                        else:
                            
                            dispenser_message = f'Additional ${abs(refund_amount):.2f} needed for {drink_ordered}'                         
                            
                    else:
                        dispenser_message = 'Error: Selection unavailable until machine refilled'
                    
                # Handle refund change request
                case 4:
                    # Refund deposited amounts by currency type
                    total_deposited, deposited_quarters, deposited_dimes, \
                        deposited_nickels, deposited_pennies = \
                            self.refund_change(total_deposited, deposited_quarters, \
                                               deposited_dimes, deposited_nickels, \
                                               deposited_pennies)
                    
                    
                    
                    # Press any key to continue
                    press_any_key_to_continue()
                    
                # Handle machine report request
                case 5:
                    self.report_resources(machine_coffee, machine_milk, machine_water, \
                                          bin_quarters, bin_dimes, bin_nickels, \
                                          bin_pennies)                  
                    
                # Handle controlled power down
                case 6:
                    controlled_power_down = self.shutdown(total_deposited, \
                                                          deposited_quarters, \
                                                          deposited_dimes, \
                                                          deposited_nickels, \
                                                          deposited_pennies)               

        return None

if __name__ == '__main__':
    app = coffee_machine()
    app.main()
