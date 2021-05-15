def prime_number(number):
    flag=0
    for i in range(2,number+1):
        if(number%i==0):
            flag+=1
            
        else:
            pass
    if flag>1:
        print("It's not a prime number")
    else:
        print("It's a prime number")

number=int(input("Please enter the number"))
prime_number(number)
