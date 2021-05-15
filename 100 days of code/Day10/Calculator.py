logo = """
 _____________________
|  _________________  |
| | Gaurav  Singh   | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print (logo)

def calculator(number1, number2, operator):
    if operator=='+':
        return number1+number2
    elif operator=='-':
        return number1-number2
    elif operator=='*':
        return number1*number2
    elif operator=='/':
        return number1/number2
    else:
        return "Invalid Input !!"

do_continue=True
while do_continue:
    number1=int(input("Enter the  first number : "))
    operator=input(
        ''' 
        +
        -
        *
        /
        Please choose operations from above list: 
        ''')
    number2=int(input("Enter the second number : "))
    print(f"{number1} {operator} {number2} = {calculator(number1,number2,operator)}")  
    continue_=input("Do you want to continue ? 'Yes' or 'No' ").lower()
    if continue_=='yes':
        do_continue=True
    else:
        do_continue=False      


