from pymongo import MongoClient
import pandas as pd
import csv 
from dateutil import parser
import json 


# Connexion à la base de données MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["FinalProjet"]

# Construction de la pipeline d'agrégation
result=db["Bourses"].aggregate(pipeline = [
    {"$lookup":
        {
            "from": "Voiture_Brut",
            "localField": "Marque",
            "foreignField": "Marque",
            "as": "Listes_Voitures"
        }
    }
]);



new_collection = db["Bourses_Voitures"]
new_collection.insert_many(result)



# Fermeture de la connexion
client.close()
print("Les données ont bien été ajoutées !")
