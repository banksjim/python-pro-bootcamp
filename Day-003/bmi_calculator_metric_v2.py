height_m = float(input("What is your height in m? "))
weight_kg = float(input("What is your weight in kg? "))

bmi_metric = weight_kg / height_m ** 2

if bmi_metric <= 18.5:
    print(f"Your BMI is {bmi_metric}, you are underweight.")
elif bmi_metric < 25:
    print(f"Your BMI is {bmi_metric}, you have a normal weight.")
elif bmi_metric < 30:
    print(f"Your BMI is {bmi_metric}, you are slightly overweight.")
elif bmi_metric < 35:
    print(f"Your BMI is {bmi_metric}, you are obese.")
else:
    print(f"Your BMI is {bmi_metric}, you are clinically obese.")
