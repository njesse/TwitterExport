#!/usr/bin/env python
# coding: utf-8

# In[38]:


import twitter
api = twitter.Api(consumer_key=' ',
                      consumer_secret=' ',
                      access_token_key=' ',
                      access_token_secret=' ',
                 tweet_mode='extended')


# In[44]:


import time
list_of_tweets = []
status = api.GetStatus(1362090727220670465)
list_of_tweets.append(status.full_text)
while status.in_reply_to_status_id:
     status = api.GetStatus(status.in_reply_to_status_id)
     list_of_tweets.append(status.full_text)
     time.sleep(10)


# In[33]:


list_of_tweets.reverse() 


# In[34]:


list_of_tweets = [tweet.replace("@niesse","") for tweet in list_of_tweets]


# In[41]:


for tweet in list_of_tweets:
    print(tweet)

