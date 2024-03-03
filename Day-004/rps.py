import os
import random
import sys

# Declare modules
def get_terminal_type():
    if sys.platform.startswith("win"):
        return "Windows"
    return None

def find_index(input_list, target_value):
    if target_value in input_list:
        return input_list.index(target_value)
    else:
        print("**Invalid selection**")
        return 999

def main():
    # Declare variables & lists
    check_selection:  int = 999 # 999 Used to signal invalid selection
    computer_choice:  int = 0
    player_choice:    int = 0
    rules_index:      int = 0

    selection_valid:  bool = False

    choices_lookup:   str = ""
    play_again:       str = "Y"
    player_selection: str = ""

    rock: str = """
        _______
    ---'   ____)
        (_____)
        (_____)
        (_____)
    ---.__(___)
    """

    paper: str = """
        ________
    ---'    ____)___
            ________)
            _________)
            _________)
    ---.____________)
    """

    scissors: str = """
        _____
    ---'   __)____
            ______)
        __________)
        (___)
    ---.(___)
    """

    # Declare lists
    rps_list = [rock, paper, scissors]

    rps_rules = [
        "00","D","01","L","02","W",
        "10","W","11","D","12","L",
        "20","L","21","W","22","D"
    ]

    valid_player_selections = ["0", "1", "2"]

    # Main() logic
    while play_again.upper() == "Y":

        # Clear the terminal screen in either windows or mac/linux
        terminal_type = get_terminal_type()
        if terminal_type == "Windows":
            os.system("cls")
        else:
            os.system("clear")

        # Determine choices
        selection_valid = False
        
        while selection_valid is False:
            player_selection = input("Choose 0, 1, or 2 -> Rock (0), Paper (1), or Scissors (2): " )

            check_selection = find_index(valid_player_selections, player_selection)
            if check_selection != 999:
                selection_valid = True
            else:
                selection_valid = False

        player_choice = int(player_selection)
        computer_choice = random.randint(0, 2)

        # Show choices using ASCII art
        print(f"{rps_list[player_choice]}")
        print("\nThe computer chose:")
        print(f"{rps_list[computer_choice]}")

        # Determine and declare winner
        choices_lookup = player_selection + str(computer_choice)
        rules_index = rps_rules.index(choices_lookup)

        if rps_rules[rules_index + 1] == "W":
            print("You win!")
        elif rps_rules[rules_index + 1] == "L":
            print("You lose")
        else:
            print("A draw")

        # Check play again
        play_again = input("\nPlay another round (Y/N)? ")

# Execute main() function
if __name__ == "__main__":
    main()
