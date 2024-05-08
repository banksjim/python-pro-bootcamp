import math

from shared_modules.system_modules import clear_terminal

def paint_calc(height: int = 0, width: int = 0):

    # initialize module variables
    can_coverage:    int = 5 # A paint can covers 5 sq meters
    required_cans:   int = 0
    work_area:       int = 0 # Area that needs to be painted

    # calculate paint cans required
    work_area = height * width
    required_cans = int(math.ceil(work_area / can_coverage))

    return required_cans

# main() program logic module
def main():

    # clear the terminal screen
    clear_terminal()

    # initialize module variables
    cans_needed: int = 0
    test_h:      int = 0
    test_w:      int = 0

    # mainline statements
    print('Paint order calculator\n')

    test_h = int(input('Enter coverage height in meters: '))
    test_w = int(input('Enter coverage width in meters:  '))

    cans_needed = paint_calc(test_h, test_w)

    # output results
    print(f'\nTo paint an area of {test_h} m high and {test_w} m wide '
          f'will require {cans_needed} cans.\n')

    return None

if __name__ == '__main__':
    main()
