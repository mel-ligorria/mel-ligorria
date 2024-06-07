def saludar():
    print ('')
    print ("Hola, cómo estas")
    print ('')

    for i in range (3):
        saludar()


# En un curso de colegio se decidiò sortear un  torta entre los mejores promedios del aula.
# Crear un programa que permita almacenar  los nombres de los alumnos y escoja uno al azar que sea el ganador del sorteo

import random

nombres = [ ]

while True:
    if nombres != "0":
        nombre= input ("Ingrese un nombre o un 0 para terminar")
        nombres.append (nombre)
    else:
        break 

print (nombres)

nombre_al_azar: random.choice(nombres)

print ("El ganador/a  de la torta es: ", nombre_al_azar)

#Colecciones de funciones
def sumar (numero1,numero2): 
    sumar = numero1 + numero2
    return sumar  

def restar (numero1,numero2): 
   restar = numero1 - numero2
   return restar

def multiplicar (numero1,numero2): 
   multiplicar = numero1 * numero2
   return multiplicar 

def dividir (numero1, numero2): 
    if numero2 != 0:
      cociente = numero1 / numero2
    else:
      conciente = "división por cero"
    return conciente