import csv
from collections import namedtuple
FrecuenciaNombre = namedtuple('FrecuenciaNombre', 'año,nombre,frecuencia,genero')
def leer_frecuencias_nombres(camino_csv):
    with open(camino_csv,mode='r' ,encoding="utf-8") as f :
        lector=csv.reader(f)
        next(lector)
        registros=[]
        for año,nombre,frecuencia,genero in lector :
            año=int(año)
            frecuencia=int(frecuencia)
            nombre=nombre.lower()
            genero=genero.lower()
            r=FrecuenciaNombre(año,nombre,frecuencia,genero)
            registros.append(r)
    return registros 

def filtrar_por_genero(lista_tupla,genero):
    lista=[]
    suma=0
    for t in lista_tupla :
        if genero in t.genero:
            suma+=1
    return lista 
def calcular_nombres(lista_tupla,genero):
    conjunto=set()
    for t in lista_tupla :
        if genero in t.genero:
            lista.append(t.nombre)
        elif genero==none :
             lista.append(t.nombre)
    return lista 
#def calcular_top_nombres_de_año (lista_tupla,año,genero,numero_limite):
