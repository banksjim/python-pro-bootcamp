from shared_modules.system_modules import clear_terminal

def greet(name: str = ""):
    print(f'Hello {name}')
    print(f'It\'s nice to meet you {name}.')
    print('line3')

# main() program logic module
def main():

    # clear the terminal screen
    clear_terminal()

    # initialize module variables

    # mainline statements
    greet("Jim")

    return None

if __name__ == '__main__':
    main()
