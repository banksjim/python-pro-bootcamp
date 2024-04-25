import requests

from shared_modules.system_modules import clear_terminal

# main() program logic module
def main():

    play_again: str = "y"

    banner:     str = r'''
    .__                                                 
    |  |__ _____    ____    ____   _____ _____    ____  
    |  |  \\__  \  /    \  / ___\ /     \\__  \  /    \ 
    |   Y  \/ __ \|   |  \/ /_/  >  Y Y  \/ __ \|   |  \
    |___|  (____  /___|  /\___  /|__|_|  (____  /___|  /
         \/     \/     \//_____/       \/     \/     \/ 
    '''

    hanged_man = [
        '   O   |',
        '  /|   |',
        '  /|\\  |',
        '  /    |',
        '  / \\  |'
    ]

    while play_again == 'y':

        found_count:   int = 0
        gallows_level: int = 2
        game_over:     bool = False
        guess:         str = ""
        hanged_level:  int = 0
        random_word:   str = ""
        response:      str = ""
        winner:        bool = False

        # initialize lists
        guessed_word = []

        # initialize the gallows
        gallows = [
            '   +---+',
            '   |   |',
            '       |',
            '       |',
            '       |',
            '       |',
            '=========='
        ]

        clear_terminal()
        print(banner)

        response = requests.get('http://random-word-api.herokuapp.com/word?number=1', timeout=5)
        if response.status_code == 200:
            random_word = response.json()[0]
            random_word = random_word.lower()
        else:
            print('Could not generate a random word.')
            print(f'Error: {response.status_code}')
            game_over = True

        hanged_level = 0

        while not game_over:

            letter_count = len(random_word)
            guessed_word = ['_'] * len(random_word)

            while (winner is False) and (game_over is False):

                guess = input("\nGuess a letter: ").lower()
                found_count = 0

                for idx, letter in enumerate(random_word):

                    if guess == letter:
                        guessed_word[idx] = guess
                        found_count += 1

                if found_count == 0:

                    if (hanged_level <= 1) or (hanged_level == 3):
                        gallows[gallows_level] = hanged_man[hanged_level]
                        gallows_level += 1

                    elif (hanged_level == 2) or (hanged_level == 4):
                        gallows[gallows_level - 1] = hanged_man[hanged_level]

                        if hanged_level == 4:
                            winner = False
                            game_over = True

                    if hanged_level < 4:
                        hanged_level += 1

                else:

                    if '_' not in guessed_word:
                        winner = True
                        game_over = True

                clear_terminal()
                print()

                for char in guessed_word:
                    print(char, end=' ')

                if winner is True:
                    print('\nJustice has saved you. You win!\n')

                elif (winner is False) and (game_over is True):
                    print('\nYou\'ve been hanged partner! You lose.\n')
                    print(f'The word was \'{random_word}\'.\n')

                elif found_count > 0:

                    if found_count == 1:
                        print(f'\n\nYou guessed \'{guess}\'. '
                              f'It appears in the word {found_count} time.\n')
                    else:
                        print(f'\n\nYou guessed \'{guess}\'. '
                              f'It appears in the word {found_count} times.\n')

                else:
                    print(f'\n\nYou guessed \'{guess}\'. '
                          'That\'s not in the word. One step closer to death.\n')

                for idx, level in enumerate(gallows):
                    print(level)

        play_again = input('\nPlay again (y/n)? ').lower()

    return None

if __name__ == '__main__':
    main()
