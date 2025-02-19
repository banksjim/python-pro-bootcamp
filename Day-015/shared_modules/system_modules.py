import os
import sys

# Determine terminal type
def get_terminal_type():

    # determine if running Windows
    if sys.platform.startswith('win'):
        return 'Windows'
    else:
        return None

# Clear the terminal in either windows or mac/linux
def clear_terminal():

    terminal_type = get_terminal_type()
    if terminal_type == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

    return None

# Press any key to continue
def press_any_key_to_continue():
    print("\nPress any key to continue...")
    if os.name == 'nt':  # For Windows
        import msvcrt
        msvcrt.getch()
    else:  # For Unix-based systems (macOS, Linux)
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
