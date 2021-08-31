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


search = "#astrophotography OR #tonystark OR TASM OR lang:en from:@NASA OR #landscapes OR #sunsets OR -donations -win -tools -btc -fund -funds -donation -stay -cosplay -safe -$LIGHT -staysafe -bitcoin -join -podcast -pod (#lightning) OR #todayinhistory OR #galaxies OR hubble OR #mountains"
interval = 120

for tweet in tweepy.Cursor(api.search, search + "lang:en min_faves:10 min_retweets:2 -filter:replies -bollywood -celebrities -politics -sadhguru -art").items():

    if not tweet.retweeted:

        try:
            tweet.retweet()
            print("I retweeted something you like ;)")
            time.sleep(interval)

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break
