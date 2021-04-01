# import requests
# from bs4 import BeautifulSoup
#
# html = requests.get('https://www.instagram.com/ayush__mehta__/')
# soup = BeautifulSoup(html.text, 'html')
# item = soup.select_one("meta[property='og:description']")
# name = item.find_previous_sibling().get("content").split("•")[0]
# followers = item.get("content").split(",")[0]
# following = item.get("content").split(",")[1].strip()
# print(f'{name}\n{followers}\n{following}')
import instaloader

# Get instance
L = instaloader.Instaloader()
# username = input('Enter your username: ')
# password = input('Enter your password: ')
# password = input('Enter your password: ')
# Login or load session
#L.interactive_login(username)        # (login)
L.login('ayush__mehta__', 'ayushpalak10080906')
profile_in = input('Enter profile you want to explore: ')


# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, profile_in)

# Print list of followees and followers

# print('The list of Followers: \n')
followers = []
following = []
# count=0
for follower in profile.get_followers():
    followers.append(follower.username)
    # f1 = profile_in + " followers.txt"
    # file = open(f1,"a+")
    # file.write(follow_list[count])
    # file.write("\n")
    # file.close()
    # print(count, follow_list[count])
    # count = count + 1

# print('The list of Following: \n')
# follow_list = []
# count=0
for followee in profile.get_followees():
    following.append(followee.username)
    # f2 = profile_in + "folowees.txt"
    # file = open(f2,"a+")
    # file.write(follow_list[count])
    # file.write("\n")
    # file.close()
    # # print(count, follow_list[count])
    # count = count + 1

def Diff(li1, li2):
    return (list(set(li1) - set(li2)))

# fhand_followers = open(f1, 'r')
# fhand_following = open(f2, 'r')
count = 0
# followers = fhand_followers.read()
# followers = followers.split('\n')
# following = fhand_following.read()
# following = following.split('\n')
common = list()
for followee in following:
    for follower in followers:
        if followee == follower:
            common.append(followee)
dont_followback = Diff(following, common)
for person in dont_followback:
    count = count + 1
    print(count, person)