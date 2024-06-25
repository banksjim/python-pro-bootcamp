import ast

from shared_modules.system_modules import clear_terminal

# initialize global variables
travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

# add_new_country() function
def add_new_country(country_add, visits_add, list_of_cities_add):
    
    travel_log.append(
        {
            "country": country_add,
            "visits": visits_add,
            "cities": list_of_cities_add
        }
    )
    
    return None

# main() program logic module
def main():

    # clear the terminal screen
    clear_terminal()

    # initialize module variables
    country: str = ""
    visits: int = 0
    list_of_cities = []  

    # mainline statements
    
    # Add country name
    country = input("Country name: ") 
    
    # Number of visits   
    visits = int(input("Number of visits: ")) 
    
     # List of cities visited
    cities_input = input("List of cities visited in the format [\"city_1\", \"city_n\"]: ")
    list_of_cities = ast.literal_eval(cities_input) # Create list from formatted string
    
    add_new_country(country, visits, list_of_cities)
    
    print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
    print(f"My favorite city was {travel_log[2]['cities'][0]}.")

    return None

if __name__ == '__main__':
    main()
