import os
import sys

# determine terminal type
def get_terminal_type():

    # determine if running Windows
    if sys.platform.startswith('win'):
        return 'Windows'
    else:
        return None

# clear the terminal in either windows or mac/linux
def clear_terminal():

    terminal_type = get_terminal_type()
    if terminal_type == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

    return None
