#Calcular_promedio
notas_materias = input("A continuación Ingrese las cincos notas de cada materia")
nota1= float(input ("Ingrese la nota de la materia 1: "))
nota2= float(input ("Ingrese la nota de la materia 2: "))
nota3= float(input ("Ingrese la nota de la materia 3: "))
nota4= float(input ("Ingrese la nota de la materia 4: "))
nota5= float(input ("Ingrese la nota de la materia 5: "))

promedio= (nota1 + nota2 + nota3 + nota4 + nota5) /5

print ('El promedio de las cinco nota es: ', promedio)

#Calculo_costomanodeobra
ancho= float(input( "Ingrese el ancho de la pared en metros: "))
alto= float (input("Ingrese el alto de la pared en metro: "))

costo_pormetrocuadrado = float(input("Ingrese el costo por metro cuadrado de pintura: "))
area= ancho* alto

costo_total= area * costo_pormetrocuadrado

print ("El costo total de la mano de obra para pintar la pared es: ", costo_total)
 
 #Calculo_puntosdelequipo
partidos_ganados = int(input("Ingrese la cantidad de partidos ganados: "))
partidos_perdidos = int (input("Ingrese la cantidad de partidos perdidos: "))
partidos_empatados = int (input("Ingrese la cantidad de partidos empatados: "))
total_depuntos= (partidos_ganados * 3) + (partidos_empatados *1)

print("El equipo acumuló", total_depuntos, "puntos en el campeonato.")


#ESTRUCTURA CONDICIONAL
#Ejercicio parcial (solo el if) con expresión lógica simple
numero = float(input ("Ingrese un número: "))
if numero > 0:
     print (f"El número es:{numero} ")

#Condicional completo (if - else) con expresión lógica simple
#Corroborar si la persona es mayor de edad
edad= int(input ("Ingrese su edad: "))
if edad >= 18:
     print ("Usted es mayor de edad")
else:
     print ("Usted es menor de edad")
     
#Condicional parcial (solo el if) con expresión lógica compuesta (and)
#Corroborar si la persona puede acceder a la licencia de conducir
edad= int(input( "Ingrese su edad: "))
has_aprobadoelexamen = input("¿Usted ha aprobado el examen? (True/False): ")
has_aprobadoelexamen= has_aprobadoelexamen == True
if edad >= 18 and has_aprobadoelexamen:
     print("¡Felicitaciones obtuviste tu licencia de conducir!")

#Condicional completo (if - else) con expresión lógica compuesta (or)
#Verificamos si el número ingresado por el usuario es par o múltiplo por 5
numero = int(input("Ingrese un número: "))
if numero % 2 == 0 or numero % 5 == 0:
     print (f"El número {numero} ingresado es par o múltiplo por 5")
else:
     print ("El número {numero} ingresado no es par ni múltiplo por 5")

#Algoritmo Calculo_costodeleche_despensa
Unidades_deleche= int(input ("Ingrese la cantidad de unidades de leche que usted desea comprar: "))
es_jubilado = input("¿Es usted jubilado? si/no: ").strip().lower() == "si"
Monto_Parcial = Unidades_deleche* 1000
print (f"unidadesdeleche {Unidades_deleche} esJubilado {es_jubilado}")

if  (Unidades_deleche <= 12 and not es_jubilado):
    print ("unidadesdeleche <=12 and not esjubilad")
    monto_a_pagar = Monto_Parcial
elif (Unidades_deleche > 12 and Unidades_deleche <= 24) and not es_jubilado:
    print("(Unidades_deleche > 12 and Unidades_deleche <= 24) and not es_jubilado")
    monto_a_pagar = Monto_Parcial * 0.9 
elif (Unidades_deleche > 4 and not es_jubilado):
     print ("unidades_deleche > 24 and not es_jubilado")
     monto_a_pagar = Monto_Parcial * 0.85
if (Unidades_deleche <=12 and es_jubilado):
     print ("Unidades_deleche <= 12 ans es_jubilado")
elif ((Unidades_deleche <=12 and Unidades_deleche <= 24) and es_jubilado):
     print ("(unidades_deleche > 12 and unidades_deleche <= 24) and es_jubilado")
     monto_a_pagar= Monto_Parcial * 0.8
elif (Unidades_deleche >24 and es_jubilado):
     print ("unidades_deleche >24 and es_jubilado")
     monto_a_pagar =Monto_Parcial * 0.75


print (f"El costo total sin descuento es: {Monto_Parcial} y el monto total a pagar con descuento es {monto_a_pagar} .")


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

#ESTRUCTURAS DE DATOS
#Pedir al usuario que ingrese 10 nombres de personas (input en un ciclo) no repetidas, guardarlos en una lista y mostrarlos. 
nombres = []

while len(nombres) < 10:
    nombre = input("Ingrese un nombre: ")
    
    if nombre not in nombres:
        nombres.append(nombre)
    else:
        print("Este nombre ya ha sido ingresado, por favor ingrese un nombre diferente.")

print("\nLos nombres ingresados son:")
for nombre in nombres:
    print(nombres)

#Eliminar la tercer y la última persona de la lista del ejercicio 1, luego ordenar la lista y mostrarlo
nombres.pop (2)
nombres.pop ()
print (nombres)

nombres.sort()
print("\n mostrar orden de la lista, luego de haber eliminado la tercera y última persona: ")
for nombre in nombres:
     print(nombres)
     

