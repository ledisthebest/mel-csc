from typing import List

def is_sink(m: List[List[int]], c: List[int]) -> bool:
    """
    Returns True if and only if c is a sink in m.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,2,3],
             [2,3,3],
             [5,4,3]]
    >>> is_sink(m, [0,0])
    True
    >>> is_sink(m, [2,2])
    True
    >>> is_sink(m, [3,0])
    False
    >>> m = [[1,2,3],
             [2,1,3],
             [5,4,3]]
    >>> is_sink(m, [1,1])
    True
    """
    #Your code goes here

    for i in range (c[0]-1, c[0]+2):
        for j in range(c[1]-1, c[1]+2):
            if i < 0:
                i = 0
            elif i > len(m)-1:
                i = len(m)-1
            if j < 0:
                j = 0
            elif j > len(m)-1:
                j = len(m)-1
            if c[0] > len(m)-1 or c[1] > len(m)-1 or m[i][j] < m[c[0]][c[1]]:
                return False
    return True


def find_local_sink(m: List[List[int]], start: List[int]) -> List[int]:
    """
    Given a non-empty elevation map, m, starting at start,
    will return a local sink in m by following the path of lowest
    adjacent elevation.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[ 5,70,71,80],
             [50, 4,30,90],
             [60, 3,35,95],
             [10,72, 2, 1]]
    >>> find_local_sink(m, [0,0])
    [3,3]
    >>> m = [[ 5,70,71,80],
             [50, 4, 5,90],
             [60, 3,35, 2],
             [ 1,72, 6, 3]]
    >>> find_local_sink(m, [0,3])
    [2,3]
    >>> m = [[9,2,3],
             [6,1,7],
             [5,4,8]]
    >>> find_local_sink(m, [1,1])
    [1,1]
    """
    #Your code goes here
    r, c = start
    elevation = m[r][c]

    while True:
        if not is_sink(m, [r, c]):  # if current location is not a sink
            # find the smallest ajacent elevation
            row_length = len(m)
            col_length = len(m[0])

            adj_elevation = []

            def larger(x, y):
                if x >= y:
                    return x
                
                return y

            def smaller(x, y):
                if x >= y:
                    return y
                
                return x

            # find the boundary index of adjacent values
            up_bound = larger(r - 1, 0)  # more than or equal to uptop index
            bt_bound = smaller(r + 1, row_length - 1)  # less than or equal to lowerest index
            lf_bound = larger(c - 1, 0)  # more than or equal to leftmost index
            rt_bound = smaller(c + 1, col_length - 1)  # less or equal to rightmost index

            for row in range(up_bound, bt_bound + 1):
                for col in range(lf_bound, rt_bound + 1):
                    
                    if not(row == r and col == c):
                        if m[row][col] < elevation:  # if location[row, col] is lower than current elevation [r,c].
                            elevation = m[row][col]  # save this location and elevation
                            r = row
                            c = col
            # after found the lowest adjacent elevation, check again to see if its a sink

        else: 
            break

    return [r, c]


m = [[ 5,70,71,80],
    [50, 4,30,90],
    [60, 3,35,95],
    [10,72, 2, 1]]

print(find_local_sink(m, [0,0]))

m = [[ 5,70,71,80],
    [50, 4, 5,90],
    [60, 3,35, 2],
    [ 1,72, 6, 3]]

print(find_local_sink(m, [0,3]))

m = [[9,2,3],
    [6,1,7],
    [5,4,8]]
print(find_local_sink(m, [1,1]))
