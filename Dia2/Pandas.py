#Importar Pandas
import pandas as pd

# Leer el archivo utilizando read_csv
data = pd.read_csv("avocado.csv")
# Obtener las primeras líneas utilizando head
data.head()

# Obtener diferentes combinaciones de columnas y datos
data.loc[13:17, ['Date', 'Total Volume', 'type']]

# Últimos datos de la tabla
data.tail(5)

# Datos obtenidos por la función describe
data.describe()

# ¿Cuántos objectos hay?
data.count()

# ¿Cuál es el valor de la variable 2 del objeto 15?
data.iloc[15, 2]

# ¿Cuál es el mínimo y máximo de la variable 3?
data.iloc[:, 3].describe()
