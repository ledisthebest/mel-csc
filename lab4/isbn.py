def isISBN(code: str) -> bool:
    sums = 0

    for place in range(len(code) - 1):
        sums += int(code[place]) * (1 + place)

    if sums % 11 == 10:
        return True

    return False


def isISBNdash(n) -> bool:
    if len(n) == 13 and n.count('-') == 3:  # if code length is 13 with 3 dashes
        if n[1] == '-' and n[5] == '-' and n[11] == '-':  # and 3 dashes are in the right place
            if isISBN(n.replace('-', '')):
                
                return True

    return False


print(isISBN('020103803X'))
print(isISBN('020108303X'))
print(isISBNdash('0-201-03803-X'))
print(isISBNdash('0201-03803-X'))
