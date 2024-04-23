import requests

from shared_modules.system_modules import clear_terminal

# main() program logic module
def main():

    # initialize static variables
    play_again: str = "y"

    # ASCII art variables
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

    # mainline statements

    # repeat until user chooses not to play_again
    while play_again == 'y':

        # clear the terminal screen
        clear_terminal()

        # initialize game-specific variables
        found_count:   int = 0
        gallows_level: int = 2
        game_over:     bool = False
        guess:         str = ""
        hanged_level:  int = 0
        letter_count:  int
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

        print(banner)

        # generate a random word via API call
        response = requests.get('http://random-word-api.herokuapp.com/word?number=1', timeout=5)
        if response.status_code == 200:
            random_word = response.json()[0]
            random_word = random_word.lower()
        else:
            print('Could not generate a random word.')
            print(f'Error: {response.status_code}')
            game_over = True

        # set hanged_level to zero
        hanged_level = 0

        while not game_over:

            # count the number of letters in the random_word
            letter_count = len(random_word)

            # initialize a guessed_word list with '_''s for the user's guess of the word
            guessed_word = ['_'] * len(random_word)

            # loop until the random_word is guessed or the hanged man flag is true
            while (winner is False) and (game_over is False):

                # prompt to guess the first letter letter
                guess = input("\nGuess a letter: ").lower()

                # set found_count to zero
                found_count = 0

                # loop to check if the guess letter is in the word and count how many times
                for idx in range(0, letter_count - 1):

                    # compare the guess to the random_word list in the current idx position
                    if guess == random_word(idx):

                        # if match - replace guessed_word current position with guess letter
                        guessed_word[idx] = guess

                        # bump found_count by 1
                        found_count += 1

                # if found_count == 0 then no matching letters were found in the word
                if found_count == 0:

                    # update the gallows list
                    # if hanged_level <= 1 or hanged_level == 3 then add a body part
                    if (hanged_level <= 1) or (hanged_level == 3):
                        gallows[gallows_level] = hanged_man[hanged_level]
                    # elif hanged_level == 2 or 4 then add an arm or leg at the same gallows_level
                    elif (hanged_level == 2) or (hanged_level == 4):
                        gallows[gallows_level - 1] = hanged_man[hanged_level]

                        # if hanged_level = 4 then fully hanged and game over
                        if hanged_level == 4:

                            # set winner to false and game_over to true
                            winner = False
                            game_over = True

                    # if not game over then increase gallows_level and hanged_level by 1
                    if hanged_level < 4:

                        # increase both gallows_level and hanged_level
                        gallows_level += 1
                        hanged_level += 1

                else:

                    # check the guessed_word for any remaining blank letters
                    if '_' not in guessed_word:

                        # set winner to true and game_over to true
                        winner = True
                        game_over = True

                # clear the terminal screen
                clear_terminal()

                # show the guessed_word list with each letter separated by a space
                for char in guessed_word:
                    print(char, end=' ')

                # announce the outcome of the last guess
                # if the winner == true
                if winner is True:

                    # show message -> "You win!\n"
                    print('\nJustice has saved you. You win!\n')

                # else if game_over == true and winner == false
                elif (winner is False) and (game_over is True):

                    # show message -> "You've been hanged partner! You lose.\n"
                    print('\nYou\'ve been hanged partner! You lose.\n')

                # else if found_count > 0
                elif found_count > 0:

                    # show message ->
                    # "You guessed '[guess]'. It appears in the word [found_count] times!\n"
                    if found_count == 1:
                        print(f'\nYou guessed \'{guess}\'. '
                              f'It appears in the word {found_count} time.\n')
                    else:
                        print(f'\nYou guessed \'{guess}\'. '
                              f'It appears in the word {found_count} times.\n')

                # else
                else:

                    # show message ->
                    # "You guessed '[guess]'. That's not in the word. One step closer to death.\n"
                    print(f'\nYou guessed \'{guess}\'. '
                          'That\'s not in the word. One step closer to death.\n')

                # loop through drawing the current gallows line-by-line
                for level in range(0, len(gallows) - 1):
                    print(gallows[level])

    # Ask user to play another game
    play_again = input('\nPlay again (Y/N)? ').lower()

    return None

if __name__ == '__main__':
    main()
