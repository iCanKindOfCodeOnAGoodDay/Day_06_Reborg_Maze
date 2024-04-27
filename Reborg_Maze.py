while at_goal() == False:
    if right_is_clear():
        turn_left()
        turn_left()
        turn_left()
        move()

    elif front_is_clear():
        move()

    else:
        turn_left()
        if front_is_clear():
            move()
    

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
