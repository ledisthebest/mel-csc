def exists_triangle(x: float, y: float, z: float) -> bool:

    a = x ** 2 + y ** 2 == z ** 2
    b = x ** 2 + z ** 2 == y ** 2
    c = y ** 2 + z ** 2 == x ** 2

    return a or b or c
    #z == (x ** 2 + y ** 2) ** 1/2

print(exists_triangle(3, 4, 5))