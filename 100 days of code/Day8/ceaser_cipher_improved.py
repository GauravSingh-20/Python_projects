alphabets=['a','b','c','d','e','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z']





def functions_performed(text,shift):
    if function_perform== 'encode':
        shift=shift*1
    else:
        shift=shift*(-1)

    cipher_text=""

    for letter in text:
        position=alphabets.index(letter)
        shifted_position=(position+shift)%len(alphabets)
        cipher_text+=alphabets[shifted_position]

    print("".join(cipher_text))
ans='y'
while ans=='y':
    function_perform=input("Tye 'encode' to encode message or 'decode' to decode the message : ").lower()
    text=input("Enter the text on which you want to perform the function : ")
    shift=int(input("Enter the shift you want to make : "))
    if function_perform=="encode":
        functions_performed(text,shift)
    elif function_perform=="decode":    
        functions_performed(text,shift)  
    else:
        print("You have enter an invalid option !!  Please try again")  

    ans=input("Do you want to continue using the program: (y/n) ?  ")  .lower() 
