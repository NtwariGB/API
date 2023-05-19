import matplotlib.pyplot as plt
import tweepy
from textblob import TextBlob

# Configuration des clés d'API Twitter
consumer_key = "votre_consumer_key"
consumer_secret = "votre_consumer_secret"
access_token = "1504013770770857985-Himz3ohDQL8ao2lNqRZsGsu6KCxb5f"
access_token_secret = "N80IBKFVYBLQqRdoXDhOzWA3Diz7NEtuR0y094TRjFh8o"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Collecte des commentaires sur un sujet donné
query = "data science"  # Sujet de recherche
num_tweets = 100  # Nombre de tweets à collecter

tweets = tweepy.Cursor(api.search_tweets, q=query).items(num_tweets)

# Analyse de sentiment des commentaires collectés
positive_count = 0
negative_count = 0
neutral_count = 0

for tweet in tweets:
    comment = TextBlob(tweet.text)
    sentiment = comment.sentiment.polarity

    if sentiment > 0:
        positive_count += 1
    elif sentiment < 0:
        negative_count += 1
    else:
        neutral_count += 1

# Visualisation des statistiques de sentiment
labels = ["Positif", "Négatif", "Neutre"]
sizes = [positive_count, negative_count, neutral_count]
colors = ["green", "red", "gray"]

plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%")
plt.axis("equal")
plt.title("Répartition des sentiments des commentaires sur Twitter")
plt.show()
