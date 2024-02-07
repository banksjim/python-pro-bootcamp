# Display welcome message
print("Welcome to the tip calculator.")

# Ask for the total bill in dollars
total_bill = float(input("What was the total bill? $"))

# Ask for which percentage tip to apply
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Ask how many people to split the bill between
number_of_parties = int(input("How many people to split the bill? "))

# Calculate the bill with tip per person
total_bill_with_tip = total_bill * (1 + (tip_percentage / 100))
final_bill_per_party = total_bill_with_tip / int(number_of_parties)

# Output the amount each person should pay
print(f"Each person should pay: ${final_bill_per_party:.2f}")
