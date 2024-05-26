#ESTRUCTURA CONDICIONAL
#Ejercicio parcial (solo el if) con expresión lógica simple
numero = float(input ("Ingrese un número positivo: "))
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
if edad >= 18 and has_aprobadoelexamen.lower() == 'true': 
     print("¡Felicitaciones obtuviste tu licencia de conducir!")

#Condicional completo (if - else) con expresión lógica compuesta (or)
#Verificamos si el número ingresado por el usuario es par o múltiplo por 5
numero = int(input("Ingrese un número: "))
if numero % 2 == 0 or numero % 5 == 0:
     print (f"El número {numero} ingresado es par o múltiplo por 5")
else:
     print (f"El número {numero} ingresado no es par ni múltiplo por 5")

#Algoritmo Calculo_costodeleche_despensa
Unidades_deleche= int(input ("Ingrese la cantidad de unidades de leche que usted desea comprar: "))
es_jubilado = input("¿Es usted jubilado? si/no: ").strip().lower() == "si"
Monto_Parcial = Unidades_deleche* 1000
print (f"unidadesdeleche {Unidades_deleche} esJubilado {es_jubilado}")

if  Unidades_deleche <= 12:
    print ("unidadesdeleche <=12")
    monto_a_pagar = Monto_Parcial
elif Unidades_deleche > 12 and Unidades_deleche <= 24:
    print("Unidades_deleche > 12 and Unidades_deleche <= 24")
    monto_a_pagar = (Monto_Parcial - (Monto_Parcial* 0.1))
elif Unidades_deleche > 24:
     print ("unidades_deleche > 24")
     monto_a_pagar = (Monto_Parcial - (Monto_Parcial* 0.15))

if es_jubilado:
    print ("Usted tiene un descuento")
    monto_a_pagar= monto_a_pagar - (monto_a_pagar * 0.1)


print (f"El costo total sin descuento es: {Monto_Parcial} y el monto total a pagar con descuento es {monto_a_pagar} .")

