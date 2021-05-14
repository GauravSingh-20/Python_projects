user_input=input("Enter the scores of students out of 100  separated by comma : ").split(",")

max_score=0

for n in range(0,len(user_input)):
    user_input[n]=int(user_input[n])
    if max_score<user_input[n]:
        max_score=user_input[n]

print(f"The maximum score is : {max_score}")