import os
import sys

# determine terminal type
def get_terminal_type():
    if sys.platform.startswith("win"):
        return "Windows"
    return None

# main() program logic module
def main():

    # Clear the terminal screen in either windows or mac/linux
    terminal_type = get_terminal_type()
    if terminal_type == "Windows":
        os.system("cls")
    else:
        os.system("clear")

    fruits = ["Apple", "Peach", "Pear"]
    print(fruits)

    for fruit in fruits:
        print(f"{fruit}")
        print(f"{fruit}" + " Pie")

if __name__ == "__main__":
    main()
