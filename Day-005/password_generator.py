import os
import random
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
    num_letters:          int = 0
    user_password:        str = ""

    # declare static lists

    # list of letters with both upper and lower case letters
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # list of symbols
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+',
               '=', '[', ']', '{', '}', ';', ':', '<', '>', ',', '.', '/', '?', '|']

    # list of numbers
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # list used to build user password
    build_password = []

    # main program logic

    # display banner
    print('Welcome to the PyPassword Generator!')

    # input user constraints for the password
    num_letters = int(input('How many letters would you like in your password?\n'))
    num_symbols = int(input('How many symbols would you like?\n'))
    num_numbers = int(input('How many numbers would you like?\n'))

    # calculate the password

    # populate symbols in build_password
    for index in range(0, num_symbols):
        build_password.append(random.choice(symbols))

    # populate numbers in build_password
    for index in range(0, num_numbers):
        build_password.append(random.choice(numbers))

    # populate letters in build_password
    for index in range(0, num_letters - (num_symbols + num_numbers)):
        build_password.append(random.choice(letters))

    # shuffle the characters to be used in the user's password
    random.shuffle(build_password)

    # print the final password
    for char in build_password:
        user_password += str(char)

    print(f'Here is your password: {user_password}')

    return None

if __name__ == '__main__':
    main()
