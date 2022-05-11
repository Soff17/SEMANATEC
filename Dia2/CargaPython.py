import csv
import math

# DATOS GUARDADOS EN MATRIZ
def creaMatriz(nombre_archivo):
    with open(nombre_archivo, newline='') as archivo_csv:
        reader = csv.reader(archivo_csv)
        data = list(reader)
    return data

# EJERCICIO 1 
'''
¿Cuántos objetos hay?
'''
id=0
with open('avocado.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        id=id+1     
    print("Cantidad de objetos = ", id)

# EJERCICIO 2
'''
¿Cuál es el valor de la variable 2 del objeto 15?
'''
def valorObjeto(matriz,nrow):
    for i in range(1, len(matriz)):
        dato = float(matriz[nrow][2])
    print("Valor de la variable 2 del objeto 15",dato)

matriz = creaMatriz('avocado.csv')
getrow=int(input("Objeto a imprimir: "))
valorObjeto(matriz,getrow)

# EJERCICIO 3
'''
¿Cuál es el mínimo y máximo de la variable 3?
'''
def accederDatos(matriz, ncol):
    columna = []
    for i in range(1, len(matriz)):
        if not matriz[i][ncol]:
            dato = 0
        else:
            dato = float(matriz[i][ncol])
        columna.append(dato)
    return columna

matriz = creaMatriz('avocado.csv')
print("Maximo de la variable 3 = ", max(accederDatos(matriz,3)))
print("Minimo de la variable 3 = ", min(accederDatos(matriz,3)))
