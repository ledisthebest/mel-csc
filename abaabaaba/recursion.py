def draw_pyramid(height): 
    
    if height <= 0:
        return   # end if no more layer to draw

    height -= 1
    draw_pyramid(height) # draw previous row
    
    for h in range(height):
        print("#", end="")
    
    print("")


draw_pyramid(5)