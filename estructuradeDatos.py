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
     
