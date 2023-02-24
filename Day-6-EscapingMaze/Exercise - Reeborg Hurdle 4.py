'''
Link for Challenge -> https://reeborg.ca/reeborg.html
Hurdle 4 
Solution

'''

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def climb1():
    while not right_is_clear():
        move()
        
def turn_1():
    turn_right()
    move()
    turn_right()

def go_down():
    while front_is_clear():
        move()
    turn_left()        

while not at_goal():
    if wall_in_front():
        turn_left()
        climb1()
        turn_1()
        go_down()
    else:
        move()
        
        
        
# Angela's Answer
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()        