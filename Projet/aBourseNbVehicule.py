import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
from dateutil import parser
import json 
import seaborn as sns
from pymongo import MongoClient 
import warnings
warnings.filterwarnings('ignore')


CONNECTION_STRING="mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.6.1"
client = MongoClient(CONNECTION_STRING)


print("Connexion établie")

mydb = client["FinalProjet"]
mycol = mydb["Bourses_Voitures"]



nomcolonnes = dict({})  
    
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))
plt.suptitle('Nombre de véhicules en vente par Groupe / Cote en Bourse du Groupe', fontsize=16)
for x in mycol.find({},{ "_id": 0, "Marque": 1, "Groupe": 1, "Pourcentage 5 dernieres annees": 1, "Pourcentage 2021": 1, 'Listes_Voitures':1 }):    
    ax1.bar(x['Groupe'],len(x['Listes_Voitures']),color='red')
    nomcolonnes[x['Groupe']] = 0
for x in mycol.find({},{ "_id": 0, "Marque": 1, "Groupe": 1, "Pourcentage 5 dernieres annees": 1, "Pourcentage 2021": 1 }):
    ax2.bar(x['Groupe'], x['Pourcentage 2021'],color='red') 
ax1.set_title('Nombre de véhicules en vente par Groupe ')
ax2.set_title('Cote en Bourse')
plt.subplots_adjust(left=0.04, right=0.99, top=0.85) # ajuster la position et l'espacement des graphes
ax1.set_xticklabels(nomcolonnes.keys(),rotation = 90)
ax2.set_xticklabels(nomcolonnes.keys(),rotation = 90)
plt.show()