#################################  Guess Number Game  #################################

'''
Number Guessing Game
The computer selects a number that we have to guess. We have to correctly guess that number to win the game. 
Two difficulty levels are present. Easy level will give you 10 chances. Hard level will give you only 5 chances.
With every guess entered by us, it should display low or high by comparing our guess and computers selected number. 

'''

start_logo = '''

╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭━━━━┳╮╱╱╱╱╱╭━╮╱╭╮╱╱╱╱╱╭╮
┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱┃╭╮╭╮┃┃╱╱╱╱╱┃┃╰╮┃┃╱╱╱╱╱┃┃
┃┃╱╰╋╮╭┳━━┳━━┳━━╮╰╯┃┃╰┫╰━┳━━╮┃╭╮╰╯┣╮╭┳╮╭┫╰━┳━━┳━╮
┃┃╭━┫┃┃┃┃━┫━━┫━━┫╱╱┃┃╱┃╭╮┃┃━┫┃┃╰╮┃┃┃┃┃╰╯┃╭╮┃┃━┫╭╯
┃╰┻━┃╰╯┃┃━╋━━┣━━┃╱╱┃┃╱┃┃┃┃┃━┫┃┃╱┃┃┃╰╯┃┃┃┃╰╯┃┃━┫┃
╰━━━┻━━┻━━┻━━┻━━╯╱╱╰╯╱╰╯╰┻━━╯╰╯╱╰━┻━━┻┻┻┻━━┻━━┻╯
'''
import random

Comp_number = 0 
attempts_remaining = 0

def comp_guess():
    global Comp_number
    Comp_number = random.randint(0,100)

comp_guess()  # This will assign a new variable for the computer to guess
print(start_logo)
print("Welcome to the Number Guessing Game!!")
print("I will select a number betwen 0 to 100, You have to guess it!!")
ask_Difficulty = input("Please enter your difficulty level (Easy / Hard): ")

if ask_Difficulty.lower() == 'hard':
    attempts_remaining = 5
    print("We shall begin. Hard level gives you 5 chances to guess!!")
elif ask_Difficulty.lower() == 'easy':
    attempts_remaining = 10
    print("We shall begin. Easy level gives you 10 chances to guess!!")
else:
    print("Invalid input!!")
    

Win_Flag = False    

while attempts_remaining != 0:
    guess = int(input("Enter Guess: "))
    if guess > Comp_number:
        print("High")
        attempts_remaining = attempts_remaining - 1
        print(f"You have {attempts_remaining} attempts remaining!!")
    elif guess < Comp_number:
        print("Low")
        attempts_remaining = attempts_remaining - 1
        print(f"You have {attempts_remaining} attempts remaining!!")
    else:
        print("Correct!!!")
        attempts_remaining = 0
        Win_Flag = True
    

if Win_Flag:
    print("You have won the game!!!")
else:
    print("You have exhausted all your attempts!!!")
    print(f"The computer's guess was: {Comp_number}")
    print("You Looseeeeeeee")
    
    
    
    
#####################   Angela's Solution #####################   
'''

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""


from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()
'''