'''
Link for Challenge -> https://reeborg.ca/reeborg.html
Hurdle 1 
Solution

'''

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump1():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for i in range(0,6):
    jump1()