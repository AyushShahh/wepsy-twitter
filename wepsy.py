import tweepy
import time


auth = tweepy.OAuthHandler("nQRWNN72f7XGpEldU12fXPtfo", "zHCaShQWmCmYGlWpLJSrBQphsWSjGwhps2LuHe2Qa7yUDgTWyg")
auth.set_access_token("1431149377368756225-6fXtB5QB9aeYd57jysHW0pdwFhPtjk", "K5YFP5PafTJWsuEZxxoJru3WSCTY9jPaIkhv86Qe1CCaf")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Authentication OK")
    print("Running...\n")
except:
    print("Error during Authentication")


search = "#astrophotography OR from:NASA OR from:AstronomyMag OR from:NewsfromScience OR -donations -win -tools -btc -fund -funds -donation -stay -cosplay -safe -$LIGHT -bitcoin -join -podcast -staysafe -pod #lightning OR from:wired OR from:verge OR from:rajshamani OR from:mashable OR hubble OR #mountains OR HiRISE OR from:MarsMissionImgs OR #Todayinhistory -wion"
interval = 60 * 10

for tweet in tweepy.Cursor(api.search, search + "lang:en -filter:replies min_faves:10 min_retweets:2 -bollywood -celebrities -sex -art -porn -dick -pakistan -pilgrimage -ndma -sadhguru -boob").items():

    if not tweet.retweeted:

        try:
            tweet.retweet()
            print("I retweeted something you might like ;)")
            time.sleep(interval)

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break
