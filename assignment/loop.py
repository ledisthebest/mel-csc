e = 1
with open('chirps.txt') as f:
    lines = f.readlines()
chirp_dictionary = {}


cid = 0
uid = 0
message = ""
tags = []
likes = []
dislikes = []

i = 0
while i < len(lines):
    if e == 1:
        cid = int(lines[i])
        e += 1
    
    elif e == 2:
        uid = int(lines[i])
        e += 1
    
    elif e == 3:
        message = lines[i]
        words = message.split()
        for word in words:
            if(word.startswith("%")):
                e += 1
                break 
        if e != 4:
            tags = []
            e += 2
    
    elif e == 4:
        tags = lines[i].strip().split(",")
        e += 1
    
    elif e == 5:
        likes = lines[i].strip().split(",") # list[x,y]
        for f in range(len(likes)):
            if likes[f]:  # if element is not empty
                likes[f] = int(likes[f].strip())  # convert number to int
        e += 1
    
    elif e == 6:
        dislikes = lines[i].strip().split(",")  # list[a,b]
        for f in range(len(dislikes)):
            if dislikes[f]:
                dislikes[f] = int(dislikes[f].strip())
        e = 1
        i += 1
        chirp_dictionary.update({cid: tuple((uid, message, tags, likes, dislikes))})
        print(chirp_dictionary)
    i += 1


print(chirp_dictionary)