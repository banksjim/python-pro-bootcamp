size = input("What size of pizza would you like? (S)mall, (M)edium, or (L)arge: ")
add_pepperoni = input("Add pepperoni? $2 extra for small, $3 extra for medium and large (Y/N): ")
extra_cheese = input("Add extra cheese? $1 extra for all sizes (Y/N): ")

# pylint: disable=C0103
total_bill = 0.00
valid_order = True

if size.upper() == "S":
    total_bill = 15
elif size.upper() == "M":
    total_bill = 20
elif size.upper() == "L":
    total_bill = 25
else:
    print("Invalid selection for pizza size. Please order again.")
    valid_order = False

if add_pepperoni.upper() == "Y":
    if size.upper() == "S":
        total_bill += 2
    else:
        total_bill += 3
elif add_pepperoni != "N":
    print("Invalid selection for option: add pepperoni. Please order again.")
    valid_order = False

if extra_cheese.upper() == "Y":
    total_bill += 1
elif extra_cheese.upper() != "N":
    print("Invalid selection for option: extra cheese. Please order again.")
    valid_order = False

if valid_order is True:
    print("Thank you for choosing Python Pizza Deliveries!")
    print(f"Your final bill is: ${total_bill:0.0f}.")
