input_year=int(input("Enter the year"))

if input_year%4==0:
    if input_year%100==0:
        if input_year%400==0:
            print("It is a leap year")
        else:
            print("Not a leap year")
    else:
        print("It is a leap year")

else:
    print("Not a leap year")