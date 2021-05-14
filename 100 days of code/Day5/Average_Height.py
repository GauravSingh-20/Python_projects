user_input=input("Enter the height of students in cm separated by comma").split(",")

no_of_students=0
sum_of_Height=0

for n in range(0,len(user_input)):
    user_input[n]=int(user_input[n])    
    no_of_students+=1
    sum_of_Height+=user_input[n]

print("Average Height of student is : ")

print(round(sum_of_Height/no_of_students))    
    