def classic_encode(s:str, key:int) -> str:

    new_str = ""
    for letter in s:

        new_str += chr(((ord(letter) - 97 + key) % 26) + 97)  #

    return new_str


print(classic_encode("abcxyz", 3))

#https://en.wikipedia.org/wiki/List_of_Unicode_characters

"""

Takes in a string containing only lowercase a-z letters, s, and
encodes it based off an offset value
key, following a classic Caesar cipher. See the examples below for
how to handle key values greater than 26
Examples:
>>> classic_encode("abc",3)
"def"
>>> classic_encode("xyz",5)
"cde"
>>> classic_encode("abc",26)
"abc"
>>> classic_encode("abc",53)
"bcd"
"""