#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install snscrape')


# In[2]:


get_ipython().system('pip install tqdm')


# In[3]:


import pandas as pd
from tqdm.notebook import tqdm
import snscrape.modules.twitter as sntwitter


# In[15]:


scraper=sntwitter.TwitterSearchScraper("#LIC")


# In[16]:


for tweet in scraper.get_items():
  break


# In[17]:


tweet


# In[7]:


tweet.date,tweet.id,tweet.url,tweet.user,tweet.content,tweet.replyCount,tweet.retweetCount,tweet.lang,tweet.source,tweet.likeCount


# In[8]:


scraper=sntwitter.TwitterSearchScraper("#LIC")
tweets=[]
for i, tweet in enumerate(scraper.get_items()):
    data=[tweet.date,tweet.id,tweet.url,tweet.user,tweet.content,tweet.replyCount,tweet.retweetCount,tweet.lang,tweet.source,tweet.likeCount]
    tweets.append(data)
    if i>50:
        break


# In[18]:


tweet_df=pd.DataFrame(tweets,columns=["date","id","url","user","content","replyCount","retweetCount","lang","source","likeCount"])


# In[10]:


tweet_df.to_csv("NGO_tweets.csv",index=False)


# In[11]:


scraper=sntwitter.TwitterSearchScraper("#NGO")
tweets=[]
for i, tweet in enumerate(scraper.get_items()):
    data=[tweet.date,tweet.id,tweet.url,tweet.user,tweet.content,tweet.replyCount,tweet.retweetCount,tweet.lang,tweet.source,tweet.likeCount]
    tweets.append(data)
    if i>50:
        break
        tweet_df=pd.DataFrame(tweets,columns=["date","id","url","user","content","replyCount","retweetCount","lang","source","likeCount"])
        tweet_df.to_csv("NGO_tweets")


# In[12]:


tweet_df


# In[13]:


import pandas as pd
from tqdm import tqdm
import snscrape.modules.twitter as sntwitter
scraper=sntwitter.TwitterSearchScraper("#NGO")
tweets=[]
n_tweets=1000
for i, tweet in tqdm(enumerate(scraper.get_items()), total=n_tweets):
    data=[tweet.date,tweet.id,tweet.url,tweet.user,tweet.content,tweet.replyCount,tweet.retweetCount,tweet.lang,tweet.source,tweet.likeCount]
    tweets.append(data)
    if i>n_tweets:
        break
        tweet_df=pd.DataFrame(tweets,columns=["date","id","url","user","content","replyCount","retweetCount","lang","source","likeCount"])
        tweet_df.to_csv("NGO_tweets.csv",index=False)


# In[14]:


tweet_df


# In[ ]:




