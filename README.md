# Tarea Semana 16: Aplicación GUI - Lista de Tareas con Atajos de Teclado

**Autor:** ANDREW DAVID VALENZUELA YELA

## Objetivo

Desarrollar una nueva versión del sistema trabajado en la Semana 15, partiendo de la aplicación de lista de tareas previamente implementada, incorporando mejoras en la interacción mediante el uso de atajos de teclado. El estudiante deberá mantener estrictamente la arquitectura modular por capas, evidenciando una evolución del sistema sin alterar la separación de responsabilidades.


## Arquitectura

El sistema sigue una arquitectura modular por capas:

- **Capa de Modelo** (`modelos/`): Define la estructura de datos (Tarea).
- **Capa de Servicio** (`servicios/`): Contiene la lógica de negocio y operaciones CRUD.
- **Capa de Presentación** (`ui/`): Maneja la interfaz gráfica y eventos de usuario.
- **Capa de Inicio** (`main.py`): Punto de entrada que inicializa la aplicación.
