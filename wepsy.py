from dotenv import load_dotenv
load_dotenv()
import os
import tweepy
import time

api_key = os.environ.get("api_key")
api_key_secret = os.environ.get("api_key_secret")
access_token = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Authentication OK")
    print("Running...\n")
except:
    print("Error during Authentication")


search = "#astrophotography OR from:NASA OR from:AstronomyMag OR from:ESA OR from:NatGeoTravel OR from:IndiaHistoryPic OR from:ForbesTech OR from:WIREDScience OR from:ScienceMagazine OR from:NewsfromScience OR from:wired OR from:verge OR from:rajshamani OR from:mashable OR hubble OR HiRISE OR from:MarsMissionImgs OR #Todayinhistory -WIONews OR from:Seeker OR from:archillect OR from:Positive_Call OR from:Inc"
interval = 60 * 8

for tweet in tweepy.Cursor(api.search, search + "lang:en -filter:replies min_faves:10 min_retweets:2").items():

    if not tweet.retweeted:

        try:
            tweet.retweet()
            print("I retweeted something you might like ;)")
            time.sleep(interval)

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break
