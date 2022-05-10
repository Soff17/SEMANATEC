import math
import csv

# EJERCICIO 1
'''
Escribir una función de Python que encuentre los números primos en los primeros N números naturales.
N es el argumento de la función
Llamar la función desde el código principal
'''
def impares(n):
    naturales =[*range(1,n+1)]
    primos = []
    for i in range(2,len(naturales)):
        lsprimos = True
        for j in range(2,int(math.sqrt(naturales[i]))+1):
            if naturales[i] % j == 0:
                lsprimos = False
                break
        if lsprimos:
            primos.append(naturales[i])
    return primos

impares(20)

# EJERCICIO 2
'''
Escribir una función de Pyton que encuentre el producto cruz en vectores de 3 componentes.
La función recibe dos listas (vectores)
La función regresa un tercer vector (lista) con el resultado
Llamar a la función desde el código principal
'''
def cruz(a,b):
    c=[]
    c.append(a[1]*b[2]-a[2]*b[1])
    c.append(a[2]*b[0]-a[0]*b[2])
    c.append(a[0]*b[1]-a[1]*b[0])
    return c

x = [1.2,3.7,-0.25]
y = [-0.44,-2.8,7]
cruz(x,y)

# EJERCICIO 3
'''
Re-escribir el problema 2, pero ahora los vectores son leídos desde un archivo de texto.
'''
filas = []
with open("vectors.csv",'r') as file:
    csvr = csv.reader(file)
    for row in csvr:
        filas.append(row)
print(filas)
a =  [float(filas[0][0]),float(filas[0][1]), float(filas[0][2])]
b =  [float(filas[1][0]),float(filas[1][1]), float(filas[1][2])]
cr = cruz(a,b)
print("a= ",a)
print("b= ",b)
print("a x b= ", cr)
