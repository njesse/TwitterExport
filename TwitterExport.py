#!/usr/bin/env python
# coding: utf-8

# In[2]:


import twitter
api = twitter.Api(consumer_key='...',
                      consumer_secret='...',
                      access_token_key='...',
                      access_token_secret='...',
                 tweet_mode='extended')


# In[3]:


import time
list_of_tweets = []
status = api.GetStatus(1362090727220670465)
list_of_tweets.append(status.full_text)
while status.in_reply_to_status_id:
     status = api.GetStatus(status.in_reply_to_status_id)
     list_of_tweets.append(status.full_text)
     time.sleep(3)


# In[5]:


list_of_tweets.reverse()
for tweet in list_of_tweets:
    tweet = tweet.replace("@niesse","")
    
for tweet in list_of_tweets:
    print(tweet)

