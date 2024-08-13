from shared_modules.system_modules import clear_terminal

# Check if leap year function
def is_leap_year(year: int = 0):
    
    # initialize variables
    leap_year_check: bool = False
    
    # calculate and return if year is a leap year
    if year % 400 == 0:
        leap_year_check= True
    elif (year % 4 == 0) and (year % 100 > 0):
        leap_year_check = True   
    
    return leap_year_check


# main() program logic module
def main():

    # clear the terminal screen
    clear_terminal()

    # initialize module variables
    leap_year_check: bool = False
    year_input:      str = ""    

    # mainline statements
    
    # input year to check if a leap year and output response
    year_input = input("Year to check if a leap year: ")
    
    if year_input.isdigit():
        leap_year_check = is_leap_year(int(year_input))
        print(leap_year_check)
    else:
        print("Error: You must enter a valid year number")

    return None

if __name__ == '__main__':
    main()
