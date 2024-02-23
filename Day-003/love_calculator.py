# pylint: disable=C0103
name1:               str = ""
name2:               str = ""
combined_names:      str = ""

first_letter_count:  int = 0
second_letter_count: int = 0
score:               int = 0

name1 = input("What is your name?  ")
name2 = input("What is their name? ")

combined_names = name1.upper() + name2.upper()

first_letter_count += combined_names.count("T")
first_letter_count += combined_names.count("R")
first_letter_count += combined_names.count("U")
first_letter_count += combined_names.count("E")

second_letter_count += combined_names.count("L")
second_letter_count += combined_names.count("O")
second_letter_count += combined_names.count("V")
second_letter_count += combined_names.count("E")

score = int( str(first_letter_count) + str(second_letter_count) )

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
