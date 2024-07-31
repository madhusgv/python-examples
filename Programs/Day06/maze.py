def turn_right():
    turn_left()
    turn_left()
    turn_left()

#for x in range(1, 7):
while(not at_goal()): 
    if (right_is_clear()):
        turn_right()
        move()
    elif (front_is_clear()):
        move()
    elif (wall_in_front() and wall_on_right()):
        turn_left()
    elif (wall_in_front() and not wall_on_right()):
        turn_right()
    elif (wall_on_right()):
        turn_left()
    else:
        move()

