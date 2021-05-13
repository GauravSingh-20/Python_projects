weight=float(input("Enter your weight"))
height=float(input("Enter your height"))

BMI=(weight)//(height*height)

print('Your BMI is : ',round(BMI,1))

if BMI<=18.5:
    print("You are UNDERWEIGHT")
elif BMI>18.5 and BMI<=25:
    print("You have NORML weight")
elif BMI>25 and BMI<=30:
    print("You are OVERWEIGHT")
elif BMI>30 and BMI<=35:
    print("You are OBESE")
else:
    print("You are clinically OBESE")
