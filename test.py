def get_adjacent(r, c):

    m = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

    row_length = len(m)
    col_length = len(m[0])

    print(f"\ncord:{r},{c}")

    adj_elevation = []

    def larger(x, y):
        if x >= y:
            return x
        
        return y

    def smaller(x, y):
        if x >= y:
            return y
        
        return x

    # check if out of bound
    up_bound = larger(r - 1, 0)
    bt_bound = smaller(r + 1, row_length - 1)
    lf_bound = larger(c - 1, 0)
    rt_bound = smaller(c + 1, col_length - 1)

    print(up_bound,bt_bound,lf_bound,rt_bound)

    for row in range(up_bound, bt_bound + 1):
        for col in range(lf_bound, rt_bound + 1):
            print(f"{m[row][col]} at row {row} and col {col}")
            
            if not(row == r and col == c):
                adj_elevation.append(m[row][col])

    return adj_elevation


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