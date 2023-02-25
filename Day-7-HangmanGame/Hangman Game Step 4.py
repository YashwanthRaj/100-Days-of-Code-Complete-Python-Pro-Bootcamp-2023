#Step 4
'''
#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

#TODO-2: - If guess is not a letter in the chosen_word,
#Then reduce 'lives' by 1. 
#If lives goes down to 0 then the game should stop and it should print "You lose."

#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

'''
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')
lives = 6
#Create blanks
display = []
for _ in range(word_length):
    display += "_"


blank_bool = True
while blank_bool:
    guess = input("Guess a letter: ").lower()
    
    # Check if choosen guess is in the word
    if guess not in chosen_word:
        lives-=1
    
    # Code to change blank values if correct guess
    for j in range(len(chosen_word)):
        if guess == chosen_word[j]:
            display[j]=guess

    # Code to stop the loop if all the values are filled with letters or lives over  
    print(stages[lives])
    print(display)    
    if display.count('_') == 0 and lives != 0:
        blank_bool= False
        print("You Win!!")
    elif display.count('_') !=0 and lives == 0:
        blank_bool= False
        print("You Loose!!")