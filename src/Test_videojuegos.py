'''
Created on 16 dic. 2020

@author: jesus
'''
from videojuegos import *
ruta = '../data/videojuegos.csv'
lista_juegos = lee_juegos(ruta)
#print(lista_juegos)
print(genero_mas_presente(lista_juegos))