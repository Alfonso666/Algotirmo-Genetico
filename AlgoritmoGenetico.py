# -*- coding: utf-8 -*-
#Ejercicio Practico en sala (Posible Solucion)
#Alfonso Duarte.
#Algoritmos de Optimizacion

import random
import datetime

setDeGenes = " abcdefghijklmnopqrstuvwxyz"
objetivo = "quiero aprobar algoritmos de optimizacion"


def generar_padre(largo):
    genes = []
    while len(genes) < largo:
        largoMuestral = min(largo - len(genes), len(setDeGenes))
        genes.extend(random.sample(setDeGenes, largoMuestral))#elegimos genes randomicamente
    return ''.join(genes)


def obtener_aptitud(frase):
    return sum(1 for esperado, real in zip(objetivo, frase)if esperado == real)


def mutar(padre):
    indice = random.randrange(0, len(padre)) #eligo un indice del padre randomicamente
    genesDelHijo = list(padre)
    nuevoGen, alterno = random.sample(setDeGenes, 2)
    genesDelHijo[indice] = alterno if nuevoGen == genesDelHijo[indice] else nuevoGen
    return ''.join(genesDelHijo)


def mostrar(frase):
    aptitud = obtener_aptitud(frase)
    print frase + "  Aptitud: " + str(aptitud)


mejorPadre = generar_padre(len(objetivo))
mejorAptitud = obtener_aptitud(mejorPadre)
mostrar(mejorPadre)


while True:
    hijo = mutar(mejorPadre)
    hijoAptitud = obtener_aptitud(hijo)
    if mejorAptitud >= hijoAptitud:
        continue
    mostrar(hijo)
    if hijoAptitud == len(mejorPadre):
        break
    mejorAptitud = hijoAptitud
    mejorPadre = hijo
