# AppOrServiceName - Description

from shared_modules.system_modules import clear_terminal

class AppOrServiceName:
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

        
        self.foo1() # Call foo() function
        self.bar2() # Call bar() function        
        
        return None
    
if __name__ == '__main__':
    app_or_service = AppOrServiceName()
    app_or_service.main()
