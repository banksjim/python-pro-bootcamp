import requests

from shared_modules.system_modules import clear_terminal

# main() program logic module
def main():

    # clear the terminal screen
    clear_terminal()

    # initialize variables
    end_game:    bool = False
    guess:       str = ""
    random_word: str = ""

    # ASCII art variables
    banner:      str = r'''
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
        '  /|\\  |',
        '  /    |',
        '  / \\  |'
    ]

    # mainline statements
    print(banner)

    while not end_game:
        # guess = input("Guess a letter: ")

        # generate a random word via API call
        # response = requests.get('http://random-word-api.herokuapp.com/word?number=1', timeout=5)
        # if response.status_code == 200:
        #     random_word = response.json()[0]
        # else:
        #     print(f'Error: {response.status_code}')

        end_game = True

    return None

if __name__ == '__main__':
    main()
