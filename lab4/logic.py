def string_xor(s1: str, s2: str) -> str:
    klee = ""

    for i in range(len(s1)): 
        if s1[i] == s2[i]:  # string index/slicing, like a list of character
            #False
            klee += '0'  # string concatenation
            #add 0 to the end klee
        else: #True
            klee += '1' 
            #add 1 to the end klee 
    return klee

    #对比每一位
        #发现一样的
        #叠在一起
        #消灭了
        #1+1=0
        #0+0=0
        #除此之外都是1
        #套公式就不会出错

print(string_xor("1011", "0111"))
print(string_xor("Mood", "Meow"))