'''
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#e.g. 
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"

##HINT: How do you get the index of an item in a list:
#https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

#TODO-4: Create a function called 'decrypt' that takes the 'text' and 'shift' as inputs.

#TODO-5: Call the decrypt function and pass in the user inputs. You should be able to test the code and decrypt a message.
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text,shift_number):
    encoded_word=''
    
    for i in plain_text:
        inxe = alphabet.index(i)
        encoded_word+=alphabet[inxe+shift_number]
    
    print("The Encrypted message is: "+encoded_word)


def decrypt(plain_text,shift_number):
    decoded_word=''
    
    for i in plain_text:
        inex = alphabet.index(i)
        decoded_word+=alphabet[inex-shift_number]

    print("The Encrypted message is: "+decoded_word)


if direction == 'encode':
    encrypt(text,shift)
elif direction == 'decode':
    decrypt(text,shift)