import random

names=input("Provide everybody's names : ")

names_list=names.split(",")

length_list=len(names_list)


random_name=random.randint(0,length_list)

payee=random.choice(names_list)

print(f"{names_list[random_name]} will pay the bill")

print(f"{payee} will pay the bill")