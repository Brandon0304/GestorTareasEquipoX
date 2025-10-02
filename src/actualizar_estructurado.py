#Este archivo actualiza una tarea
def actualizar_tarea(tareas, indice, nueva_tarea):
    """
    Reemplaza una tarea existente en una posición dada.
    """
    if indice >= 0 and indice < len(tareas):
        tareas[indice] = nueva_tarea
        print(f"Tarea {indice+1} actualizada a: {nueva_tarea}")
    else:
        print("❌ Índice inválido.")
