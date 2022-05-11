import pandas, seaborn, matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math 

# Cargando datos
data = pd.read_csv("covid19_tweets.csv")

# Variables a trabajar
new_data = data[['user_followers','user_friends','user_favourites']]

# Diagrama de cajas y bigotes 
plt.boxplot(new_data)
plt.title('Grafica Boxplot')
plt.show()

# Mapas de calor 
np.random.seed(0)
sns.set_theme()
ax = sns.heatmap(new_data)

# Diagrama de dispersión
sns.pairplot(new_data)
plt.show()

