print("Welcome to Love Calculator")
name1=(input("Enter your name : ")).lower()
name2=(input("Enter his/her name : ")).lower()
c_name=name1+name2

string1="True".lower()
string2="Love".lower()


true_count=(c_name.count("t"))+(c_name.count("r"))+(c_name.count("u"))+(c_name.count("e"))
love_count=c_name.count("l")+c_name.count("o")+c_name.count("v")+c_name.count("e")

love_score=int(str(true_count)+str(love_count))

if love_score >90 or love_score<10:
    print(f"your score is {love_score} , You go together like coke and mentos")

elif love_score>=40 and love_score<=50:
    print(f"your score is {love_score} , You are alright together")

else:
    print(f"Your score is {love_score}")    