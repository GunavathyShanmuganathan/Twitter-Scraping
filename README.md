# Twitter-Scraping
About the Project:
    Today, data is scattered everywhere in the world. Especially in social media, there may be a big quantity of data on Facebook, Instagram, YouTube, Twitter, etc. This consists of pictures and films on YouTube and Instagram as compared to Facebook and Twitter. To get the real facts on Twitter, you want to scrape the data from Twitter like (date, id, url, tweet content, user, reply count, retweet count, language, source, like count etc.) from twitter.
         Twitter Scrapping helps to scrape tweets with user provided keywords and hashtags in a given data range.
Approach: 
        By using the “snscrape” Library, the data is scraped from Twitter.
What is SNScrape? 
•	A scraper for social networking platforms known as snscrape (SNS). It retrieves objects, such as pertinent posts, by scraping things like date, id, url, tweet content, user, replycount, retweetcount, language, source, like count,user profiles, hashtags.

Install Snscrape 
          Snscrape requires Python 3.8 or higher. The Python package dependencies are installed automatically when you install Snscrape. You can install using the following commands. 
•	pip3 install snscrape 
•	pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git (Development Version)
Store each collection of data 
            After scraping store the each collection of data into a document into Mongodb along with the hashtag or key word we use to Scrape from twitter.
o	pip3 install pymongo
o	import pymongo


  Create a GUI using streamlit 
                    This application contains the feature to enter the keyword or hashtag to be searched, select the date range and limit the tweet count need to be scraped. After scraping, the data is displayed in the page and there is an option  to upload the data into Database. We can also download the scraped data into csv and json format.
Installation
        pip3 install streamlit.
  




