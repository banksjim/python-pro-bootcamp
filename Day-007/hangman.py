import requests

from shared_modules.system_modules import clear_terminal

# main() program logic module
def main():

    # initialize static variables
    play_again:   str = "Y"

    # ASCII art variables
    banner:       str = r'''
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
    while play_again == 'Y':

        # clear the terminal screen
        clear_terminal()

        # initialize game-specific variables
        game_over:    bool = False
        found_count:  int = 0
        guess:        str = ""
        hanged_level: int = 0
        hanged_man:   bool = False
        random_word:  str = ""
        response:     str = ""
        winner:       bool = False

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

        while not game_over:

            # count the number of letters in the random_word

            # initialize the letters of the random word in a list of letters

            # initialize a guessed_word list with '_''s for the user's guess of the word

            # loop until the random_word is guessed or the hanged man flag is true

                # prompt to guess the first letter letter
                # guess = input("\nGuess a letter: ").lower()

                # set found_count to zero

                # loop to check if the guess letter is in the word and count how many times

                    # compare the guess to the random_word list in the current idx position

                        # if match
                        # replace the guessed_word current position with upper guess letter
                        # bump found_count by 1

                # if found_count == 0 then no matching letters were found in the word

                    # increase hanged_level by 1

                    # update the gallows list
                    # if hanged_level == 1
                    # gallows idx of (hanged_level + 1) = hanged_man (hanged_level - 1)
                    # elif hanged_level == 2 or 4
                    # gallows idx of (hanged_level + 1) = hanged_man (hanged_level - 1)
                    # else
                    # gallows idx of (hanged_level) = hanged_man (hanged_level - 1)

                    # if hanged_level == 5
                    # set winner to false
                    # set game_over to true

                # else

                    # check the guessed_word for any remaining blank letters

                    # if no remaining '_' letters

                        # set winner to true
                        # set game_over to true

                # clear the terminal screen

                # show the guessed_word list with each letter separated by a space

                # announce the outcome of the last guess
                # if the winner == true
                    # show message -> "You win!\n"
                # else if game_over == true and winner == false
                    # show message -> "You've been hanged partner! You lose.\n"
                # else if found_count > 0
                    # show message ->
                    # "You guessed '[guess]'. It appears in the word [found_count] times!\n"
                # else
                    # show message ->
                    # "You guessed '[guess]'. That's not in the word. One step closer to death.\n"

                # loop through drawing the current gallows line-by-line

        # Ask user to play another game
        # play_again = input("Play again (Y/N)? ").upper()

    return None

if __name__ == '__main__':
    main()
