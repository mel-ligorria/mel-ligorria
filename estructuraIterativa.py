#ESTRUCTURA ITERATIVA
#Consignas de Estructuras iterativas
#Mostrar los números desde el 0 al número solicitado al usuario (input)
numero = int (input ("Ingrese un numero entero: "))
for i in range (numero + 1):
     print (i,numero)

#Mostrar sólo los números pares desde 0 hasta el número ingresado (input). Nota: para saber si un número es par hacer i % 2 == 0)
#Se solciita al usuario que ingrese un número entero
numero = int(input("Ingrese un numero entero: "))
for i in range (0, numero +1):
     if i % 2 == 0:
          print (i)

#tructura iterativa: Pedir que el usuario ingrese (input) nombre de personas y mostrarlos hasta que el valor de lo que ingresa sea “fin”
nombre = ""
while nombre.lower() != "fin":
    nombre = input("Ingrese el nombre de una persona (o 'fin' para terminar): ")
    if nombre.lower() != "fin":
        print(nombre)

print("Programa finalizado")

#En una escuela, luego de tomar un determinado examen, es necesario calcular el promedio de notas (las notas van de 0 a 10) de los alumnos de un curso. Se necesita saber si el rendimiento ha sido elevado (el promedio es mayor a 8), aceptable (el promedio está comprendido entre 6 y 8) o bajo (promedio es inferior a 6). Desarrollar un algoritmo que resuelva este problema. Para tener en cuenta: las autoridades del colegio saben cuántos estudiantes del curso han rendido el examen. 

total_estudiantes = int(input ("Ingrese el total de estudiantes: "))
suma_denotas= 0
for i in range (1, total_estudiantes +1):
    nota= float(input(f"Ingrese la nota de los estudiantes {i} : "))
    suma_denotas += nota

promedio= suma_denotas / total_estudiantes

if promedio >8:
     print ("rendimiento elevado")
elif promedio >=6:
     print ("rendimiento aceptable")
else:
    print ("rendimiento bajo")

print(f"\nEl promedio de las notas es: {promedio:.2f}")