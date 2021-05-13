samll_pizza=15
medium_pizza=20
large_pizza=25

pepperoni_small=2
pepperoni_M_L=3

extra_cheese=1

pizza_input=input("Which pizza do you want ? S,M,L ")
pepperoni_input=input("Do you want pepperoni? (Y/N)")
cheese_input=input("Do you want extra cheese ? (Y/N)")

bill=0

if pizza_input=="S" or pizza_input=='s':
    bill=samll_pizza
    if pepperoni_input=='Y' or pepperoni_input=='y':
        bill+=pepperoni_small
    if cheese_input=='Y' or extra_cheese=='y':
        bill+=extra_cheese 
elif pizza_input=='M' or pizza_input=='m':
    bill=medium_pizza
    if pepperoni_input=='Y' or pepperoni_input=='y':
        bill+=pepperoni_M_L
    if cheese_input=='Y' or extra_cheese=='y':
        bill+=extra_cheese
elif pizza_input=='L' or pizza_input=='l':
    bill=large_pizza
    if pepperoni_input=='Y' or pepperoni_input=='y':
        bill+=pepperoni_M_L
    if cheese_input=='Y' or extra_cheese=='y':
        bill+=extra_cheese 

print("Your total bill is : ",bill)                  
