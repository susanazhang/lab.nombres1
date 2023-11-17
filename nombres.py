import csv
from collections import namedtuple
FrecuenciaNombre = namedtuple('FrecuenciaNombre', 'año,nombre,frecuencia,genero')
#actividad 1 recibe la ruta de un fichero CSV codificado en UTF-8,
# y devuelve una lista de tuplas de tipo FrecuenciaNombre(int, str, int, str) conteniendo todos los datos almacenados en el fichero.
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
#actividad 2 recibe una lista de tuplas de tipo FrecuenciaNombre y un género de tipo str, 
# y devuelve una lista de tuplas de tipo FrecuenciaNombre con los registros del género recibido como parámetro.
def filtrar_por_genero(registro,genero):
    lista=[]
    for t in registro :
        if genero in t.genero:
            lista.append(t)
    return lista 
#actividad 3 recibe una lista de tuplas de tipo FrecuenciaNombre y un género de tipo str, y devuelve un conjunto {str} con los nombres del género recibido como parámetro.
#  El género puede ser 'Hombre', 'Mujer' o tener un valor None, en cuyo caso se incluyen en el conjunto todos los nombres. El valor por defecto del género es None.
def calcular_nombres(registro,genero = None ):# hay que poner genero:optional[str]=None->set[str] cuando hay on none pq que no me de error 
    lista=set()
    for t in registro:
        if genero in t.genero:
            lista.add(t.nombre)
        elif genero==None :
             lista.add(t.nombre)
    return lista 

#actividad 4 recibe una lista de tuplas de tipo FrecuenciaNombre, un año de tipo int,
#  un número límite de tipo int y un género de tipo str, y devuelve una lista de tuplas (nombre, frecuencia) de tipo (str, int)
#  con los nombres más frecuentes del año y el género dados, ordenada de mayor a menor frecuencia, y con un máximo de límite nombres. 
# El género puede ser 'Hombre', 'Mujer' o tener un valor None, en cuyo caso se incluyen en la lista todos los nombres. 
# El valor por defecto del límite es 10 y el del género es None.
def calcular_top_nombres_de_año (registro,año,genero = None, limite = 10):
    if genero is not None :
        registro = filtrar_por_genero(registro, genero)
    lista = []
    for x in registro:
        if x.año == año:
            lista.append((x.frecuencia,x.nombre))
    lista.sort(key = lambda x:x[0], reverse=True) # reverse false para que vaya de menor a mayor y true para que vaya de mayor a menor
    return lista[:limite]
#actividad 5 recibe una lista de tuplas de tipo FrecuenciaNombre, y devuelve un conjunto {str} con los nombres que han sido utilizados en ambos géneros.
def calcular_nombres_ambos_generos(registro): #el metodo .intercection te devuelve las cosas que se repiten 
    lista1=[]
    lista2=[]
    for x in registro:
        if x.genero=="mujer":
            lista1.append(x.nombre)
        if x.genero=="hombre":
            lista2.append(x.nombre)
    return lista1.intercection(lista2)
#.items para recuperar el elemento 
