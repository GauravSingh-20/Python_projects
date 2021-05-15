############DEBUGGING#####################

# Describe Problem
# def my_function():
#   for i in range(1, 21):        #Change the  upper bound of range to 21
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)                              #Indexing is from 0 to 5, changed the upper bound of randint to 5
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year <= 1994:                    #Changed the < to <= to include year 1994   
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age =int(input("How old are you?"))               # Casted the input as int since it is compared to int  in next line
# if age > 18:                                      
#     print(f"You can drive at age {age}.")         # Indetation added to print and made the print statement as f string

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))   # Changed the == to =
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list =[]
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)           # Changed the indetation for b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])