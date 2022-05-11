#!/usr/bin/env python
# coding: utf-8

# In[14]:


import seaborn, matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

# Cargando datos
data = pd.read_csv("covid19_tweets.csv")

# Cantidad de datos que se tienen
datosVariable = data.count()
datosTotales = sum(data.count())
print("\n ---> Cantidad de datos por variable")
print(datosVariable)
print("\n ---> Cantidad de datos que se tienen = ",datosTotales)

# Variables que contiene cada vector
def variablesVector(matriz):
    variables = data.columns.values
    for i in range(0, len(variables)):
        print(variables[i])

print(" \n ---> Variables que contiene cada vector")
variablesVector(data)

# Tipo de variables
tiposVariables = data.dtypes
print("\n --->Tipos de variables")
print(tiposVariables)

# Rangos en los que se encuentran las variables
print("\n ---> Rango de user_followers = de ",data["user_followers"].min(), "hasta",data["user_followers"].max())
print("---> Rango de user_friends = de ",data["user_friends"].min(), "hasta",data["user_friends"].max())
print("---> Rango de user_favourites = de ",data["user_favourites"].min(), "hasta",data["user_favourites"].max())
print("---> Rango de user_verified  = de minimo",data["user_verified"].min(), "hasta maximo",data["user_verified"].max())
print("---> Rango de is_retweet = de minimo",data["is_retweet"].min(), "hasta maximo",data["is_retweet"].max())

# Diagrama de dispersión 
new_data = data[['user_followers','user_friends','user_favourites']]
sns.pairplot(new_data)
plt.show()

# Obtención de media, mediana y desviación estándar
estadistica = data.describe()
print("\n --->Media, Mediana y Desviación estándar")
print(estadistica)


# In[ ]:




