print("Check for Leap Year")
year = int(input("What year do you want to check? "))

if year % 4 == 0:
    if year % 400 == 0:
        print("Leap year")
    elif year % 100 == 0:
        print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")
