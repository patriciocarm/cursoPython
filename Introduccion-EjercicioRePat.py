# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 09:43:31 2025

@author: Patricio Carmona
"""

%reset -f
import math

a=22.8+35.3
b=25-10
c=3.14*5
d=50/4
e=125**0.5
math.sqrt(125)

type(a)
type(b)
type(c)
type(d)
type(e)
nombre="Patricio Carmona"
LugarNacimiento="Sevilla"
LugarResidencia="Bilbao"
datos="Me llamo " + nombre +" nací en " +LugarNacimiento +" y vivo en " +LugarResidencia
len(datos)
datos[-6:]
nombre[::9]
datos[9:20:9]

datos = datos.lower()
"patricio" in datos
datos.count("a")

listDatos=datos.split(" ")
datos = datos.upper()

diasSemana =["Lunes","Martes","Miércoles","Jueves","Viernes"]
diasMes=[10,11,12,13,14]
type(diasSemana[0])
type(diasMes[0])

datosMes=diasSemana+diasMes

listaLarga = " ".join(diasSemana)

listaLarga = listaLarga.split(" ")
"Lunes" in datosMes
4 in datosMes


datosMes.remove("Viernes")
datosMes.remove(14)

datosMes.insert(4,"Sábado")
datosMes.insert(5,"Domingo")
datosMes.append(15)
datosMes.append(16)












