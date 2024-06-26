lista_tareas = []

def modificar_estado_tarea():
    id_tarea = int(input("Ingrese el ID de la tarea: "))
    
    tarea = next((t for t in lista_tareas if t['id'] == id_tarea), None)
    
    if tarea:
        # Mostrar opciones de estado
        print("Seleccione el nuevo estado de la tarea:")
        print("1. Pendiente")
        print("2. Realizada")
        print("3. Observada")
        
        opcion_estado = input("Ingrese el número correspondiente al nuevo estado: ")
        estados = {"1": "Pendiente", "2": "Realizada", "3": "Observada"}
        
        if opcion_estado in estados:
            # Actualizar el estado de la tarea
            tarea['estado'] = estados[opcion_estado]
            print(f"El estado de la tarea con ID {id_tarea} ha sido actualizado a {tarea['estado']}.")
        else:
            print("Opción de estado no válida.")
    else:
        print("Tarea no encontrada.")

def listar_tareas():
    if not lista_tareas:
        print("No hay tareas para mostrar.")
    else:
        print("\nListado de Tareas:")
        for tarea in lista_tareas:
            print(f"ID: {tarea['id']}, Descripción: {tarea['descripcion']}, Estado: {tarea['estado']}, Categoría: {tarea['categoria']}")

def listar_tareas():
    if not lista_tareas:
        print("No hay tareas para mostrar.")
    else:
        print("\nListado de Tareas:")
        for tarea in lista_tareas:
            print(f"ID: {tarea['id']}, Descripción: {tarea['descripcion']}, Estado: {tarea['estado']}, Categoría: {tarea['categoria']}")
        