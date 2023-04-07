def draw_stair(height, width):
    for i in range(height):
        for f in range(width):
            print("#", end="")
        
        print("")
        width += 1

draw_stair(4, 1)