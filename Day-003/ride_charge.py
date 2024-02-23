# pylint: enable=C0103
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")

    # pylint: disable=C0103
    admission_fee = 0.00
    ticket_type = ""

    age = int(input("What is your age? "))
    if age < 12:
        admission_fee = 5.00
        ticket_type = "Child"
    elif age <= 18:
        admission_fee = 7.00
        ticket_type = "Youth"
    elif age >= 45 and age <= 55:
        admission_fee = 0.00
        ticket_type = "Midlife Crises Adult"
        print("You deserve a break. Have a free ride on us!")
    else:
        admission_fee = 12.00
        ticket_type = "Adult"

    print(f"{ticket_type} tickets are ${admission_fee:0.2f}")

    purchase_photo = input("Would you also like to add a photo for $3 more (Y/N)? ")
    if str.upper(purchase_photo) == "Y":
        admission_fee += 3.00

    print(f"Your total admission fee is ${admission_fee:0.2f}")
else:
    print("Sorry, you are not yet tall enought to ride.")
