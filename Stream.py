#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import snscrape.modules.twitter as sntwitter
import pandas as pd
import streamlit as st
import datetime
import pymongo
import time 
client = pymongo.MongoClient("mongodb+srv://Gunavathy:1234@cluster0.j7dtaf6.mongodb.net/?retryWrites=true&w=majority") 
db = client.Twitter
records=db.scraping
tweets_df = pd.DataFrame()
dfm = pd.DataFrame()
st.write("# Welcome to Twitter scraping:speech_balloon:")
option = st.selectbox('How would you like the data to be searched?',('Keyword', 'Hashtag'))
word = st.text_input('Please enter a '+option, 'Example:Paleo')
word = st.text_input('Please enter a '+option, 'Paleo')
start = st.date_input("Select the start date", datetime.date(2022, 1, 1),key='d1')
end = st.date_input("Select the end date", datetime.date(2023, 1, 1),key='d2')
tweet_c = st.slider('How many tweets to scrape', 0, 1000, 5)
tweets_list = []
 
if word:
    if option=='Keyword':
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{word} + since:{start} until:{end}').get_items()):
            if i>tweet_c:
                if i>tweet_c-1:
                    break
            tweets_list.append([ tweet.id, tweet.date,  tweet.content, tweet.lang, tweet.user.username, tweet.replyCount, tweet.retweetCount,tweet.likeCount, tweet.source, tweet.url ])
        tweets_df = pd.DataFrame(tweets_list, columns=['ID','Date','Content', 'Language', 'Username', 'ReplyCount', 'RetweetCount', 'LikeCount','Source', 'Url'])
    elif option=='Hashtag':
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{word} + since:{start} until:{end}').get_items()):
            if i>tweet_c:
                if i>tweet_c-1:
                    break
            tweets_list.append([ tweet.id, tweet.date,  tweet.content, tweet.lang, tweet.user.username, tweet.replyCount, tweet.retweetCount,tweet.likeCount, tweet.source, tweet.url ])
        tweets_df = pd.DataFrame(tweets_list, columns=['ID','Date','Content', 'Language', 'Username', 'ReplyCount', 'RetweetCount', 'LikeCount','Source', 'Url'])
    else:
        st.warning(option,' cant be empty', icon="⚠️")

with st.sidebar:   
    st.info('DETAILS', icon="ℹ️")
    if option=='Keyword':
        st.info('Keyword is '+word)
    else:
        st.info('Hashtag is '+word)
    st.info('Starting Date is '+str(start))
    st.info('End Date is '+str(end))
    st.info("Number of Tweets "+str(tweet_c))
    st.info("Total Tweets Scraped "+str(len(tweets_df)))
    x=st.button('Show Tweets',key=1)

def convert_df(df):    
    return df.to_csv().encode('utf-8')

if not tweets_df.empty:
    col1, col2,col3 = st.columns(3)
    with col1:
        csv = convert_df(tweets_df) 
        c=st.download_button(label="Download data as CSV",data=csv,file_name='tweets_df.csv',mime='text/csv',)        
    with col2:   
        json_string = tweets_df.to_json(orient ='records')
        j=st.download_button(label="Download data as JSON",file_name="tweets_df.json",mime="application/json",data=json_string,)

    with col3:
     if st.button('Upload Tweets to Database'):
        coll=word
        coll=coll.replace(' ','_')+'_Tweets'
        mycoll=db[coll]
        dict=tweets_df.to_dict('records')
     if dict:
            mycoll.insert_many(dict) 
            ts = time.time()
            mycoll.update_many({}, {"$set": {"KeyWord_or_Hashtag": word+str(ts)}}, upsert=False, array_filters=None)
            st.success('Successfully uploaded to database', icon="✅")
            st.snow()
     else:
            st.warning('Cant upload because there are no tweets', icon="⚠️")

with st.sidebar:   
    st.write('Uploaded Datasets: ')
    for i in db.list_collection_names():
        mycollection=db[i]     
        if st.button(i):            
            dfm = pd.DataFrame(list(mycollection.find())) 
if c:
    st.success("The Scraped Data is Downloaded as .CSV file:",icon="✅")  
if j:
    st.success("The Scraped Data is Downloaded as .JSON file",icon="✅")     
if x: 
    st.success("The Scraped Data is:",icon="✅")
    st.write(tweets_df)
if not dfm.empty: 
    st.write( len(dfm),'Records Found')
    st.write(dfm) 





