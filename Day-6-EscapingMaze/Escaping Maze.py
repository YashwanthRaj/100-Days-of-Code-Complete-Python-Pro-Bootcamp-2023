'''
Link for Challenge -> https://reeborg.ca/reeborg.html
Maze
Solution

'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    while wall_on_right():
        if front_is_clear():
            move()
            while at_goal():
                break
        else:
            turn_left()
    if not at_goal():
        turn_right()
        move()
    else:
        while at_goal():
            break
    
        
# Angela's Solution
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()