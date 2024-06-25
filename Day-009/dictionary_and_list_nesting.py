from shared_modules.system_modules import clear_terminal

# main() program logic module
def main():

    # clear the terminal screen
    clear_terminal()

    # initialize module variables

    # basic dictionary
    capitals = {
        "France": "Paris",
        "Germany": "Berlin"
    }

    # nesting lists in a dictionary
    travel_log = {
        "France": ["Paris", "Lyon", "Dijon"],
        "Germany": ["Berlin", "Stuttgart", "Hamburg"]
    }

    # nesting a dictionary in a dictionary
    extended_travel_log = {
        "France": {
            "cities_visited": ["Paris", "Lyon", "Dijon"],
            "total_visits": 12
        },
        "Germany": {
            "cities_visited": ["Berlin", "Stuttgart", "Hamburg"],
            "total_visits": 4
        }
    }

    # nesting dictionaries in a list
    alternate_travel_log = [
        {
            "country": "France",
            "cities_visited": ["Paris", "Lyon", "Dijon"],
            "total_visits": 12
        },
        {
            "country": "Germany",
            "cities_visited": ["Berlin", "Stuttgart", "Hamburg"],
            "total_visits": 4
        }
    ]

    # mainline statements

    return None

if __name__ == '__main__':
    main()
