import random
from words import words
import string

#function to get a valid word without a sapce or -
def get_valid_word(words):
    #takes alist and chooses a random word
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)

    return word.upper()


def hangman():
    word=get_valid_word(words)
    word_letters=set(word) #letters in the word
    alphabet=set(string.ascii_uppercase) #list of all the alphabets
    used_letters=set()#used by the user 
    
    # No. of lives to player
    lives=8

    #getting user input
    while len(word_letters)>0 and lives!=0:
        #letters used
        print("you have", lives,"lives left and you used these letters:  ",' '.join(used_letters))

        #What current word is  (the word with missing  alphabets)
        word_list=[letter if letter in used_letters else '_' for letter in word]
        print ("current words: ",' '.join(word_list) )

        user_letter=input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("")

            else:
                lives=lives-1
                print("\n Your letter", user_letter ,"is not  in the word")    

        elif user_letter in used_letters:
            print("You have already used that caharacter. Please try again.")

        else:
            print("Invalid character. Please try again")

    if lives==0:
        print("You have died because you have failed to guess the word \n The word is",word)

    else:
        print("You are great human. You have decoded the word !! \n The word id : ", word)            

hangman()
