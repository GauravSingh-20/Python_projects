from os import system

print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\



               WELCOME TO THE SECRET AUCTION !!!!

''')


ans='yes'
bids={}
while ans=='yes':
    _=system('cls')
    name=input("Please enter your name :  ")
    bid=(int(input("Please input your bid :  ")))
    bids[name]=bid

    ans=input("Are there any other bidders . Type 'Yes' or 'No"    ).lower()

max_bid=0

names_list=list(bids.keys())
bid_list=list(bids.values())

for i in bid_list:
    if i > max_bid:
        max_bid=i
position=bid_list.index(max_bid)
name=names_list[position]
print(f'{name} has the highest bid with ${max_bid}')        
