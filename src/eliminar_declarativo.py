# Eliminar tarea - Paradigma Declarativo

def eliminar_tarea(tareas, indice):

    """
    Elimina una tarea usando list comprehension (declarativo).
    Devuelve una nueva lista sin la tarea indicada.
    """

    if indice >= 0 and indice < len(tareas):
        return [t for i, t in enumerate(tareas) if i != indice]
    else:
        print("❌ Índice inválido.")
        return tareas
