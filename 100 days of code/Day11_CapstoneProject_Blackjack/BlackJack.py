import random

jack=10
Queen=10
King=10
cards=[11,2,3,4,5,6,7,8,9,10,jack,Queen,King]

user_cards=[]
computer_cards=[]

for i in range(0,2):
    for card in cards:
        user_cards=random.choice(cards)
        computer_cards=random.choice(cards)

sum_user=0
sum_computer=0

for card in user_cards:
    sum_user+=card

for card in computer_cards:
    sum_computer+=card

if (user_cards[0]==11 or user_cards[1]==10) and (user_cards[0]==10 or user_cards[1]==11):
    print()

    