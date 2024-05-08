from shared_modules.system_modules import clear_terminal

def greet_with(name: str = "", location: str = ""):
    print(f'Hello {name}.')
    print(f'Please tell us more about {location}.')
    print('\n')

# main() program logic module
def main():

    # clear the terminal screen
    clear_terminal()

    # mainline statements
    greet_with('Jim', 'Monett, MO')

    greet_with(location='Aurora, CO', name='Paul')

    return None

if __name__ == '__main__':
    main()
