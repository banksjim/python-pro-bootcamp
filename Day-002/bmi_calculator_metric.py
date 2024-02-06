# Metric BMI calculation:

#       weight (kg)
# BMI = --------------------
#       height ** 2 (m ** 2)

# Express BMI as a whole number

height = 1.65
weight = 72

bmi_metric = (weight / (height ** 2))

print("Patient #1's BMI = " + str(int(bmi_metric)))

# Imperial BMI calculation:
#       weight (lbs)
# BMI = ------------------------------------ * 703
#       ((height_feet + height_inches) ** 2)

# Express BMI as a whole number

height_feet = 5
height_inches = 11
weight = 160

bmi_imperial = (weight / (((height_feet * 12) + height_inches) ** 2)) * 703

print("Patient #2's BMI = " + str(int(bmi_imperial)))
