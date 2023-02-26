#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install dnspython')
get_ipython().system('pip install pymongo[srv]')


# In[4]:


import pymongo
client=pymongo.MongoClient("mongodb+srv://Gunavathy:1234@cluster0.j7dtaf6.mongodb.net/?retryWrites=true&w=majority")
db=client.Twitter
records=db.Scrape


# In[5]:


records.find_one()


# In[6]:


import pandas as pd


# In[7]:


data=pd.DataFrame(list(records.find()))
display(data)


# In[8]:


import pymongo
client=pymongo.MongoClient("mongodb+srv://Gunavathy:1234@cluster0.j7dtaf6.mongodb.net/?retryWrites=true&w=majority")
db=client.Twitter
records=db.Scraping


# In[9]:


records.find_one()


# In[10]:


import pandas as pd


# In[11]:


data=pd.DataFrame(list(records.find()))
display(data)


# In[ ]:




