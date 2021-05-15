import random

logo= '''

 ██████  ██    ██ ███████ ███████ ███████     ████████ ██   ██ ███████     ███    ██ ██    ██ ███    ███ ██████  ███████ ██████  
██       ██    ██ ██      ██      ██             ██    ██   ██ ██          ████   ██ ██    ██ ████  ████ ██   ██ ██      ██   ██ 
██   ███ ██    ██ █████   ███████ ███████        ██    ███████ █████       ██ ██  ██ ██    ██ ██ ████ ██ ██████  █████   ██████  
██    ██ ██    ██ ██           ██      ██        ██    ██   ██ ██          ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██      ██   ██ 
 ██████   ██████  ███████ ███████ ███████        ██    ██   ██ ███████     ██   ████  ██████  ██      ██ ██████  ███████ ██   ██ 
                                                                                                                                 
                                                                                                                                 
'''

print(logo)


print("Welcome to the number guessing game !!!")

def guess_the_number():
    print("I'm thinking of a number between 1 and 100\n")
    difficulty=input("Choose a Difficulty , Easy or Hard !!").lower()

    lives=0
    if difficulty=='hard':
        lives=5
    else:
        lives=10

    print(f"You have chosen {difficulty} difficulty, you have {lives} lives")

    computer_guess=random.randint(1,100)

    user_guess=0

    while user_guess!=computer_guess and lives!=0:
        
        user_guess=int(input("Make a Guess : "))

        if user_guess<computer_guess:
            print("Too low, guess again")
            lives-=1
            print(f"You have {lives} lives remaining !")

        elif user_guess>computer_guess:
            print("Too High, guess again")
            lives-=1
            print(f"You have {lives} lives remaining !")
        elif user_guess==computer_guess:
            print(f"You guessed the correct number : {computer_guess}")

        if lives==0:
            print(f"You have lost all your lives, You loose. The correct guess was {computer_guess}")


guess_the_number()
            


        
            
        