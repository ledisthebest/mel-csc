from typing import List
from termcolor import colored

def can_hike_to(m: List[List[int]], s: List[int], d: List[int], supplies: int) -> bool:
    
    current_elevation = m[s[0]][s[1]]
    r, c = s
    des_row, des_col = d
    supply = supplies
    
    row_length = len(m)
    col_length = len(m[0])
    
    
    while r <= des_row and c <= des_col:  # while we haven't got to the destination
        if r == des_row and c == des_col:
            return True
        
        def smaller(x, y):
            if x >= y:
                return y
            
            return x

        # if we are at southernmost and not at easternmost
        # if we are in the same row as the destination
        # or if to south cost is same as to east
        # or if to south cost is more expansive than east
        # and if supply is more than to east
            # to east
        
        # if we are at easternmost and not at southernmost
        # or if we are in the same col as the destination
        # or if to south coseis more expansive than east
        # and if supply is more than to east
            # to south
        
        to_east = -1
        to_south = -1 

        print(f"now at [{r}, {c}]: {current_elevation}") 

        if c < col_length and r < row_length:  # if we are not at the edgest row/col
            if c + 1 <= des_col:  # there is place to move right 
                to_east = abs(m[r][c + 1] - current_elevation)
                print(f"can go east[{r}, {c + 1}]: {m[r][c + 1]} and cost {to_east}")
            
            if r + 1 <= des_row:
                to_south = abs(m[r + 1][c] - current_elevation)
                print(f"can go south[{r + 1}, {c}]: {m[r + 1][c]} and cost {to_south}")

            """ if r + 1 < row_length and c + 1 < row_length:
                to_east = absolute(m[r][c + 1])
                to_south = absolute(m[r + 1][c]) """

        if to_east > -1 or to_south > -1:  # if any path(s) exist
            if to_east > -1 and ((to_south == -1) ^ (to_east <= to_south)) and supply >= to_east:  # if they are cost the same supply or is cheaper and enough supply to east
                supply -= to_east
                c += 1
                current_elevation = m[r][c]

            elif to_south > -1 and ((to_east == -1) ^ (to_south < to_east)) and supply >= to_south: # if is cheaper and enough supply to east
                supply -= to_south
                r += 1
                current_elevation = m[r][c]
            else:               
                return False
        
        else:
            print("no where to go")
            return False

        """ 
        if c != des_col and (r + 1 > row_length or r == des_row):  # if we are not on the same col as destination, and going south is out of bound, or we are on row the same as the destination
            if c + 1 < col_length:  # if going east is not out of bound 
                if c + 1 > row_length:
                    break
                # compare both direction
                to_south = absolute(m[smaller(r + 1, row_length - 1)][c] - current_elevation)
                to_east = absolute(m[r][smaller(c + 1, col_length - 1)] - current_elevation)
                if to_south >= to_east:  # if to south cost is same or more expansive than east
                    
                    if supply < to_south: # if supply is not enough
                        return False
                    else: 
                        supply -= to_south
                        c += 1
                        current_elevation = m[r][c]
        
        elif r != des_row and (c + 1 > col_length or c == des_col):  # if r is
            if c + 1 > col_length:   # if going east is out of bound
                if r +

            to_south = absolute(m[smaller(r + 1, row_length - 1)][c] - current_elevation)
            to_east = absolute(m[r][smaller(c + 1, col_length - 1)] - current_elevation)
            if to_south < to_south:
                
                if supply < to_south:
                    return False
                else:
                    supply -= to_south
                    r += 1
                    current_elevation = m[r][c]

    print("no where to go")
    return False """


m = [[1,4,3],
    [2,3,5],
    [5,4,3]]
print(colored(can_hike_to(m, [0,0], [2,2], 4), "red"))
#True
print(colored(can_hike_to(m, [0,0], [0,0], 0), "red"))
#True
print(colored(can_hike_to(m, [0,0], [2,2], 3),"red"))
#False

m = [[1,  1,100],
    [1,100,100],
    [1,  1,  1]]
print(colored(can_hike_to(m, [0,0], [2,2], 4), "red"))
#False
print(colored(can_hike_to(m, [0,0], [2,2], 202), "red"))
#True
