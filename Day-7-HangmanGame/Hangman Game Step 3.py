#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won. 

blank_bool = True
while blank_bool:
    guess = input("Guess a letter: ").lower()
    
    # Code to change blank values if correct guess
    for j in range(len(chosen_word)):
        if guess == chosen_word[j]:
            display[j]=guess
    
    # Code to stop the loop if all the values are filled with letters        
    if display.count('_') == 0:
        blank_bool= False
    print(display)
print("You win!!")