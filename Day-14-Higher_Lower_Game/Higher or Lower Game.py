"""
Game starts with two celebrities. We have to determine which of then have higher number of followers. 
If we are correct then we will be displayed with another set of celebrities.
For each correct guess we will get a point. The game ends when we make a wrong guess. 
Finally the score is displayed indicating the number of correct guess. 
"""
from Game_Data import data
import random 

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

Game_end_flag = False
Game_points = 0
Game_start_flag = 0
B = ''

B_Value = ""

def celeb():
    name = random.choice(data)
    return name

def compare(PA,PB):
    PA_Followers = PA["follower_count"]
    PB_Followers = PB["follower_count"]
    
    if PA_Followers > PB_Followers:
        return("a")
    else:
        return("b")

print(logo)

while not Game_end_flag:
    if Game_start_flag == 0:
        A = celeb()
        Game_start_flag += 1
    else:
         A = B
    print(f"Person A: {A['name']}, {A['description']} from {A['country']}")
    
    print(vs)
    
    B = celeb()
    if B != A:
        print(f"Person B: {B['name']}, {B['description']} from {B['country']}")
    else:
        B = celeb()
        print(f"Person B: {B['name']}, {B['description']}, from {B['country']}")
    
    print("\n")
    check = compare(A,B)
    User_Input = input("Who has higher followers A or B. Enter your choise: ")
    
    if User_Input.lower() == check:
        print("Great, You guessed it right!!")
        print("\n")
        Game_points += 1
    else:
        Game_end_flag = True
        print(f'Wrong!!, The correct answer is {check}')
        print("\n")
        print(f'Your final score is {Game_points} !!!')
        
        

##########################  ANGELA's Solution  ##########################
'''
from game_data import data
import random
from art import logo, vs
from replit import clear

def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = get_random_account()
  account_b = get_random_account()

  while game_should_continue:
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
      account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()

'''
'''
FAQ: Why does choice B always become choice A in every round, even when A had more followers? 

Suppose you just started the game and you are comparing the followers of A - Instagram (364k) to B - Selena Gomez (174k). 
Instagram has more followers, so choice A is correct. However, the subsequent comparison should be between Selena Gomez (the new A) and someone else. 
The reason is that everything in our list has fewer followers than Instagram. 
If we were to keep Instagram as part of the comparison (as choice A) then Instagram would stay there for the rest of the game. 
This would be quite boring. By swapping choice B for A each round, we avoid a situation where the number of followers of choice A keeps going up over the course of the game. Hope that makes sense :-)

'''