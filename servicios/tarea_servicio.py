from modelos.tarea import Tarea

class TareaServicio:
    def __init__(self):
        self.tareas = []
        self.next_id = 1

    def agregar_tarea(self, descripcion):
        tarea = Tarea(self.next_id, descripcion)
        self.tareas.append(tarea)
        self.next_id += 1
        return tarea

    def marcar_completada(self, id):
        for tarea in self.tareas:
            if tarea.id == id:
                tarea.completada = True
                return True
        return False

    def eliminar_tarea(self, id):
        for i, tarea in enumerate(self.tareas):
            if tarea.id == id:
                del self.tareas[i]
                return True
        return False

    def obtener_tareas(self):
        return self.tareas