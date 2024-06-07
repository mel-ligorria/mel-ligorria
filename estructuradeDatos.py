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
    print(nombre)

#Eliminar la tercer y la última persona de la lista del ejercicio 1, luego ordenar la lista y mostrarlo
nombres.pop (2)
nombres.pop ()
print (nombres)

nombres.sort()
print("\n mostrar orden de la lista, luego de haber eliminado la tercera y última persona: ")
for nombre in nombres:
     print(nombre)
#Guardar en un diccionario los datos de una persona: nombre, apellido, dni, email, fecha de nacimiento.
datos_personas = {"nombre": "Melania", "apellido": "Ligorria", "dni": 38412646, "email": "melanialigorria@gmail.com", "fecha de nacimiento": "29/8/1994"}
print (datos_personas)

# En un nuevo diccionario llamado familia guardar 4 personas, cada una de ellas con los mismos 5 datos (nombre, apellido, dni, email, fecha de nacimiento)
info_melania= {"nombre": "Melania", "apellido": "Ligorria", "dni": 38412646, "email": "melanialigorria@gmail.com", "fecha de nacimiento": "29/8/1994"}
info_sonia= {"nombre": "Sonia", "apellido": "Solis", "dni": 17056184, "email": "soniasolis@gmail.com", "fecha de nacimiento": "02/12/1964"}
info_noah= {"nombre": "Noah", "apellido": "Abrego", "dni": 37134987, "email": "noahabrego@gmail.com", "fecha de nacimiento": "03/07/2000"}
info_renzo= {"nombre": "Renzo", "apellido":"Lemos", "dni": 30456123, "email": "renzolemos@gmail.com", "fecha de nacimiento": "07/07/1990"}

familia = {
    "persona1": info_melania,
    "persona2": info_sonia,
    "persona3": info_noah,
    "persona4": info_renzo
}

print(familia)     

#Guardar en una tupla los primeros n números pares. El valor de n que lo ingrese el usuario (input). 
n = int(input("Ingrese la cantidad de números que desee almacenar en la estructura de datos llamada tupla: "))
pares = []

contador= 0
numero= 0
while contador < n:
    if numero % 2 == 0:
        pares.append(numero)
        contador += 1
    numero += 1
pares_estructuradatostuplas = tuple (pares)

print ("Los primeros", n, "números pares son:", pares_estructuradatostuplas)

