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





def add(number1,number2):
    return number1+number2

def substract(number1, number2):
    return number1-number2

def multiply(number1,number2):
    return number1*number2

def divide(number1,number2):
    return number1/number2


operations={
    "+":add,
    "-":substract,
    "*":multiply,
    "/":divide,
}    
def Calculator():

    print (logo)

    number1=float(input("Enter the first number : "))
    
    for operation in operations:
        print(operation)

    isTrue=True

    while isTrue:
        number2=float(input("Enter the next number : "))
        operation_symbol=input("Choose from the above  mentioned operations : ") 
        operation_performed=operations[operation_symbol]
        result=operation_performed(number1,number2)
        print(f"{number1} {operation_symbol} {number2} = {result}")
        _continue=input(f"Do you want to perform more operations with previous answer {result}?  Type 'Yes' or 'No'").lower()
        if _continue=='yes':
            number1=result
            
        else:
            isTrue=False
            if input("Do you want to start fresh calculation. Type 'Yes' or 'No' " ).lower()=='yes':
                Calculator()
            else:
                break      

Calculator()            