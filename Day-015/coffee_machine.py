# Coffee machine - Simulation of the software required to operate a coffee dispenser machine

from shared_modules.system_modules import clear_terminal

class coffee_machine:

    # Declare AppOrServiceName constants here

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

        self.foo1() # Call foo() function
        self.bar2() # Call bar() function

        return None

if __name__ == '__main__':
    app = coffee_machine()
    app.main()
