def count_sentences(s):
    m1 = ".!?"
    count = 0
    str_start = False

    for character in s:
        #loop start
        if character.isupper():
            str_start = True

        if character in m1 and str_start:
            count += 1
            str_start = False
        #loop start
            
    return count

    #go through individual letter
        #find the first Capital letter and if found, that means the sentence has started
                #look for .!? and found them
                        #count +1 and restart 


print(count_sentences(input("Sentences:")))

"""
Returns the number of sentences which occur in a string s. Assume a
sentence is any substring
begins with a capital letter and completes the first time one of ".",
"!", or "?" occurs after said capital letter.
Examples:
>>> count_sentences("I like dogs. You like cats? I hate snakes!")
3
>>> count_sentences("i type like child!")
0
>>> count_sentences("Hmm, maybe...")
1
>>> count_sentences("this is a weIrd case?")
1
"""