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


"""
Ejercicios Python básico.

Operaciones básicas
Sumar 22,8 y 35,3
Restar 25-10
Multiplicar 3,14 por 5.
Dividir 50 entre 4.
Calcular de dos maneras la raíz cuadrada de 125.

Creación de variables simples
Crear variables con las operaciones anteriores.
Comprobación de la clase
Comprobar la clase de las variables creadas.

Creación de cadenas.
Crear tres cadenas: Nombre y apellidos, lugar de nacimiento y lugar de residencia. 
Comprobar el tipo de dato cada una de las cadenas.

Concatenación de cadenas.
Crear la frase  “Me llamo ” “, nací en “ “ pero vivo en “ con vuestros datos concatenando frases.
Medir la longitud de la cadena creada.

Extracción elementos de la cadena
Extraer la ciudad en la que vivís.
Extraer vuestras iniciales.
		
Transformar en mayúsculas/minúsculas.


Poner todo con minúsculas.






Comprobar si existen ciertos elementos.


Comprobar si existe vuestro nombre.
Comprobar el número de veces que aparece la letra “a”.




Separar una cadena


Separar vuestra cadena por espacios.




Transformar una cadena.


Poner vuestros datos en mayúsculas.




Creación de listas
Crear dos listas con los días de la semana y los días del mes del curso.
Analizar el tipo de dato del primer elemento de cada lista.
Concatenar las dos listas.
Crear una lista encadenando los elementos de la lista 1
Comprobar si existe el lunes y el día 4 en la lista concatenada.
Eliminar el viernes y su correspondiente día del mes.
Añadir el fin de semana y sus días del mes correspondientes en su lugar.






"""












