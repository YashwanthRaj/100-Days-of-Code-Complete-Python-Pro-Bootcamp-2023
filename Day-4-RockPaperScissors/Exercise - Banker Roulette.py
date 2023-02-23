'''
You are going to write a program that will select a random name from a list of names. 
The person selected will have to pay for everybody's food bill.

'''
# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
max_num = len(names)

randNum = random.randint(0, max_num-1)
bill_name = names[randNum]
print(f"{bill_name} is going to buy the meal today!")