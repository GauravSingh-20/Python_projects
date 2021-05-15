from data import data
from art import logo,vs
import random
import os

#Format the account data into printable format
def format_data(account):
    account_name=account['name']
    account_descriptipn=account['description']
    account_country=account['country']
    return f"{account_name}, a {account_descriptipn} from {account_country}"


#Checking answer
def check_answer(guess,a_followers_count,b_followers_count):
    if a_followers_count>b_followers_count:
        return guess=='a'

    else:
        return guess=='b'

#Display Art

print(logo)

score=0
continue_game=True
account_b=random.choice(data)

#Make game repeatable

while continue_game:
    #Getting two random choices
    account_a=account_b
    account_b=random.choice(data)

    while account_a==account_b:
        account_b=random.choice(data)

    #Clear the screen
    _=os.system('cls')
    print(logo)

    print(f"Comapare A : {format_data(account_a)}")
    print(vs)
    print(f"Against B : {format_data(account_b)}")


    #Ask user for a Guess

    guess=input("Who has more followers , Type  A or B : ").lower()

    #Check if user is correct 
    ##Get follower count for each acccount

    a_followers_count=account_a['follower_count']
    b_followers_count=account_b['follower_count']

    is_correct=check_answer(guess,a_followers_count,b_followers_count)


    #Give user feedback on their guess

    if is_correct:
        score+=1
        print(f"You are correct. Current score : {score}")
    
    else:
        continue_game=False
        print(f"Sorry, that's wrong. Final score : {score}")

    
