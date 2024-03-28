from shared_modules.system_modules import clear_terminal

# main() program logic module
def main():

    # clear the terminal screen
    clear_terminal()

    # initialize variables
    end_game: bool = False
    guess:    str = ""

    # ASCII art variables
    banner:   str = r'''
    .__                                                 
    |  |__ _____    ____    ____   _____ _____    ____  
    |  |  \\__  \  /    \  / ___\ /     \\__  \  /    \ 
    |   Y  \/ __ \|   |  \/ /_/  >  Y Y  \/ __ \|   |  \
    |___|  (____  /___|  /\___  /|__|_|  (____  /___|  /
         \/     \/     \//_____/       \/     \/     \/ 
    '''

    # initialize lists
    empty_gallows = [
        '   +---+',
        '   |   |',
        '       |',
        '       |',
        '       |',
        '       |',
        '=========='
    ]
    
    hanged_man = [
        '   O   |',
        '   |   |',
        '  /|   |',
        '  /|\  |',
        '  /    |',
        '  / \  |'
    ]

    # mainline statements
    print(banner)

    while not end_game:
        guess = input("Guess a letter: ")

    return None

if __name__ == '__main__':
    main()
