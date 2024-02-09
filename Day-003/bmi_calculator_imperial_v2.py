print("What is your height in feet and inches?")
height_ft = float(input("Feet:   "))
height_in = float(input("Inches: "))
weight_lbs = float(input("What is your weight in lbs? "))

bmi_standard = (weight_lbs / (((height_ft * 12) + height_in) ** 2)) * 703

if bmi_standard < 18.5:
    print(f"Your BMI is {bmi_standard}, you are underweight.")
elif bmi_standard < 25:
    print(f"Your BMI is {bmi_standard}, you have a normal weight.")
elif bmi_standard < 30:
    print(f"Your BMI is {bmi_standard}, you are slightly overweight.")
elif bmi_standard < 35:
    print(f"Your BMI is {bmi_standard}, you are obese.")
else:
    print(f"Your BMI is {bmi_standard}, you are clinically obese.")
