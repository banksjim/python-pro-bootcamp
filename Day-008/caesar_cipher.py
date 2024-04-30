from shared_modules.system_modules import clear_terminal
from caesar_cipher_banner import banner

# main() program logic module
def main():

    # initialize module variables
    run_again:         str = 'y'

    # mainline statements
    while run_again == 'y':

        # initialize session variables
        ciphered_messsage: str = ''
        encode_option:     str = ''
        message:           str = ''
        shift:             int = 0
        shift_input:       str = ''

        # clear the terminal screen
        clear_terminal()

        # print application banner
        print(banner)

        print('Type \'encode\' to encrypt. Type \'decode\' to decrypt:')
        encode_option = input().lower()

        if (encode_option == 'encode') or (encode_option == 'decode'):

            # input message to encode or decode
            print('\nType your message:')
            message = input().lower()

            # input encode / decode shift number
            print('\nType your shift number:')
            shift_input = input()

            # check if shift value is a number and convert to int
            if shift_input.isdigit():

                # assign shift_input to an integer var
                shift = int(shift_input)

            else:
                print('\nShift value must be a number between 1 and 25.')

        else:

            # invalid encode or decode option selection
            print('\nInvalid option selected.')
    
        # ask if user wants to run the app again
        run_again = input('\nRun the application again (y/n)? ').lower()

    return None

if __name__ == '__main__':
    main()
