# Analyse de sentiment des commentaires sur les médias sociaux

Ce projet vise à collecter des commentaires à partir d'une plateforme de médias sociaux, comme Twitter, et à effectuer une analyse de sentiment sur ces commentaires pour déterminer s'ils sont positifs, négatifs ou neutres. Ensuite, des statistiques sur la répartition des sentiments sont générées et visualisées à l'aide de graphiques.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les bibliothèques Python suivantes :

- Tweepy : Utilisé pour accéder à l'API Twitter et collecter les commentaires.
- TextBlob : Utilisé pour effectuer l'analyse de sentiment des commentaires.


## Utilisation du projet

1. Ouvrez le fichier "tweet.py" dans un éditeur de code.
2. Remplacez les valeurs des variables suivantes par vos propres clés d'API :
consumer_key = "votre_consumer_key"
consumer_secret = "votre_consumer_secret"
access_token = "votre_access_token"
access_token_secret = "votre_access_token_secret"


3. Définissez les paramètres de recherche en modifiant la valeur de la variable "query" :

4. Exécutez le script "tweet.py" pour collecter les commentaires correspondant à votre recherche.
5. Les commentaires seront affichés avec leur sentiment (positif, négatif ou neutre).
6. Les statistiques sur la répartition des sentiments seront générées et affichées sous forme de graphiques.

## Difficultés rencontres

- Accès à l'API de twitter