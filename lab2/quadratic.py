def solver(a: float, b:float, c: float) -> float:

    a1 = (-b - (b ** 2 - 4 * a * c) ** .5) / (2 * a)
    a2 = (-b + (b ** 2 - 4 * a * c) ** .5) / (2 * a)

    if a1 > a2:
        return a1

    return a2


print(solver(2, -8, 6))