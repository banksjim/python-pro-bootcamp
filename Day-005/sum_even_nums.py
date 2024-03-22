import os
import sys

# determine terminal type
def get_terminal_type():
    if sys.platform.startswith('win'):
        return 'Windows'
    return None

# main() program logic module
def main():

    # clear the terminal in either windows or mac/linux
    terminal_type = get_terminal_type()
    if terminal_type == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

    # declare variables
    target: int = 0
    sum_even: int = 0

    # input the target ending number from the console
    target = int(input('Enter the ending number: '))

    # only accept input of <= 1000
    if target <= 1000:
    
        # sum the even numbers from 0 to target
        for number in range(0, target + 1, 2):
            sum_even += number

        # print the sum of even numbers
        print(sum_even)    
    else:
        print('Please enter a number less than or equal to 1000')

    return None

if __name__ == '__main__':
    main()
