import random

row1=["😀", "😍", "🤩"]
row2=["😡", "🤥", "🥺"]
row3=["🤖", "☠️", "🎃"]

map=[row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}")

index1=random.randint(0,2)
index2=random.randint(0,2)


print("\n\n\n")
map[index1][index2]="🎯"

print(f"{row1}\n{row2}\n{row3}")



