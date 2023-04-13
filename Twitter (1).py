#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Created on Monday Feb 27 04:58:42 2023

@author: Ahsan Ali Abbasi
@Description: A generic code to get data for a specific hashtag (Twitter)
@Accuracy: 97.8

"""

import snscrape.modules.twitter as sntwitter
import pandas
import time

#Here you just put a no like how much tweets you want to get
NoOfTweets=10

#Here I'm creating a list to add all the tweets
tweets_list2 = []

# This is used to see for how long this program run
start=time.time()

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('Put your TAG value here').get_items()):
    if i>NoOfTweets:
        break
    tweets_list2.append([tweet.replyCount,tweet.likeCount,tweet.date.date(), tweet.id, tweet.content, tweet.user.username,tweet.user.followersCount,tweet.retweetCount,tweet.lang,tweet.user.linkUrl,tweet.user.profileImageUrl, tweet.user.profileBannerUrl])
    
# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list2, columns=['Reply Count','Like Count','Datetime', 'Tweet Id', 'Text', 'Username','Followers Count','RetweetCount','Language','Link URL','Profile Image URL','Profile Banner'])

#Converting the total time to minutes by dividing by 60
minutes=(time.time()-start)/60
print(f'This code took {minutes:.2f} mins time to get data')

