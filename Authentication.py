
import tweepy
import webbrowser
import time



consumer_key = "-"
consumer_secret = "-"




callback_uri = 'oob'




auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)
redirect_url = auth.get_authorization_url()
print(redirect_url)




webbrowser.open(redirect_url)




user_pint_input = input("What's the pin value? ")





user_pint_input




auth.get_access_token(user_pint_input)




api = tweepy.API(auth)




me = api.me()



print(me.screen_name)






