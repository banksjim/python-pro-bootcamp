import requests

from shared_modules.system_modules import clear_terminal

# main() program logic module
def main():

    # clear the terminal screen
    clear_terminal()

    # initialize variables
    end_game:    bool = False
    guess:       str = ""
    hanged_man:  bool = False
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

    # count the number of letters in the random word

    # store the letters of the random word in a list of letters

    # store the partially completed word in a list of letters starting with blanks in each character

    # prompt for guess the first letter letter

    # loop user guesses until the random word is guessed or the hanged man flag is true

        # clear the terminal screen

        # show the partially completed world list with each letter separated by a space

        # user guesses a letter

        # check if the guessed letter is in the word

            # yes - fill the letter in all matching locations of the partially completed word list

                # check if any of the remaining characters are blanks

                    # no - the word was guessed correctly and end game = true

            # no - add a level to the hanged man, and increase the hanged level count

        end_game = True

    return None

if __name__ == '__main__':
    main()
