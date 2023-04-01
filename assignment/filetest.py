from typing import List, Dict, Tuple

def create_profile_dictionary(file_name: str) \
        -> Dict[int, Tuple[str, List[int], List[int]]]:
    """
    Opens the file "file_name" in working directory and reads the content into a
    profile dictionary as defined on Page 2 Functions 1.

    Note, some spacing has been added for human readability.
    
    >>> create_profile_dictionary("profiles.txt")
    {100: ('Mulan', [300, 500], [200, 400]), 
    200: ('Ariel', [100, 500], [500]), 
    300: ('Jasmine', [500], [500, 100]), 
    400: ('Elsa', [100, 500], []), 
    500: ('Belle', [200, 300], [100, 200, 300, 400])}
    """
    #Your code goes here
    file = open(file_name, 'r')
    contents = file.readlines()  # save the whole file as list
    file.close()
    profile_dictionary = {}

    for i in range(0, len(contents), 5):  # count every 5 lines
        uid = int(contents[i].strip())
        name = contents[i + 1].strip()
        
        if not i + 2 >= len(contents):
            if contents[i + 2] != '\n':
                tags = contents[i + 2].strip().split(",") # list[x,y]
                for f in range(len(tags)):
                    if tags[f]:  # if element is not empty
                        tags[f] = int(tags[f].strip())  # convert number to int
            else:
                tags = []
        
        if not i + 3 >= len(contents):
            if contents[i + 3] != '\n':
                dislikes = contents[i + 3].strip().split(",")  # list[a,b]
                for f in range(len(dislikes)):
                    if dislikes[f]:
                        dislikes[f] = int(dislikes[f].strip())
            else:
                dislikes = []
        #profile_dictionary = {uid: (name, [x, y], [a, b] )}
        profile_dictionary.update({uid: tuple((name, tags, dislikes))})
        uid = name = tags = dislikes = None

    return profile_dictionary


def create_chirp_dictionary(file_name: str) \
        -> Dict[int, Tuple[int, str, List[str], List[int], List[int]]]:

    file = open(file_name, 'r')
    contents = file.readlines()  # save the whole file as list
    file.close()
    chirp_dictionary = {}

    for i in range(0, len(contents), 7):  # count every 7 lines
        cid = int(contents[i].strip())
        uid = int(contents[i + 1].strip())
        message = contents[i + 2].strip()

        if not i + 3 >= len(contents):
            if contents[i + 3] != '\n':
                tags = contents[i + 3].replace("\n", '').replace(" ", '').split(',')  # split into a list
            else:
                tags = []
        
        if not i + 4 >= len(contents):
            if contents[i + 4] != '\n':
                likes = contents[i + 4].replace("\n", '').replace(" ", '').split(',')
                for l in range(len(likes)):  # convert list items to interger
                    if likes[l]: # check if number exist
                        likes[l] = int(likes[l])
            else:
                likes = []

        if not i + 5 >= len(contents):
            if contents[i + 5] != "\n":
                dislikes = contents[i + 5].replace("\n", '').replace(" ", '').split(',')
                for d in range(len(dislikes)):
                    if dislikes[d]:
                        dislikes[d] = int(dislikes[d])
            else:
                dislikes = []

        #chirp_dictionary = {cid: (uid, message, [x, y], [a, b], [i, j])}
        chirp_dictionary.update({cid: tuple((uid, message, tags, likes, dislikes))})
        cid = uid = message = tags = likes = dislikes = None

    return chirp_dictionary


def get_top_chirps( \
        profile_dictionary: Dict[int, Tuple[str, List[int], List[int]]], \
        chirp_dictionary: Dict[int, Tuple[int, str, List[str], List[int], List[int]]],
        user_id: int)\
        -> List[str]:
    followings = profile_dictionary[user_id][2]  # id of following users

    feed = {}  # uid:[message, like_count]
    for chirps in chirp_dictionary:
        
        uid = chirp_dictionary[chirps][0]
        if uid in followings: #if chirp by is chirped by followed user
            message = chirp_dictionary[chirps][1]
            like_count = len(chirp_dictionary[chirps][3])
            
            if uid in feed:  # if there are other chirps of the same user in feed
                if like_count > feed[uid][1]:  # if chirps has more like than previous
                    feed.update({uid: [message, like_count]})
            else:
                feed.update({uid: [message, like_count]})
    
    top_chirps = []
    for f in feed:
        top_chirps.append(feed[f][0])

    return top_chirps


#print(create_profile_dictionary("profiles.txt"))
#print(create_chirp_dictionary("chirps.txt"))
print(get_top_chirps(create_profile_dictionary("profiles.txt"), create_chirp_dictionary("chirps.txt"), 2))