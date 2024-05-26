Algoritmo Calculo_costodeleche_despensa
	Definir Unidades_deleche Como Entero
    Definir es_jubilado Como Logico
    Definir Monto_Parcial, monto_a_pagar Como Real
	Definir respuesta Como Caracter
	
    Escribir "Ingrese la cantidad de unidades de leche que usted desea comprar: "
    Leer Unidades_deleche
	
    Escribir "¿Es usted jubilado? si/no: "
    Leer respuesta_jubilado
    
	
    Monto_Parcial = Unidades_deleche * 1000
    Escribir "unidadesdeleche ", Unidades_deleche, " esJubilado ", es_jubilado
	
    Si Unidades_deleche <= 12 Entonces
        Escribir "unidadesdeleche <= 12"
        monto_a_pagar = Monto_Parcial
    Sino
        Si Unidades_deleche > 12 y Unidades_deleche <= 24 Entonces
            Escribir "Unidades_deleche > 12 y Unidades_deleche <= 24"
            monto_a_pagar = Monto_Parcial - (Monto_Parcial * 0.1)
        Sino
            Si Unidades_deleche > 24 Entonces
                Escribir "unidades_deleche > 24"
                monto_a_pagar = Monto_Parcial - (Monto_Parcial * 0.15)
            FinSi
        FinSi
    FinSi
	
	Si es_jubilado Entonces
        Escribir "Usted tiene un descuento"
        monto_a_pagar = monto_a_pagar - (monto_a_pagar * 0.1)
    FinSi
	
    Escribir "El costo total sin descuento es: ", Monto_Parcial, " y el monto total a pagar con descuento es: ", monto_a_pagar, "."
   
FinAlgoritmo
