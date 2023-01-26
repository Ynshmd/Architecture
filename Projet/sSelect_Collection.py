import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
from dateutil import parser
import json 
from pymongo import MongoClient 


CONNECTION_STRING="mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.6.1"
client = MongoClient(CONNECTION_STRING)


print("Connexion établie")

mydb = client["Projet"]
mycol = mydb["PIB_Dep_Reg"]

for x in mycol.find({},{ "_id": 0, "Rang": 1, "Departements": 1, "PIB_dep_euros": 1, "Numero_Departement": 1, "Region": 1, "PIB_Region (en milliard d'euro)": 1 }):
        print(x)
