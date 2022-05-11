# Pip install Tweepy if you don't already have the package
# !pip install tweepy

# Imports
import tweepy
import pandas as pd
import time

# Credentials hardcoded
####input your credentials here
ACCESS_TOKEN = ''
ACCESS_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

API_KEY = 'gkWDkY8vrg6fFNW3QzhhMTHmb'

API_secret_key = 'JyuQO12oqihDEZGehDvaYMcplIVuMaBgrcgKDZ9VpPXr8TPtfo'

bearer_token = 'AAAAAAAAAAAAAAAAAAAAABTHcQEAAAAAOxoyav%2FcpTxrHlvrQDqYpXlq%2F34%3DWioPlKnjquGm7M0GOd1W7QYvzwqQ0Q2j9ioDatYUJiecYjMgze'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Function created to extract coordinates from tweet if it has coordinate info
# Tweets tend to have null so important to run check
# Make sure to run this cell as it is used in a lot of different functions below
def extract_coordinates(row):
    if row['Tweet Coordinates']:
        return row['Tweet Coordinates']['coordinates']
    else:
        return None

# Function created to extract place such as city, state or country from tweet if it has place info
# Tweets tend to have null so important to run check
# Make sure to run this cell as it is used in a lot of different functions below
def extract_place(row):
    if row['Place Info']:
        return row['Place Info'].full_name
    else:
        return None

def scrape_text_query(text_query, max_tweets):
    # Creation of query method using parameters
    tweets = tweepy.Cursor(api.search,q=text_query, tweet_mode='extended',lang ="en").items(max_tweets)

    # List comprehension pulling chosen tweet information from tweets iterable object
    # Add or remove tweet information you want in the below list comprehension
    tweets_list = [[tweet.full_text, tweet.created_at, tweet.id_str, tweet.user.screen_name, tweet.coordinates,
               tweet.place, tweet.retweet_count, tweet.favorite_count, tweet.lang,
               tweet.source, tweet.in_reply_to_status_id_str, 
                tweet.in_reply_to_user_id_str, tweet.is_quote_status,
                ] for tweet in tweets]

    # Creation of dataframe from tweets_list
    # Add or remove columns as you remove tweet information
    tweets_df = pd.DataFrame(tweets_list,columns=['Tweet Text', 'Tweet Datetime', 'Tweet Id', 'Twitter @ Name', 'Tweet Coordinates', 'Place Info',
                                                 'Retweets', 'Favorites', 'Language', 'Source', 'Replied Tweet Id',
                                                  'Replied Tweet User Id Str', 'Quote Status Bool'])

    # Checks if there are coordinates attached to tweets, if so extracts them
    tweets_df['Tweet Coordinates'] = tweets_df.apply(extract_coordinates,axis=1)
    
    # Checks if there is place information available, if so extracts them
    tweets_df['Place Info'] = tweets_df.apply(extract_place,axis=1)

    # Uncomment/comment below lines to decide between creating csv or excel file 
    tweets_df.to_csv('{}-tweets.csv'.format(text_query), sep=',', index = False)
#     tweets_df.to_excel('{}-tweets.xlsx'.format(text_query), index = False)


# Input search query to scrape tweets and name csv file
text_query = 'organic food'

# Max recent tweets pulls x amount of most recent tweets from that user
max_tweets = 15000

# Function scrapes for tweets containing text_query, attempting to pull max_tweet amount and create csv/excel file containing data.
scrape_text_query(text_query, max_tweets)

