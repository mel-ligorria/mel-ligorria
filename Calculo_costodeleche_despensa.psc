Algoritmo Calculo_costodeleche_despensa
	Definir Unidades_deleche Como Entero
    Definir es_jubilado Como Logico
    Definir Monto_Parcial, monto_a_pagar Como Real
	
    Escribir "Ingrese la cantidad de unidades de leche que usted desea comprar: "
    Leer Unidades_deleche
	
    Escribir "¿Es usted jubilado? si/no: "
    Leer respuesta_jubilado
    es_jubilado = respuesta_jubilado == "si"
	
    Monto_Parcial = Unidades_deleche * 1000
    Escribir "unidadesdeleche ", Unidades_deleche, " esJubilado ", es_jubilado
	
    Si Unidades_deleche <= 12 y no es_jubilado Entonces
        Escribir "unidadesdeleche <= 12 and not es_jubilado"
        monto_a_pagar = Monto_Parcial
    Sino
        Si Unidades_deleche > 12 y Unidades_deleche <= 24 y no es_jubilado Entonces
            Escribir "unidadesdeleche > 12 and unidadesdeleche <= 24 and not es_jubilado"
            monto_a_pagar = Monto_Parcial * 0.9
        Sino
            Si Unidades_deleche > 24 y no es_jubilado Entonces
                Escribir "unidadesdeleche > 24 and not es_jubilado"
                monto_a_pagar = Monto_Parcial * 0.85
            FinSi
        FinSi
    FinSi
	
    Si Unidades_deleche <= 12 y es_jubilado Entonces
        Escribir "Unidades_deleche <= 12 and es_jubilado"
        monto_a_pagar = Monto_Parcial * 0.9
    Sino
        Si Unidades_deleche > 12 y Unidades_deleche <= 24 y es_jubilado Entonces
            Escribir "unidadesdeleche > 12 and unidadesdeleche <= 24 and es_jubilado"
            monto_a_pagar = Monto_Parcial * 0.8
        Sino
            Si Unidades_deleche > 24 y es_jubilado Entonces
                Escribir "unidadesdeleche > 24 and es_jubilado"
                monto_a_pagar = Monto_Parcial * 0.75
            FinSi
        FinSi
    FinSi
	
    Escribir "El costo total sin descuento es: ", Monto_Parcial, " y el monto total a pagar con descuento es ", monto_a_pagar, "."
	
FinAlgoritmo
