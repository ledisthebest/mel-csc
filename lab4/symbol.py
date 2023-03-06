SPECIAL_SYMBOLS = '!@#$%^&*()_+=[]?/'

def symbol_count(s):
    count = 0
    start_counting = False
    highest = 0 

    for character in s:
        if character in SPECIAL_SYMBOLS:
            if not start_counting:  # if character is a symbol and counting has not started
                count = 0  # reset counter and start counting
                start_counting = True
            count += 1
        else:  # when character is not a symbol
            start_counting = False
        
        if count > highest:
            highest = count
            
        #if symbol_started == True and symbol == SPECIAL_SYMBOLS:
            #set count + 1
        #if special symbols is not found
            #set symbol_started = False
        # #else add 1 to count
    return highest

print(symbol_count("H!!aa[][][][][][][][]ahhh?????"))