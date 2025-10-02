print('Bienvenido al Gestor de Tareas en Python')

# Listar tareas - Paradigma POO

class GestorTareas:
    def __init__(self, tareas):
        self.tareas = tareas

    def listar_tareas(self):
        """
        Muestra las tareas almacenadas.
        """
        if not self.tareas:
            print("No hay tareas.")
        else:
            print("📋 Lista de tareas:")
            for i, tarea in enumerate(self.tareas, 1):
                print(f"{i}. {tarea}")
