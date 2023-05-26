############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])



########################## Debugging - Solution for above code ##########################

# Describe Problem
# The range limits ends with value 19, hence i is not assigned 20 at any point
def my_function():
  for i in range(1, 21):  # When we change the limit to 21, hence the range ends with 21
    if i == 20:
      print("You got it")
my_function()


# Reproduce the Bug
# The number 6 for dice_num will give a index out of range error as dice_imgs index values are from 0 to 5 
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5) # We change (1,6) to (0,5)
print(dice_imgs[dice_num])


# Play Computer
# When we enter 1994, nothing happens as the the loop is considering values above and below 1994, but no specifications for when its equal
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994:  # Here we will specify equal sign too as well
  print("You are a Gen Z.")


# Fix the Errors
# The input takes in default as string. Hence we need to specify the datatype as int so that ">" can work
# The yellow message denotes a warning denoting that there is indentation missing aftre loop
# There is also f missing that denotes the f-string where we can include variable name 
age = int(input("How old are you?")) # We include int 
if age > 18:
    print(f"You can drive at age {age}.") # After we indent, the warning goes away and include f 


# Print is Your Friend
# In word_per_page variable, there is == operator used insted of =, hence the value remains 0 
# print used to check which section produces the error
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
#print(pages) - works fine
word_per_page = int(input("Number of words per page: "))  # Replace == with =
#print(word_per_page) - Value still remains 0, hence found out the that error is in above code
total_words = pages * word_per_page
print(total_words)


#Use a Debugger
# The append code line should exist inside the loop for all the values to get updated
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item) # Here we add tab to denote its inclusion inside the for loop which solve the problem
  print(b_list)
  
mutate([1,2,3,5,8,13])