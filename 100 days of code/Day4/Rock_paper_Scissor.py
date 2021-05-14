import random

rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

ROCK

""")

paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

PAPER

""")

scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

SCISSORS

""")

choice_list=[rock,paper,scissors]
comp_choice=random.randint(0,2)


user_input=int(input("What do you choose ?  Type 1 for rock, 2 for paper and 3 for scissors "))-1
print(f"Your Choice : \n{choice_list[user_input]}\n\n")
print(f"Computer's Choice : \n{choice_list[comp_choice]}")


# 0 is ROCK
# 1 is PAPER
# 2 is SCISSORS

if user_input==0:
    if comp_choice==0:
        print("It's a Draw 🤭 ")
    elif comp_choice==1:
        print("Yay ! You won 🤩 ")
    else:
        print("Sorry ! You Lost 😭 ")
elif user_input==1:
    if comp_choice==0:
        print("Sorry ! You Lost 😭 ")
    elif comp_choice==1:
        print("It's a Draw 🤭 ")
    else:
        print("Yay ! You won 🤩 ")
elif user_input==2:
    if comp_choice==0:
        print("Yay ! You won 🤩 ")
    elif comp_choice==1:
        print("Sorry ! You Lost 😭  ")
    else:
        print("It's a Draw 🤭 ")
else:
    print("Please enter a valid choice !!")




