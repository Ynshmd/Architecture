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


CONNECTION_STRING="mongodb://localhost:27017/"
client = MongoClient(CONNECTION_STRING)


print("Connexion établie")

mydb = client["FinalProjet"]
mycol = mydb["Bourses"]


for x in mycol.find({},{ "_id": 0, "Marque": 1, "Groupe": 1, "Pourcentage 5 dernieres annee": 1, "Pourcentage 2021": 1 }):
   
    plt.bar(x['Groupe'], x['Pourcentage 2021'],color='red')
    
plt.rcParams['figure.figsize']=(20, 10)    
plt.title('Bourse 2021 / Groupe')
plt.xlabel('Groupe')
plt.ylabel('Pourcentage 2021')
plt.ylabel('Pourcentage 2021')
plt.xticks(rotation = 90)
plt.show()