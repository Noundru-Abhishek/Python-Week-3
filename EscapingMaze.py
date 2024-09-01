def navigate_maze():
    while not at_goal():
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Assume Reeborg starts at (3, 5) and needs to get to (6, 4)
navigate_maze()
