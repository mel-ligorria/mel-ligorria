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
