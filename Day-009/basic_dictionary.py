from shared_modules.system_modules import clear_terminal

# main() program logic module
def main():

    # clear the terminal screen
    clear_terminal()

    # initialize module variables
    empty_dictionary = {}

    programming_dictionary = {
        "Bug": "An error in a program that prevents the program from running as expected.",
        "Function": "A construct in code that you can easily call over and over again.",
        "Loop": "The action of doing something over and over again."
    }

    # mainline statements

    # Display an entry in the dictionary
    print(programming_dictionary["Bug"])

    # Add an entry to the dictionary
    programming_dictionary["Variable"] = (
        "A name that is used to refer to a memory location in a computer's "
        "memory where a value is stored."
    )

    print(programming_dictionary["Variable"])

    # Display the contents of the dictionary
    print(empty_dictionary)
    print(programming_dictionary)

    # Edit the contents of a dictionary
    programming_dictionary["Bug"] = "A moth in your computer"
    print(programming_dictionary["Bug"])

    # Loop through the contents of a dictionary
    for key in programming_dictionary:
        print(key)
        print(programming_dictionary[key])
  
    # Recommend method for looping through dictionary content
    for pl_dict_key, pl_dict_value in programming_dictionary.items():
        print(pl_dict_key)
        print(pl_dict_value)

    # Wipe the contents from a populated dictionary
    programming_dictionary = {}
    print(programming_dictionary)

    return None

if __name__ == '__main__':
    main()
