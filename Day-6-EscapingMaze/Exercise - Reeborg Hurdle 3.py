'''
Link for Challenge -> https://reeborg.ca/reeborg.html
Hurdle 3 
Solution

'''

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump1():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump1()
    else:
        berak