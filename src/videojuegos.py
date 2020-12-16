'''
Created on 16 dic. 2020

@author: jesus
'''
import csv
from matplotlib import pylab as plt
from collections import namedtuple

Juego = namedtuple('Juego','rank, name, platform, year, genre, publisher, NA_sales, EU_sales, JP_sales, other_sales, global_sales')


def lee_juegos(fichero):
    with open(fichero,'r', encoding='utf-8')as f:
        lector = csv.reader(f)
        next(lector)
        res = [Juego(int(rank), str(name),str(platform),int(year), str(genre),float(NA_sales),float(EU_sales),float(JP_sales),float(other_sales),float(global_sales))for rank, name, platform, year, genre, publisher, NA_sales, EU_sales, JP_sales, other_sales, global_sales in lector]
        return res
def num_juegos_mas_ventas_JP(lista_juegos):
    lista_aux = []
    for Juego in lista_juegos:
        if Juego.JP_sales >Juego.NA_sales:
            lista_aux.append(Juego.name)
    res = len(lista_aux)
    return res

def juegos_distribuidora_anyo(lista_juegos, publisher, anyo):
    res = []
    for Juego in lista_juegos:
        if Juego.publisher == publisher and anyo == Juego.year:
            res.append(Juego.name)
    return res 
def num_distribuidoras(lista_juegos):
    res = {Juego.publisher for Juego in lista_juegos}
    return len(res)
def juego_mas_antiguo(lista_juegos):
    pass
    
        