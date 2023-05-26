#  We need to Debug the following segments of code 

'''
Exercise 1 - Odd or Even


number = int(input("Which number do you want to check?"))

if number % 2 = 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
'''


number = int(input("Which number do you want to check?"))

if number % 2 == 0:  # We include ==, to check wether LHS equal to RHS 
  print("This is an even number.")
else:
  print("This is an odd number.")
  
  
'''
Exercise 2 - Leap year


year = input("Which year do you want to check?")

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
'''

year = int(input("Which year do you want to check?"))  # Here we include int() 

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  
'''
Exercise 3 - Fizz Buuz


for number in range(1, 101):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])
'''

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:  # Change or to and
    print("FizzBuzz")
  elif number % 3 == 0:  # Changing to elif
    print("Fizz")
  elif number % 5 == 0:  # Changing to elif
    print("Buzz")
  else:
    print(number)