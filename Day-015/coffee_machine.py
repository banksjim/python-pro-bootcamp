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

    def bar2(self): # Second function template
        return None

    def main(self): # Main app routine

        # Initialize main() variables
        controlled_power_down: bool = False
        
        # Main() logic
        while controlled_power_down is False: # Continuously operate while power is on
        
            # Clear terminal screen if used
            clear_terminal()
        

            # self.report_resources() # Output remaining machine resources
            self.bar2() # Call bar() function

        return None

if __name__ == '__main__':
    app = coffee_machine()
    app.main()
