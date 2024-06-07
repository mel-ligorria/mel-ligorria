Algoritmo Calculo_costomanodeobra
	Definir ancho, alto, costo_pormetrocuadrado, area, costo_total Como Real
	Escribir " Ingrese el ancho de la pared en metros: "
	Leer ancho
	Escribir "Ingrese el alto de la pared en metros: "
	Leer alto
	Escribir "Ingrese el costo por metro cuadrado de pintura: "
	Leer costo_pormetrocuadrado
	area= ancho* alto
	
	costo_total = area* costo_pormetrocuadrado
	Escribir "El costo total de la mano de obra para pintar la pared es: " costo_total
	
FinAlgoritmo
