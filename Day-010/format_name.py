from shared_modules.system_modules import clear_terminal

# format_name() function
def format_name(first_name: str = "", last_name: str = ""):
    
    # function variables
    formatted_name: str = ""
    
    # change function input variables to titles
    formatted_name = f"{first_name.title()} {last_name.title()}"
    
    return formatted_name

# main() program logic module
def main():

    # clear the terminal screen
    clear_terminal()

    # initialize module variables
    first_name_input: str = ""
    last_name_input:  str = ""
    full_name:        str = ""
    
    # mainline statements

    # input first and last names
    first_name_input = input("First name: ")
    last_name_input = input("Last name:  ")
    
    # Convert input names to title case and output
    full_name = format_name(first_name_input, last_name_input)
    print(f"\nFormatted name: {full_name}")

    return None

if __name__ == '__main__':
    main()
