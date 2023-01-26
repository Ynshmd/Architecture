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
d_moyennes2 = dict({})  

for x in mycol.aggregate( [{ "$project":{"_id" : 0, "prix":"$Listes_Voitures.prix", "Groupe" : 1}} ] ):
    if len(x['prix'])!=0:
        if x['Groupe'] in d_moyennes2:
            d_moyennes2[x['Groupe']]= d_moyennes2[x['Groupe']] + x['prix']
        else:
            d_moyennes2[x['Groupe']]= x['prix']
         

 
for cle,valeur in d_moyennes2.items():
    d_moyennes[cle]=round((sum(valeur) / len(valeur)),2)


    
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))
plt.suptitle('Moyenne de prix des groupes de voitures en ventes / Cote en Bourse', fontsize=16)
for cle,valeur in d_moyennes.items():
    ax1.bar(cle, valeur,color='red')
for x in mycol.find({},{ "_id": 0, "Marque": 1, "Groupe": 1, "Pourcentage 5 dernieres annees": 1, "Pourcentage 2021": 1 }):  
    ax2.bar(x['Groupe'], x['Pourcentage 5 dernieres annees'],color='red')
ax1.set_title('Prix des véhicules')
ax2.set_title('Pourcentage 2016-2021')
plt.subplots_adjust(left=0.04, right=0.99,  wspace=0.2, top=0.85) 
ax1.set_xticklabels(d_moyennes.keys(),rotation = 90)
ax2.set_xticklabels(d_moyennes.keys(),rotation = 90)
plt.show()