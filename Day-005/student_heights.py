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

    average_height: float = 0.0
    student_count:  int = 0
    student_height: int = 0
    total_height:   int = 0

    # clear the terminal in either windows or mac/linux
    terminal_type = get_terminal_type()
    if terminal_type == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

    # Modifed exercise-provided code
    student_heights = input().split()

    for n in range(0, len(student_heights)):
        student_heights[n] = int(student_heights[n])

    # Excercise-submitted code
    for student_height in student_heights:
        total_height += student_height
        student_count += 1

    average_height = round(total_height / student_count, 0)

    # output results
    print(f"total height = {total_height}")
    print(f"number of students = {student_count}")
    print(f"average height = {average_height:.0f}")

if __name__ == '__main__':
    main()
