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

    # initialize variables
    banner: str = r'''
    .__                                                 
    |  |__ _____    ____    ____   _____ _____    ____  
    |  |  \\__  \  /    \  / ___\ /     \\__  \  /    \ 
    |   Y  \/ __ \|   |  \/ /_/  >  Y Y  \/ __ \|   |  \
    |___|  (____  /___|  /\___  /|__|_|  (____  /___|  /
         \/     \/     \//_____/       \/     \/     \/ 
    '''
    
    # mainline routine
    print(banner)

    return None

if __name__ == '__main__':
    main()
