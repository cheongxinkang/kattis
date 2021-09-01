cup_swaps = input()

ball_position = 1

for swap in cup_swaps:
    if ball_position == 1:
        if swap == "A":
            ball_position = 2
        elif swap == "C":
            ball_position = 3
    elif ball_position == 2:
        if swap == "A":
            ball_position = 1
        elif swap == "B":
            ball_position = 3
    elif ball_position == 3:
        if swap == "B":
            ball_position = 2
        elif swap == "C":
            ball_position = 1
            
print(ball_position)
