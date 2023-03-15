def get_adjacent(r, c):

    m = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

    row_length = len(m)
    col_length = len(m[0])

    print(f"\ncord:{r},{c}")

    adj_elevations = []

    def larger(x, y):
        if x >= y:
            return x
        
        return y

    def smaller(x, y):
        if x >= y:
            return y
        
        return x

    # check if out of bound
    up_bound = larger(r - 1, 0)  # more than or equal to uptop index
    bt_bound = smaller(r + 1, row_length - 1)  # less than or equal to lowerest index
    lf_bound = larger(c - 1, 0)  # more than or equal to leftmost index
    rt_bound = smaller(c + 1, col_length - 1)  # less or equal to rightmost index

    print(up_bound,bt_bound,lf_bound,rt_bound)

    for row in range(up_bound, bt_bound + 1):
        for col in range(lf_bound, rt_bound + 1):
            print(f"{m[row][col]} at row {row} and col {col}")
            
            if not(row == r and col == c):
                adj_elevations.append(m[row][col])

    return adj_elevations


    """ for row in range(-1, 2):
        for col in range(-1, 2):
            if row != 0 or row == 2 or col != 0 or col == 2:
                adj_elevation.append(m[r + row][c + col])
    """

print(get_adjacent(0, 0))
print(get_adjacent(0, 1))
print(get_adjacent(1, 0))
print(get_adjacent(1, 1))
print(get_adjacent(2, 2))
"""for row in range(-1 , 2):
         
        if row - 1 > -1 and row + 1 < length:
            if m[row - 1][col] > elevation or m[row + 1][col] > elevation:  # check top and bottom
                ...
            if col - 1 > -1 and col + 1 < length:
                if m[row - 1][col - 1] > elevation or m[row + 1][col + 1] > elevation:  # check top-left and bottom-right
                    ... 
        
        if col - 1 > -1 and col + 1 < length:
            if m[row][col - 1] > elevation or m[row][col + 1] > elevation:  # check left and right
                ...
            if row - 1 > -1 and row + 1 < length:
                if m[row + 1][col - 1] > elevation or m[row - 1][col + 1] > elevation:  # check bottom-left and top-right
                    ...
    """
    """     
        if row - 1 > -1 and row + 1 < length:  # check top and bottom
            adj_elevation.append(m[row - 1][col])
            adj_elevation.append(m[row + 1][col])
            
            if col - 1 > -1 and col + 1 < length:  # check left and right
                adj_elevation.append(m[row][col - 1])
                adj_elevation.append(m[row][col + 1])
                # top-left and bottom-right
                adj_elevation.append(m[row - 1][col - 1])
                adj_elevation.append(m[row + 1][col + 1])

            if row - 1 > -1 and row + 1 < length: # check bottom-left and top-right
                adj_elevation.append(m[row + 1][col - 1])
                adj_elevation.append(m[row - 1][col + 1])
    """
    """ 
    if row == 0 or row == len(m) - 1 or col == 0 or col == len(m[row]) - 1:

        if  > c_height or m[row - 1][col + 1] > c_height or m[row][col + 1] > c_height or m[row + 1][col + 1] > c_height or m[row + 1][col] > c_height or m[row + 1][col - 1] > c_height or m[row][col - 1] > c_height or m[row - 1][col - 1]:



    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if i >= 0 and i < len(m) and j >= 0 and j < len(m[0]) and (i, j) != (row, col) and m[i][j] <= value:
                return False
    return True """