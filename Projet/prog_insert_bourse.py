import pandas as pd
import csv 
from dateutil import parser
import json 
from pymongo import MongoClient 


def get_database():
    CONNECTION_STRING="mongodb://localhost:27017/"
    client = MongoClient(CONNECTION_STRING)
    return(client)

def create_db_collection(client):
    db=client['FinalProjet']
    collection_name=db["Bourses"]
    return(collection_name)
client=get_database()
collection_name=create_db_collection(client)

csvfile = pd.read_csv("Bourses.csv", sep=";")
reader = csv.DictReader( csvfile )

csvfile.replace('\\N', None, inplace = True)



header= [ "Marque","Groupe","Pourcentage 5 dernieres annees","Pourcentage 2021"]
collection_name.create_index('Rang')
db=client['FinalProjet']
csvfile = csvfile.head(30000)
output=csvfile.to_dict('records')


collection_name.insert_many(output)
print("Les données ont bien été ajoutées !")
