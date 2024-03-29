from typing import List

def get_average_elevation(m: List[List[int]]) -> float:
    """
    Returns the average elevation across the elevation map m.

    Examples
    >>> get_average_elevation([])
    0
    >>> m = [[1,2,3],[4,5,6],[7,8,9]]
    >>> get_average_elevation(m)
    5.0
    >>> m = [[1,2,2,5],[4,5,4,8],[7,9,9,1],[1,2,1,4]]
    >>> get_average_elevation(m)
    4.0625
    """
    #Your code goes here
    if not m:
        return 0

    total_elevation = 0
    number_elements = 0

    for average in m:
        for elevation in average:
            total_elevation += elevation
            number_elements += 1

    average_elevation = total_elevation / number_elements

    return average_elevation 
    

def find_peak(m: List[List[int]]) -> List[int]:
    """
    Given an non-empty elevation map m, returns the cell of the
    highest point in m.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,2,3],
             [9,8,7],
             [5,4,6]]
    >>> find_peak(m)
    [1,0]
    >>> m = [[6,2,3],
             [1,8,7],
             [5,4,9]]
    >>> find_peak(m)
    [2,2]
    """
    #Your code goes here
    height = m[0][0]
    peak = [0,0]

    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] > height:
                height = m[i][j]
                peak = [i, j]
            
    return peak
            

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
    row = c[0]
    col = c[1]
    elevation = m[row][col]

    length = len(m)
    
    if row >= length and col >= length:
        return False

    adj_elevations = get_adjacent(m, row, col)
    
    for adjacent in adj_elevations:
        if adjacent < elevation:
            return False

    return True


def get_adjacent(m: List[List[int]], r: int, c: int) -> List[int]:

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

    # check if out of bound
    up_bound = larger(r - 1, 0)
    bt_bound = smaller(r + 1, row_length - 1)
    lf_bound = larger(c - 1, 0)
    rt_bound = smaller(c + 1, col_length - 1)

    print(up_bound,bt_bound,lf_bound,rt_bound)

    for row in range(up_bound, bt_bound + 1):
        for col in range(lf_bound, rt_bound + 1):
            
            if not(row == r and col == c):
                adj_elevation.append(m[row][col])

    return adj_elevation
    

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

    row = start[0]
    col = start[1]

    cur_val = m[row][col]

    length = len(m)
    if row >= length and col >= length:
        return False
    
    adj_sinks = get_adjacent(m, row, col)
    
    cur_valmin(adj_sinks)

    #when entering value outside of range of m
        #returns empty list

    #place = [0,0]
    
    #for i first level number of big lists -1
        #for j second level number of values within lists -1
            #use is_sink function to analyze values
        #if True:
            #return their position [i,j]
        #elif is false:
            #find smaller value around it and store it in place
            #continue to use value stored in place to redo loop
            #once no smaller values around are found
    #return place

    """ 
    place = [0,0]
    cur_val = 0
    smal_val = 0
    smal_val_pos = [0,0]
    
    for i in range(start[0]-1, start[0]+2):
        for j in range(start[1]-1, start[1]+2):
            if is_sink(m,[i,j]) == True:
                return [i,j]
            elif is_sink(m,[i,j]) == False:
                cur_val = m[i][j]
                #smal_val = 
                #this part needs some work
                if cur_val > smal_val:
                    cur_val = smal_val
                
            smal_val_pos = [i,j]

        return smal_val_pos  """

    
def can_hike_to(m: List[List[int]], s: List[int], d: List[int], supplies: int) -> bool:
    """
    Given an elevation map m, a start cell s, a destination cell d, and
    the an amount of supplies returns True if and only if a hiker could reach
    d from s using the strategy dscribed in the assignment .pdf. Read the .pdf
    carefully. Assume d is always south, east, or south-east of s. The hiker
    never travels, north, west, nor backtracks. 

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,4,3],
             [2,3,5],
             [5,4,3]]
    >>> can_hike_to(m, [0,0], [2,2], 4)
    True
    >>> can_hike_to(m, [0,0], [0,0], 0)
    True
    >>> can_hike_to(m, [0,0], [2,2], 3)
    False
    >>> m = [[1,  1,100],
             [1,100,100],
             [1,  1,  1]]
    >>> can_hike_to(m, [0,0], [2,2], 4)
    False
    >>> can_hike_to(m, [0,0], [2,2], 202)
    True
    """
    #Your code goes here


"""
You are not required to understand or use the code below. It is there for
curiosity and testing purposes.
"""
def create_real_map()-> List[List[int]]:
    """
    Creates and returns an elevation map from the real world data found
    in the file elevation_data.csv.

    Make sure this .py file and elevation_data.csv are in the same directory
    when you run this function to ensure it works properly.
    """
    data = open("elevation_data.csv")
    m = []
    for line in data:
        m.append(line.split(","))
    data.close()
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = int(m[i][j])
    return m
    
    










    
