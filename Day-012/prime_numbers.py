from shared_modules.system_modules import clear_terminal

def is_prime(num):  
    
    if num > 1:
        for smaller_num in range((num - 1), 0, -1):
            if smaller_num == 1:
                return True
            elif (num % smaller_num) == 0:
                return False
    else:
        return False
        
# main() program logic module
def main():

    # initialize module variables
    check_again:     str = 'n'
    is_prime_number: bool = False
    number:          int = 0

    # clear the terminal screen
    clear_terminal()
    
    # input number
    number = int(input('Input an integer to evaluate as a prime: '))
    
    # test number
    is_prime_number = is_prime(number)
    
    # output result
    if is_prime_number is True:
        print(f'\n{number} is a prime number')
    else:
        print(f'\n{number} is NOT a prime number')
        
    # ask to test another number
    check_again = input('\nTest another number (y/n)? ')
    if check_again == 'y':
        main()

    return None

if __name__ == '__main__':
    main()
