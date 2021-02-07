

import random
import tweepy

consumer_key = "-"
consumer_secret = "-"

callback_uri = 'oob'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)
redirect_url = auth.get_authorization_url()
print(redirect_url)


user_pint_input = input("What's the pin value? ")

user_pint_input



auth.get_access_token(user_pint_input)

api = tweepy.API(auth)


me = api.me()

Moneda = "aaaaaaaaaaaaaaa"
positiu = "nanan"
import nltk
import pickle
import pandas as pd

def postt(Moned, positiv) :
    if Moned != "nada tete":
        print ("amo a publika")
        numerolio = random.randint(0, 999999)
        if positiv == 1:
            print ("amo a publika positivo")
            api.update_status(f"There is a famous person talking good about {Moned}{numerolio}" )
        elif positiv == 0:
            print ("amo a publika negativo")
            api.update_status(f"There is a famous person talking shit about {Moned}{numerolio}") 
        Moned = "nada tete"
        
f = open('./model_sentiment.pickle', 'rb')
classifier = pickle.load(f)
f.close()

f = open('./dictionary.pickle', 'rb')
vocabulary = pickle.load(f)
f.close()

def extract_features(review):
    review_words=set(review)
    features={}
    for word in vocabulary:
        features[word]=(word in review_words)
    return features
#LECTURA DATASET DE CRIPTOS###############################################
data=pd.read_csv('data_bitcoins.csv',index_col=0)
x=data.to_dict()
lista=list(x.values())
cryptos=lista[0]
######################################################################

cryptos_list1 = []
abreujaments_incomplerts = list(cryptos.keys())

abreujaments = ["$" + suit for suit in abreujaments_incomplerts]

cryptos_list1 = list(cryptos.values()) +list(abreujaments)
print ("final:", cryptos_list1)

cryptos_list = cryptos_list1


twit="hjj"
import tweepy

class TweetsListener(tweepy.StreamListener):
    def on_connect(self):
        print("Working")
    
    def on_status(self,status):  #aqui es pot guardar una base de dades de piulades actuals
        print(status.text)
        twit1= status.text
        twit = twit1
        for i in cryptos_list:
            for word in twit.split():
                if i.lower() == word.lower():
                    print ("detectada moneda en twit")
                    problemInstance = twit.split()
                    problemFeatures = extract_features(problemInstance)
                    tal = classifier.classify(problemFeatures)
                    Moneda = i
                    #print (Moneda, positiu)
                    positiu = "nanan"
                
                    if tal == "positive":
                        print ("positiu")
                        positiu = 1
                    
                    elif tal=="negative":
                        positiu = 0
                        print ("negatiu")
                    postt(Moneda, positiu)
                
    def on_error(self,status_code):
        print("Error",status_code)

   


consumer_key = "-"
consumer_secret = "-"
access_token = "-"
access_token_secret = "-"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit_notify=True, wait_on_rate_limit=True)

stream = TweetsListener()
streamingApi= tweepy.Stream(auth=api.auth, listener=stream)
#follow ens diu a qui esta escoltant l'stream tweet
#track ens diu una llista del que passa
streamingApi.filter(
    follow=["2307220706",  "797718721989066752"]   
    )


# In[ ]:





# In[ ]:




