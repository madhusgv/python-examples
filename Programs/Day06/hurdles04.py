def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
        turn_left()
        move()
        turn_right()
        if front_is_clear():        
            move()
            turn_right()
            move()
            while (not wall_in_front()):
                move()
            turn_left()

#for x in range(1, 7):
while(not at_goal()): 
    if (wall_in_front()):
        jump()
    else:
        move()
