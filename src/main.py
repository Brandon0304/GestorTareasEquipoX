from crear_funcional import crear_tarea
from listar_poo import GestorTareas
from actualizar_estructurado import actualizar_tarea
from eliminar_declarativo import eliminar_tarea


def main():
    print("\n===== BIENVENIDO AL GESTOR DE TAREAS =====\n")

    # Lista inicial vacía
    tareas = []

    # --- Crear tareas (Funcional) ---
    tareas = crear_tarea(tareas, "Estudiar Python")
    tareas = crear_tarea(tareas, "Practicar Git")
    print("\n✅ Se crearon dos tareas.\n")

    # --- Listar tareas (POO) ---
    gestor = GestorTareas(tareas)
    print("📋 Lista inicial de tareas:")
    gestor.listar_tareas()

    # --- Actualizar tarea (Estructurado) ---
    print("\n✏️  Actualizando la primera tarea...\n")
    actualizar_tarea(tareas, 0, "Estudiar Python y Git")

    # --- Listar nuevamente ---
    print("📋 Lista después de la actualización:")
    gestor = GestorTareas(tareas)
    gestor.listar_tareas()

    # --- Eliminar tarea (Declarativo) ---
    print("\n🗑️  Eliminando la segunda tarea...\n")
    tareas = eliminar_tarea(tareas, 1)

    # --- Listar final ---
    print("📋 Lista final de tareas:")
    gestor = GestorTareas(tareas)
    gestor.listar_tareas()

    print("\n===== FIN DE LA DEMOSTRACIÓN =====\n")


if __name__ == "__main__":
    main()
