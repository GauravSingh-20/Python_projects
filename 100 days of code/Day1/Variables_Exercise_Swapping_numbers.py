num1=int(input("Input the first number"))
num2=int(input("Input the second number"))
def swap(a,b):
    a=a+b
    b=a-b
    a=a-b

swap(num1,num2)
print("Num1 after swapping",num1)
print("Num2 after swapping",num2)