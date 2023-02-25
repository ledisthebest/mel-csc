def in_range(num) -> bool:
    a = num == 1
    b = num == 2
    c = num == 3

    return a or b or c


print(in_range(1.0))
print(in_range(2.5))
print(in_range(3))
print(in_range(7))