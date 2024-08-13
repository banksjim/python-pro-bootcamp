from shared_modules.system_modules import clear_terminal
from calc_banner import banner

# add function
def add(num1: float = 0.0, num2: float = 0.0):
    return num1 + num2

# divide() function
def divide(num1: float = 0.0, num2: float = 0.0):
    return num1 / num2

# input_factor function
def input_factor(which_factor: int = 0):
    
    # initialize variables
    factor_counter_string:  str = ""
    factor_input:           str = ""
    factor_input_error:     str = "Error: Invalid number input"
    factor_input_is_digit:  bool = False
    valid_factor:           float = 0.0
    
    # loop until a valid floating point number is input
    while factor_input_is_digit is False: 
    
        # set factor counter string
        if which_factor == 1: 
            factor_counter_string = "First"
        elif which_factor == 2:
            factor_counter_string = "Second"
        else:
            factor_counter_string = "Error: Invalid"
    
        # request input value for factors
        factor_input = input(f"{factor_counter_string} number: ").strip()

        # check that factor_input is numeric and error if not
        factor_input_is_digit = factor_input.isdigit()

        # assign and return valid_factor value or output error
        if factor_input_is_digit is True:    
            valid_factor = float(factor_input)   
            return valid_factor
        else:
            print(factor_input_error)
            
# input_operation function
def input_operation():
    
    # initialize variables
    operation_error:       str = "Error: Invalid operation"
    operation_input:       str = ""
    operation_input_valid: bool = False
    
    operation_name = None
    
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        "%": modulus
    }
    
    # loop until a valid and supported math operation is input
    while operation_input_valid is False:

        # request math operation input
        operation_input = input("Choose math operation (+,-,*,/,%): ").strip()

        # check for valid operation name
        operation_name = operations.get(operation_input, operation_error)

        if operation_name != operation_error:
            operation_input_valid = True
            return operation_input, operation_name
        else:
            print(operation_error)

# modulus() function
def modulus(num1: float = 0.0, num2: float = 0.0):
    return num1 % num2

# multiply() function
def multiply(num1: float = 0.0, num2: float = 0.0):
    return num1 * num2

# subtract() function
def subtract(num1: float = 0.0, num2: float = 0.0):
    return num1 - num2

# main() program logic module
def main():

    # initialize module variables
    factor1:           float = 0.0
    factor2:           float = 0.0
    formatted_result:  float = 0.0
    operation_symbol:  str = ""
    result:            float = 0.0
    user_option:       str = "n"
    user_option_error: str = "Error: Invalid option provided"     
    
    operation = None

    # mainline statements

    # Loop program logic until user selects the e"x"it option
    while user_option != "x" :  # 'x' -> exit program

        # take action on the program's user_option 
        if user_option == "n":  # 'n' -> new calculation
        
            # clear input variables, clear screen, and print banner for new calculations
            clear_terminal()
    
            # print app banner
            print(banner)
            
            # reset factor1 and factor2
            factor1 = 0.0
            factor2 = 0.0
            
            # input factor1
            factor1 = input_factor(1)

        elif user_option == "y":  # 'y' -> reuse previous result as factor1 value
            
            # assign previous result to factor1
            factor1 = result
            
            # output the first number in the equation for transparency to the user
            print(f"First number: {factor1}")
            
        # continue with math expression and result when user_option is "n" or "y"
        if user_option == "n" or user_option == "y":
            
            # input math operation
            operation_symbol, operation = input_operation()
            
            # input factor2
            factor2 = input_factor(2)
            
            # calculate result
            result = operation(factor1, factor2)
            
            # format the result to remove trailing zeros after the first zero following the decimal
            formatted_result = f"{result:.5f}"
            if "." in formatted_result:
                formatted_result = formatted_result.rstrip("0")
                if formatted_result[-1] == ".":
                    formatted_result += "0"            
            
            # output the complete math expression and result
            print(f"{factor1} {operation_symbol} {factor2} = {formatted_result}\n")
            
        # ask for user_input to continue
        user_option = input(
            f"Type 'y' to continue calculating with {formatted_result}, "
            "type 'n' to start a new calculation, "
            "or 'x' to exit: ").strip().lower()
    
        # check user_option response and notify if input error
        if user_option not in ('y', 'n', 'x'):
            print(user_option_error)
        else:
            print("\n")  # print a blank line for separation

    return None

if __name__ == '__main__':
    main()
