name = input ("Enter your name: ")

weight = int(input("Enter your weight in pounds: "))

height = int(input ("Enter your height in inches: "))

BMI = (weight * 703) / (height * height)

print(BMI)
if BMI > 0:
    if(BMI< 18.5):
        print(name + ", You are Underweight")
    elif(BMI<=24.9):
        print(name + ", You are Normal weight")
    elif(BMI<29.9):
        print(name + ", You are overweight weight")
    elif(BMI<34.9):
        print(name + ", You are Obese weight")
    elif(BMI<39.9):
        print(name + ", You are severely Obese weight")
    elif(BMI>40):
        print(name + ", You are Morbidly Obese weight")
else:
        print("Enter valid inputs")





if BMI > 0:
    if(BMI< 18.5):
        print(name + ", You are Underweight")
    elif(BMI<=24.9):
        print(name + ", You are Normal weight")
    elif(BMI<29.9):
        print(name + ", You are overweight weight")
    elif(BMI<34.9):
        print(name + ", You are Obese weight")
    elif(BMI<39.9):
        print(name + ", You are severely Obese weight")
    elif(BMI>40):
        print(name + ", You are Morbidly Obese weight")
    else:
        print("Enter valid inputs")



# BMI = (weight in pounds X 703) / (height in inches X height in inches)


# Under 18.5	Underweight	Minimal
# 18.5 - 24.9	Normal Weight	Minimal
# 25 - 29.9	Overweight	Increased
# 30 - 34.9	Obese	High
# 35 - 39.9	Severely Obese	Very High
# 40 and over	Morbidly Obese	Extremely High