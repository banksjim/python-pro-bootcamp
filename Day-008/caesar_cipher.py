import string
from shared_modules.system_modules import clear_terminal
from caesar_cipher_banner import banner

def encode_decode(msg: str = '', encode_option: str = 0, shift_value: int = 0):

    # initialize variables
    alphabet_loc:         int = 0
    msg_length:           int = 0
    replacement_char_idx: int = 0
    result_string:        str = ''

    alphabet = list(string.ascii_lowercase)

    # determine the length of the msg
    msg_length = len(msg)

    # iterate through the msg characters
    for letter in msg:

        # check if the current character in the msg is alphabetic
        if letter in alphabet:

            # determine position of the current msg char in the alphabet
            alphabet_loc = alphabet.index(letter)

            if encode_option == 'encode':

                # determine if the position of the msg(idx) char + the
                # shift_value will exceed the alphabet list and need to
                # wrap forward from the beginning of the alphabet
                if (alphabet_loc + shift_value) < 26:
                    # calculate the replacement_char_idx position from
                    # alphabet_loc + shift_value
                    replacement_char_idx = alphabet_loc + shift_value
                else:
                    # calculate the replacement_char_idx position from
                    # shift_value - (25 - alphabet_loc)
                    replacement_char_idx = shift_value - (26 - alphabet_loc)

            elif encode_option == 'decode':

                # determine if the position of the msg(idx) char - the
                # shift_value will be less than 0 causing a need to wrap
                # backwards through the alphabet
                if (alphabet_loc - shift_value) >= 0:
                    # calculate the replacement_char_idx position from
                    # alphabet_loc - shift_value
                    replacement_char_idx = alphabet_loc - shift_value
                else:
                    # calculate the replacement_char_idx position from
                    # 26 - (shift_value - alphabet_loc)
                    replacement_char_idx = 26 - (shift_value - alphabet_loc)

            # build replacement string
            result_string += alphabet[replacement_char_idx]

        else:
            result_string += msg[idx]

    return result_string

# main() program logic module
def main():

    # initialize module variables
    run_again:         str = 'y'

    # mainline statements
    while run_again == 'y':

        # initialize session variables
        encode_option:  str = ''
        message:        str = ''
        message_result: str = ''
        shift:          int = 0
        shift_input:    str = ''

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

                # encode / decode message
                message_result = encode_decode(message, encode_option, shift)

                # output results
                if encode_option == 'encode':
                    print(f'Here\'s your encoded result: {message_result}')
                else:
                    print(f'Here\'s your decoded result: {message_result}')

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
