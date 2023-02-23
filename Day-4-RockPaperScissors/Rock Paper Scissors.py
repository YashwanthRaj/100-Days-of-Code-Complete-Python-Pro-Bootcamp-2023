import random

print("Welcome to Rock Paper Scissors Game!")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choise = input("Enter your choise: ").lower()
print("Your Choise is: ")
if choise == 'rock':
    print(rock)
elif choise == 'paper':
    print(paper)
elif choise == 'scissors':
    print(scissors)
else:
    print("Not recognized")

Comp_Choise_list = ["rock","paper","scissors"]
print("The computers Choise is: ")
Comp_Choise = Comp_Choise_list[random.randint(0,2)]
if Comp_Choise == 'rock':
    print(rock)
elif Comp_Choise == 'paper':
    print(paper)
else:
    print(scissors)

if choise == Comp_Choise:
    print("We have a draw!")
elif choise == 'rock' and Comp_Choise == 'paper':
    print("Computer wins!!")
elif choise == 'rock' and Comp_Choise == 'scissors':
    print("You win!!")
elif choise == 'paper' and Comp_Choise == 'rock':
    print("You win!!")
elif choise == 'paper' and Comp_Choise == 'scissors':
    print("Computer Wins!!")
elif choise == 'scissors' and Comp_Choise == 'rock':
    print("Computer Wins!!")
elif choise == 'scissors' and Comp_Choise == 'paper':
    print("You win!!")