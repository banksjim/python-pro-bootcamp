# U.S. states ordered by date of ratification into the Union
us_states = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
    "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
    "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",
    "Illinois", "Alabama", "Maine", "Missouri", "Arkansas",
    "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
    "California", "Minnesota", "Oregon", "Kansas", "West Virginia",
    "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota",
    "Montana", "Washington", "Idaho", "Wyoming", "Utah",
    "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"
]

# The final of the original 13 states
print(us_states[12])

# A negative index starts counting backwards from the end of the list,
# but is 1 based not 0 based (-0 is not a real number)
print(us_states[-3])

# Change the value of an item in a list
us_states[1] = "Pencilvania"
print(us_states[1])

# Append one item to the list
us_states.append("Puerto Rico")
print(us_states)

# Remove from the list
us_states.remove("Pencilvania")
print(us_states)

# Insert into the list
us_states.insert(1, "Pennsylvania")
print(us_states)

# Add more than one item to the end of the list
us_states.extend(["Guam", "U.S. Virgin Islands"])
print(us_states)

# Get the length of the list
print(len(us_states))
