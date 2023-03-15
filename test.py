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


        same_row = False
        same_col = False
        if r == des_row:  # if we are in the same row as the destination
            same_row = True
        elif c == des_col:
            same_col = True
        
        # compare both direction
        to_south = abs(m[smaller(r + 1, row_length - 1)][c] - current_elevation)
        to_east = abs(m[r][smaller(c + 1, col_length - 1)] - current_elevation)

        print(f"Now at [{r}, {c}]: {current_elevation}, cost {to_south} to south or cost {to_east} to east")

        # find the lower change in elevation
        if (to_south >= to_east or same_row) and not same_col:  # if going south is more expansive than or eqaul to north
            print(f"east: {m[r][c + 1]}")
            # to East
            if supply < to_east:
                print("out of supply")
                return False
            
            supply -= to_east
            c += 1
            current_elevation = m[r][c]

        else:
            print(f"south: {m[r + 1][c]}")
            
            # to South
            if supply < to_south:
                print("out of supply")
                return False
            
            supply -= to_south
            r += 1
            current_elevation = m[r][c]
            
        # move again        
    print("no where to go")
    return False


m = [[1,4,3],
    [2,3,5],
    [5,4,3]]
print(colored(can_hike_to(m, [0,0], [2,2], 4), "red"))
#True
print(colored(can_hike_to(m, [0,0], [0,0], 0), "red"))
#True
print(colored(can_hike_to(m, [0,0], [2,2], 3), "red"))
#False

m = [[1,  1,100],
    [1,100,100],
    [1,  1,  1]]
print(colored(can_hike_to(m, [0,0], [2,2], 4), "red"))
#False
print(colored(can_hike_to(m, [0,0], [2,2], 202), "red"))
#True
