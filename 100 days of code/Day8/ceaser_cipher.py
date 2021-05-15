alphabets=['a','b','c','d','e','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z']

function_perform=input("Tye 'encode' to encode message or 'decode' to decode the message : ").lower()
text=input("Enter the text on which you want to perform the function : ")
shift=int(input("Enter the shift you want to make : "))

def encrypt(text,shift):

    cipher_text=""
    for letter in text:
        position=alphabets.index(letter)
        shifted_position=(position+shift)%len(alphabets)
        cipher_text+=alphabets[shifted_position]

    print("".join(cipher_text))

def decrypt(text,shift):
    normal_text=""
    for letter in text:
        position=alphabets.index(letter)
        shifted_position=(position-shift)%len(alphabets)
        normal_text+=alphabets[shifted_position]

    print("".join(normal_text))

if function_perform=="encode":
    encrypt(text,shift)
elif function_perform=="decode":    
    decrypt(text,shift)  
else:
    print("You have enter an invalid option !!  Please try again")     
