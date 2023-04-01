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


def create_tag_dictionary( \
        chirp_dictionary: Dict[int, Tuple[int, str, List[str], List[int], List[int]]]) \
        -> Dict[str, Dict[int, List[str]]]:
    """
    Creates a dictionary that keys tags to tweets that contain them.

    Note, some spacing has been added for human readability.

    >>> chirp_dictionary = create_chirp_dictionary("chirps.txt")
    >>> create_tag_dictionary(chirp_dictionary)
    {'': {1: ['Just landed on Mars and it feels amazing!']}, '2EZ': {1: ["Just tested the %Starship prototype and it's looking great! Can't wait for the next test! %2EZ %SpaceX %CEO"], 10: ['Just got a Victory Royale in a solo match! Feeling pumped and ready for more! %Gaming %2EZ']}, 'SpaceX': {1: ["Just tested the %Starship prototype and it's looking great! Can't wait for the next test! %2EZ %SpaceX %CEO"]}, 'Starship': {1: ["Just tested the %Starship prototype and it's looking great! Can't wait for the next test! %2EZ %SpaceX %CEO"]}, 'CEO': {1: ["Just tested the %Starship prototype and it's looking great! Can't wait for the next test! %2EZ %SpaceX %CEO"], 2: ['Just had a great meeting with the team discussing the future of %Twitter. Exciting things to come! %CEO %Future'], 4: ["Had a great meeting with some fellow philanthropists today. We're making progress on some important initiatives! %Philanthropy %Progress %CEO"]}, 'RichVibes': {1: ["I'm going to buy %twitter. %RichVibes"]}, 'Twitter': {1: ["I'm going to buy %twitter. %RichVibes"], 2: ['Just had a great meeting with the team discussing the future of %Twitter. Exciting things to come! %CEO %Future', 'Love seeing all the creative ways people are using Twitter. Keep it up! %Twitter %Creativity'], 7: ['Breaking news: The biggest movie of the year is coming soon! Stay tuned for updates. %Hollywood %Movies %Twitter']}, 'Future': {2: ['Just had a great meeting with the team discussing the future of %Twitter. Exciting things to come! %CEO %Future']}, 'Creativity': {2: ['Love seeing all the creative ways people are using Twitter. Keep it up! %Twitter %Creativity']}, 'Grammys': {3: ['Had an amazing time performing at the %Grammys tonight! Thank you to all my fans for your support! %Mu$ic %Blessed %TaylorFansRejoice']}, 'Mu$ic': {3: ['Had an amazing time performing at the %Grammys tonight! Thank you to all my fans for your support! %Mu$ic %Blessed %TaylorFansRejoice']}, 'Blessed': {3: ['Had an amazing time performing at the %Grammys tonight! Thank you to all my fans for your support! %Mu$ic %Blessed %TaylorFansRejoice']}, 'TaylorFansRejoice': {3: ['Had an amazing time performing at the %Grammys tonight! Thank you to all my fans for your support! %Mu$ic %Blessed %TaylorFansRejoice']}, 'Philanthropy': {4: ["Had a great meeting with some fellow philanthropists today. We're making progress on some important initiatives! %Philanthropy %Progress %CEO"]}, 'Progress': {4: ["Had a great meeting with some fellow philanthropists today. We're making progress on some important initiatives! %Philanthropy %Progress %CEO"]}, 'Gaming': {5: ['Love seeing all the amazing games coming out lately. The %Gaming industry is always evolving! %Youtube %Sam'], 10: ['Just got a Victory Royale in a solo match! Feeling pumped and ready for more! %Gaming %2EZ']}, 'Youtube': {5: ['Love seeing all the amazing games coming out lately. The %Gaming industry is always evolving! %Youtube %Sam']}, 'Sam': {5: ['Love seeing all the amazing games coming out lately. The %Gaming industry is always evolving! %Youtube %Sam']}, 'AI': {6: ["I'm going to reign over the world. Kneel before me. %AI %LLM %KingLife %humanssuck"]}, 'LLM': {6: ["I'm going to reign over the world. Kneel before me. %AI %LLM %KingLife %humanssuck"]}, 'KingLife': {6: ["I'm going to reign over the world. Kneel before me. %AI %LLM %KingLife %humanssuck"]}, 'humanssuck': {6: ["I'm going to reign over the world. Kneel before me. %AI %LLM %KingLife %humanssuck"]}, 'Hollywood': {7: ['Breaking news: The biggest movie of the year is coming soon! Stay tuned for updates. %Hollywood %Movies %Twitter']}, 'Movies': {7: ['Breaking news: The biggest movie of the year is coming soon! Stay tuned for updates. %Hollywood %Movies %Twitter']}, 'DepressionWednsday': {11: ['Sometimes I feel like a wilted rose, my petals falling one by one, leaving me bare and exposed... %DepressionWednsday %SadLife']}, 'SadLife': {11: ['Sometimes I feel like a wilted rose, my petals falling one by one, leaving me bare and exposed... %DepressionWednsday %SadLife']}}
    """
    #Your code goes here
    tag_dictionary = {"":{}}  # tag: {uid: message[a, b]}

    for chirp in chirp_dictionary:
        tags = chirp_dictionary[chirp][2]  # [tag0, tag1]
        uid = chirp_dictionary[chirp][0] # uid of the user that made this chirp
        message = chirp_dictionary[chirp][1]
        if len(tags) == 0:  # if chirp has no tags
            if uid in tag_dictionary[""]:  # if user had made other post with the same tag
                tag_dictionary[""][uid].append(message)  # add this chirp to tag:user:[]
            else:
                tag_dictionary[""].update({uid: [message]})  # create a new user and add chirp

        else: 
            for tag in tags:  # go through list of tags
                if not tag in tag_dictionary:  # if tag is not found in dictionary
                    tag_dictionary.update({tag: {uid: [message]}})
                
                else:
                    if uid in tag_dictionary[tag]: # if this user already made chirps with the same tag
                        tag_dictionary[tag][uid].append(message)

                    else:
                        tag_dictionary[tag].update({uid:[message]})

    return tag_dictionary


#print(create_profile_dictionary("profiles.txt"))
#print(create_chirp_dictionary("chirps.txt"))
#print(get_top_chirps(create_profile_dictionary("profiles.txt"), create_chirp_dictionary("chirps.txt"), 2))
print(create_tag_dictionary(create_chirp_dictionary("chirps.txt")))