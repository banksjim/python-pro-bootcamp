from shared_modules.system_modules import clear_terminal

# check and report if a number is prime
def prime_checker(number: int = 0):
    # initialize variables
    denominator: int = 2
    is_prime:    bool = True
    remainder:   float = 0

    # check for prime
    if (number >= 1) and (number <= 100):

        # 1 is not a prime number
        if number == 1:
            is_prime = False

        # check for non-prime number
        while (denominator < number) and (is_prime is True):
            remainder = number % denominator
            if remainder == 0:
                is_prime = False
            denominator += 1

        # output results
        if is_prime is True:
            print('It\'s a prime number.')
        else:
            print('It\'s not a prime number.')

    else:
        print('This program only supports numbers between 1 and 100')

    return None

# main() program logic module
def main():

    # clear the terminal screen
    clear_terminal()

    # initialize module variables
    n: int = 0

    # mainline statements
    print('Check if a number is prime\n')
    n = int(input('Enter a number to check for prime: ')) # Check this number
    prime_checker(number=n)

    return None

if __name__ == '__main__':
    main()
