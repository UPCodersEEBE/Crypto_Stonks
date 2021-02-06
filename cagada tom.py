
import nltk
import pickle
import pandas as pd
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
            if i in twit.split():
                print ("detectada moneda en twit")

                problemInstance = twit.split()
                problemFeatures = extract_features(problemInstance)
                tal = classifier.classify(problemFeatures)
               
                
                if tal == "positive":
                    print("tete invierte en", i)
                elif tal=="negative":
                    print("tete no inviertas en", i)
                
    def on_error(self,status_code):
        print("Error",status_code)

   
    
    

consumer_key = "y9iuklm5x6J00j1jST7xMvELc"
consumer_secret = "p3OsGkS8vPHrL3VGPfJS1yPUiTwbrxt7eyPH9uGvpLfcHRTX6b"
access_token = "2307220706-lHanCvNdgV9v7irKnrKwmNpeRsczsoYOjjhEMvA"
access_token_secret = "PoRfn9EnqiqHTx6D9HozWc4AdwYLAYB0QKGrxRlsCDS8S"

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

