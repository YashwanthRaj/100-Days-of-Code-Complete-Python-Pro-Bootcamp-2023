'''
To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. 

Then check for the number of times the letters in the word LOVE occurs. 

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:
"Your score is **z**."

'''

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = (name1 + name2).lower()

T = name.count('t')
R = name.count('r')
U = name.count('u')
E = name.count('e')
a = T+R+U+E

L = name.count('l')
O = name.count('o')
V = name.count('v')
E = name.count('e')
b=L+O+V+E

ab = (a*10) + b

if (ab < 10) or (ab > 90):
    print(f"Your score is {ab}, you go together like coke and mentos.")
elif (ab >= 40) and (ab <= 50):
    print(f"Your score is {ab}, you are alright together.")
else:
    print(f"Your score is {ab}")
