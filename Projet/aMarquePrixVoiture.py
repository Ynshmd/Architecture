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



d_moyennes = dict({})  

for x in mycol.aggregate( [{ "$project":{"_id" : 0, "prix":"$Listes_Voitures.prix", "Marque" : 1}} ] ):
    m=0
    n=len(x['prix'])
    #print(x['Marque'],len(x['prix']))
    for cpt in x['prix']:
        m = m + cpt
    if(n==0):
        d_moyennes[x['Marque']] =0
    else:
        m = m/n
        d_moyennes[x['Marque']] = round(m , 2)

    




    
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))
plt.suptitle('Moyenne de prix des marques de voitures en ventes / Cote en Bourse', fontsize=16)
for cle,valeur in d_moyennes.items():
    ax1.bar(cle, valeur,color='red')
for x in mycol.find({},{ "_id": 0, "Marque": 1, "Groupe": 1, "Pourcentage 5 dernieres annee": 1, "Pourcentage 2021": 1 }):  
    ax2.bar(x['Marque'], x['Pourcentage 2021'],color='red')
ax1.set_title('Prix des véhicules')
ax2.set_title('Pourcentage 2021')
plt.subplots_adjust(left=0.04, right=0.99, wspace=0.01, top=0.85) # ajuster la position et l'espacement des graphes
ax1.set_xticklabels(d_moyennes.keys(),rotation = 90)
ax2.set_xticklabels(d_moyennes.keys(),rotation = 90)
plt.show()