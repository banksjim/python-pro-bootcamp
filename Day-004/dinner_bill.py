import random

# Declare variables
payee: int = 0
attendee_count: int = 0
names_string: str = ""
names = []

# Input who went to dinner delimited by a comma and space (e.g., Jim, Bill, Jill)
names_string = input("Who joined the meal together? ")

# Initialize the list from the default string and count the attendees
names = names_string.split(", ")
attendee_count = len(names)

# Select a random index to choose the payee
payee = random.randint(0, (attendee_count - 1) )

# Print who pays the bill
print(f"{names[payee]} is going to buy the meal today!")
