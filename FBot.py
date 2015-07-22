__author__ = 'ndieks'

import bot


#Get user page feed
#This returns a list of dictionaries of the various posts

page=bot.my_bot.get_feed('me')
#print(page)

'''
Check post updater gender &&location
'''

#get post id for Photos
for post in page:
    dy=post['id']
    id=bot.get_post_id(dy)
    #Post like to the photos
    print("Id to like: "+id)
    print("User :"+post['fro'])
    #bot.my_bot.like_post(id)

#Done#
