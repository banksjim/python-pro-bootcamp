# pylint: disable=C0200
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

    # declare main() variables
    high_score: int = 0
    score:      int = 0

    # input and initialize scores list
    student_scores = input().split()
    for score in range(0, len(student_scores)):
        student_scores[score] = int(student_scores[score])

    # find the highest score
    for score in student_scores:
        if score > high_score:
            high_score = score

    # print the high score
    print(f"The highest score in the class is: {high_score}")

if __name__ == '__main__':
    main()
