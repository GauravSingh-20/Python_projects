print("Welcome to RollerCoster")
height=int(input("Please enter your height in cm"))
age=int(input("Enter your age : "))
bill=0

if height>=120:
    print("You can ride the RollerCoster !!")
    if age<12:
        bill=5
        print("Ticket price is $5")
    elif age<=18:
        bill=7
        print("Ticket price is $7")
    else:
        bill=12
    
    want_photo=input("Do you want your photo taken? (Y/N) : ")
    if want_photo=='Y' or want_photo== 'y':
        bill+=3
    
    print(f"Your total bill is : {bill} " )

else:
    print("You can not ride the RollerCoster !!S")