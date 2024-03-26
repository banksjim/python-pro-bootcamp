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

    # my custom function
    def my_function(an_integer: int):
        print("Hello")
        print("Bye")
        print(f"{an_integer}")

    # invoke my custom function
    my_function(15)    

    return None

if __name__ == '__main__':
    main()
