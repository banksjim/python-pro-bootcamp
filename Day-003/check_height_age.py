print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")

    age = int(input("What is your age? "))
    if age < 12:
        print("Your admission fee will be $5")
    elif age <= 18:
        print("Your admission fee will be $7")
    else:
        print("Your admission fee will be $12")
else:
    print("Sorry, you are not yet tall enought to ride.")
