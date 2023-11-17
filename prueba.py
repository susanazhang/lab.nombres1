from nombres import *
if __name__=="__main__":
    datos_nombres=leer_frecuencias_nombres(r'data\frecuencias_nombres.csv')
    filtro=filtrar_por_genero(datos_nombres,"mujer")
    nombres=calcular_nombres(datos_nombres,"mujer")
    calcu_top=calcular_top_nombres_de_año(datos_nombres,2002,"hombre",10)
    nombre_comun=calcular_nombres_ambos_generos(datos_nombres)
