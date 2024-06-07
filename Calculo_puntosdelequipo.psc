Algoritmo Calculo_puntosdelequipo
	Definir partidos_ganados, partidos_perdidos, partidos_empatados Como Entero
	Definir total_depuntos Como Entero
	Escribir "Ingrese la cantidad de partidos ganados: " 
	Leer partidos_ganados
	Escribir "Ingrese la canditas de partidos perdidos: "
	Leer partidos_perdidos
	Escribir "Ingrese la canditas de partidos empatados: "
	Leer partidos_empatados
	
	total_depuntos =  (partidos_ganados * 3) + (partidos_empatados * 1)
	
	Escribir " El equipo acumulo " total_depuntos " puntos en el campeonato."
	
FinAlgoritmo
