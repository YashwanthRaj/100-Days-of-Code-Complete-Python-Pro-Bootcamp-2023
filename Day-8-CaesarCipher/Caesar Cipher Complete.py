"""
Here we re-organise the code and make it more effitient

We can see that the encode and decode functions are very similar, hence we will combine them and improve effitiency 

Improve user Experience

"""
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alpha_size = len(alphabet)


def cipher(plain_text,shift_number):
    cipher_text=''
    
    if shift_number > alpha_size:
        shift_number = shift_number%alpha_size
        
       
    for i in plain_text:
        if i in alphabet:
            inex = alphabet.index(i)
            if direction == 'encode':
                cipher_text+=alphabet[inex+shift_number]
            else:
                cipher_text+=alphabet[inex-shift_number]
        else:
            cipher_text+=i
    
    print(f"The cipher message is: {cipher_text}")
   
    
ask = True

while ask:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))   
    cipher(text,shift)
    descision = input("Do you want to continue: ").lower()
    if descision == "no":
        ask = False
        print("See you soon, bye!!")